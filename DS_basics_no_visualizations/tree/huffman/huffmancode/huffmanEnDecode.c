#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct HuffmanNode
{
    char value;
    int freq;
    int index;
    struct HuffmanNode *parent, *left, *right;
} HuffmanNode;

HuffmanNode *nodes_list[512];
int nodes_count = 0;

HuffmanNode *createNode(char value, int freq)
{
    HuffmanNode *node = (HuffmanNode *)malloc(sizeof(HuffmanNode));
    node->value = value;
    node->freq = freq;
    node->index = nodes_count;
    nodes_list[nodes_count++] = node;
    node->parent = node->left = node->right = NULL;
    return node;
}

int comparator(const void *p, const void *q)
{
    return ((HuffmanNode *)p)->freq - ((HuffmanNode *)q)->freq;
}
HuffmanNode *buildHuffmanTree(const char *data)
{
    int freq[256] = {0};
    int i;
    for (i = 0; data[i]; i++)
    {
        freq[(unsigned char)data[i]]++;
    }

    HuffmanNode *heap[256];
    int heapSize = 0;
    for (i = 0; i < 256; i++)
    {
        if (freq[i] > 0)
        {
            heap[heapSize++] = createNode(i, freq[i]);
        }
    }

    while (heapSize > 1)
    {
        qsort(heap, heapSize, sizeof(HuffmanNode *), comparator); // 这一步是关键，每次都要把频率最小的两个节点放在最前面

        HuffmanNode *left = heap[0];
        HuffmanNode *right = heap[1];
        for (i = 0; i < heapSize - 2; i++)
        {
            heap[i] = heap[i + 2];
        }
        heapSize -= 2;

        HuffmanNode *parent = createNode(0, left->freq + right->freq);
        parent->left = left;
        parent->right = right;
        left->parent = parent;
        right->parent = parent;

        printf("合并节点 %d(%c:%d) 和 %d(%c:%d)，生成新节点 %d(%d)\n",
               left->index, left->value ? left->value : ' ', left->freq,
               right->index, right->value ? right->value : ' ', right->freq,
               parent->index, parent->freq);

        heap[heapSize++] = parent;
    }

    return heap[0];
}

void printHuffmanTree()
{
    printf("---------------------------------------------------------------------\n");
    printf("| Index |  Node  | Weight | Parent | Left Child | Right Child |\n");
    printf("---------------------------------------------------------------------\n");
    int i;

    for (i = 0; i < nodes_count; i++)
    {
        char nodeStr = nodes_list[i]->value ? nodes_list[i]->value : ' ';
        int parentIndex = nodes_list[i]->parent ? nodes_list[i]->parent->index : -1;
        int leftIndex = nodes_list[i]->left ? nodes_list[i]->left->index : -1;
        int rightIndex = nodes_list[i]->right ? nodes_list[i]->right->index : -1;
        printf("|%7d|%8c|%8d|%8d|%12d|%13d|\n",
               nodes_list[i]->index, nodeStr, nodes_list[i]->freq, parentIndex, leftIndex, rightIndex);
    }
    printf("---------------------------------------------------------------------\n");
}

void buildHuffmanTable(HuffmanNode *node, char *code, char table[256][256])
{
    if (node->value)
    {
        strcpy(table[(unsigned char)node->value], code);
        return;
    }
    if (node->left)
    {
        char newCode[256];
        sprintf(newCode, "%s0", code);
        buildHuffmanTable(node->left, newCode, table);
    }
    if (node->right)
    {
        char newCode[256];
        sprintf(newCode, "%s1", code);
        buildHuffmanTable(node->right, newCode, table);
    }
}

char *encode(const char *data, char table[256][256])
{
    static char encoded[4096];
    encoded[0] = '\0';
    int i;
    for (i = 0; data[i]; i++)
    {
        strcat(encoded, table[(unsigned char)data[i]]);
    }
    return encoded;
}

char decodeChar(HuffmanNode *root, const char **pencoded)
{
    HuffmanNode *node = root;
    while (!node->value && **pencoded)
    {
        node = **pencoded == '0' ? node->left : node->right;
        (*pencoded)++;
    }
    return node->value;
}

char *decode(const char *encoded, HuffmanNode *root)
{
    static char decoded[1024];
    char *pdecoded = decoded;
    while (*encoded)
    {
        *pdecoded++ = decodeChar(root, &encoded);
    }
    *pdecoded = '\0';
    return decoded;
}
int main()
{
    const char data[] = "This is a test message for Huffman coding.";
    HuffmanNode *root = buildHuffmanTree(data);

    char table[256][256] = {0};
    buildHuffmanTable(root, "", table);

    char *encodedData = encode(data, table);
    char *decodedData = decode(encodedData, root);

    printHuffmanTree();
    printf("原始数据：%s\n", data);
    printf("编码后的数据：%s\n", encodedData);
    printf("解码后的数据：%s\n", decodedData);

    return 0;
}