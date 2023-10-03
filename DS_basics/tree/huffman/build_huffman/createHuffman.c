#include <stdio.h>
#include <stdlib.h>

typedef struct HuffmanNode
{
    int value;
    int freq;
    struct HuffmanNode *left;
    struct HuffmanNode *right;
} HuffmanNode;

HuffmanNode *build_huffman_tree(int *weights, int n)
{
    // 构建哈夫曼树
    HuffmanNode **nodes = (HuffmanNode **)malloc(n * sizeof(HuffmanNode *));
    int i;
    for (i = 0; i < n; i++)
    {
        nodes[i] = (HuffmanNode *)malloc(sizeof(HuffmanNode));
        nodes[i]->value = i;
        nodes[i]->freq = weights[i];
        nodes[i]->left = NULL;
        nodes[i]->right = NULL;
    }

    int index = n;
    while (n > 1)
    {
        // 选取权值最小的两个节点
        int min1 = 0, min2 = 1;

       
        if (nodes[min1]->freq > nodes[min2]->freq)
        {
            int temp = min1;
            min1 = min2;
            min2 = temp;
        }
        for ( i = 2; i < n; i++)
        {
            if (nodes[i]->freq < nodes[min1]->freq)
            {
                min2 = min1;
                min1 = i;
            }
            else if (nodes[i]->freq < nodes[min2]->freq)
            {
                min2 = i;
            }
        }

        // 将它们作为左右子节点，构建一个新的节点作为它们的父节点
        HuffmanNode *parent = (HuffmanNode *)malloc(sizeof(HuffmanNode));
        parent->value = index;
        parent->freq = nodes[min1]->freq + nodes[min2]->freq;
        parent->left = nodes[min1];
        parent->right = nodes[min2];
        index++;

        // 将新节点插入到列表中
        nodes[min1] = parent;
        nodes[min2] = nodes[n - 1];
        n--;
    }

    // 返回哈夫曼树的根节点
    HuffmanNode *root = nodes[0];
    free(nodes);
    return root;
}

void print_huffman_tree(HuffmanNode *root)
{
    // 创建表格
    printf("%-6s%-8s%-8s%-12s%-12s\n", "Index", "Weight", "Parent", "Left Child", "Right Child");

    // 遍历哈夫曼树，将每个节点添加到表格中
    HuffmanNode *queue[1000];
    int front = 0, rear = 0;
    queue[rear++] = root;
    while (front < rear)
    {
        HuffmanNode *node = queue[front++];
        printf("%-6d%-8d%-8d%-12d%-12d\n", node->value, node->freq, node->left ? node->left->value : -1, node->left ? node->left->value : -1, node->right ? node->right->value : -1);
        if (node->left)
        {
            queue[rear++] = node->left;
        }
        if (node->right)
        {
            queue[rear++] = node->right;
        }
    }
}

int main()
{
    // 测试代码
    int weights[] = {5, 29, 7, 8, 14, 23, 3, 11};
    int n = sizeof(weights) / sizeof(weights[0]);
    HuffmanNode *root = build_huffman_tree(weights, n);
    print_huffman_tree(root);
    return 0;
}