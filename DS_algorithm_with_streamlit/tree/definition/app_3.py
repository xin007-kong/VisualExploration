import streamlit as st

# Create a button to create a tree
create_tree_button = st.button("Create Tree")

# Define a function to create a tree
# Define the tree data structure


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree(values):
   tree = Tree(values[0])
   for value in values[1:]:
       if value < tree.value:
           if tree.left is None:
               tree.left = Tree(value)
           else:
               tree.left.value = value
       else:
           if tree.right is None:
               tree.right = Tree(value)
           else:
               tree.right.value = value
   return tree

# Define a function to traverse the tree


def traverse(node):
   if node is None:
       return
   print(node.value)
   traverse(node.left)
   traverse(node.right)


# Create a text area to display the tree's values
tree_values = st.text_area("Tree Values:", "")

# Create a button to traverse the tree
traverse_button = st.button("Traverse Tree")

# Define the callback function for the create tree button



def create_tree_callback(values):
   tree = create_tree(values)
   tree_values.value = str(tree)

# Define the callback function for the traverse button



def traverse_callback():
   traverse(tree)
