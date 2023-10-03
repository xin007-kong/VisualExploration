import streamlit as st
from collections import Counter
import heapq
from nltk.corpus import wordnet
import matplotlib.pyplot as plt
import graphviz


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.freq == other.freq

    def __hash__(self):
        return hash(str(self.char) + str(self.freq))


def build_huffman_tree(freqs):
    heap = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def encode_tree(node, prefix="", code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix
        encode_tree(node.left, prefix + "0", code)
        encode_tree(node.right, prefix + "1", code)
    return code


@st.cache
def get_synset_words(num_words=100):
    # wordnet = download_and_load_wordnet()
    synsets = list(wordnet.all_synsets())[:num_words]
    words = []
    for syn in synsets:
        words.extend(syn.lemma_names())
    return words


def get_synset_words(num_words=100):
    # Fetch a limited number of synsets
    synsets = list(wordnet.all_synsets())[:num_words]

    words = []
    for syn in synsets:
        # Take the lemma names for each synset
        words.extend(syn.lemma_names())

    return words


def plot_frequencies(freqs):
    words, frequencies = zip(*freqs.most_common())
    plt.figure(figsize=(10, 5))
    plt.bar(words, frequencies)
    plt.ylabel("Frequencies")
    plt.xticks(rotation=45)
    st.pyplot(plt)


def plot_huffman_tree(node, dot=None):
    if dot is None:
        dot = graphviz.Digraph()
        dot.node('0', 'root')

    if node.left:
        left_id = str(hash(node.left))
        dot.node(left_id, str(node.left.char) + ':' + str(node.left.freq))
        dot.edge(str(hash(node)), left_id, label="0")
        plot_huffman_tree(node.left, dot)

    if node.right:
        right_id = str(hash(node.right))
        dot.node(right_id, str(node.right.char) + ':' + str(node.right.freq))
        dot.edge(str(hash(node)), right_id, label="1")
        plot_huffman_tree(node.right, dot)

    return dot


def display_tree(node, indent="", last='updown'):
    """A recursive function to display the tree in a textual format."""

    nb_children = sum((node.left is not None, node.right is not None))
    if last == 'updown':
        # Names of the links. Also change them if needed
        up = '|- '
        down = '|- '
    else:
        up = '|- '
        down = '|  '

    if node.left is not None:
        yield "".join([indent, up, node.left.char or "[...]", "(", str(node.left.freq), ")"])
        if last == 'up':
            indent += '   '
        else:
            indent += '|  '
        for nextIndent in display_tree(node.left, indent, 'up' if nb_children == 1 else 'updown'):
            yield nextIndent

    if node.right is not None:
        yield "".join([indent, down, node.right.char or "[...]", "(", str(node.right.freq), ")"])
        if last == 'down':
            indent += '   '
        else:
            indent += '|  '
        for nextIndent in display_tree(node.right, indent, 'down' if nb_children == 1 else 'updown'):
            yield nextIndent


def build_huffman_tree(freqs, display_process=False):
    heap = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)

    process_steps = []

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        if display_process:
            process_steps.append(
                f"Combine nodes '{left.char}'({left.freq}) and '{right.char}'({right.freq})")

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    if display_process:
        return heap[0], process_steps
    else:
        return heap[0]


def main():
    st.title("Huffman Coding with WordNet: Interactive Exploration")

    num_words = st.slider("Select number of WordNet entries",
                          10, 50, 15)  # Reduce max for clarity
    words = get_synset_words(num_words)

    freqs = Counter(words)
    root, process_steps = build_huffman_tree(freqs, display_process=True)
    codes = encode_tree(root)

    st.subheader("Word Frequencies from WordNet")
    plot_frequencies(freqs)

    st.subheader("Huffman Encoding Process")
    for step in process_steps:
        st.write(step)

    st.subheader("Huffman Tree")
    tree_dot = plot_huffman_tree(root)
    st.graphviz_chart(tree_dot)

    st.subheader("Explore Huffman Codes")
    word_to_explore = st.selectbox(
        "Choose a word to explore its Huffman code", list(freqs.keys()))
    st.write(f"Code for {word_to_explore}: {codes[word_to_explore]}")
    st.subheader("Huffman Tree - Textual View")
    for line in display_tree(root):
        st.text(line)


if __name__ == "__main__":
    main()
