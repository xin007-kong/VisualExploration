#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h> // 用于定义 INT_MAX

/*
本程序用于生成哈夫曼编码
程序结构如下：
1. 定义结构体 Node，用于存储哈夫曼树的节点
2. 定义结构体 HuffmanCode，用于存储哈夫曼编码
3. 定义函数 CreateHuffmanTree，用于生成哈夫曼树
4. 定义函数 SelectTwoSmallest，用于从哈夫曼树中选择两个权重最小的节点
5. 定义函数 CreateHuffmanCode，用于生成哈夫曼编码
6. 定义函数 test_case，用于测试
7. 定义函数 main，用于测试
*/

typedef struct
{
    int weight;
    int parent, lchild, rchild;
} Node, *HuffmanTree;

typedef char **HuffmanCode;

void PrintHuffmanTree(HuffmanTree HT, int n)
{
    int m = 2 * n - 1;
    printf("-------------------------------------------------\n");
    printf("| Node | Weight | Parent | Left Child | Right Child |\n");
    printf("-------------------------------------------------\n");
    int i;
    for (i = 1; i <= m; i++)
    {
        printf("| %5d | %6d | %6d | %11d | %12d |\n", i, HT[i].weight, HT[i].parent, HT[i].lchild, HT[i].rchild);
    }
    printf("-------------------------------------------------\n\n");
}

HuffmanCode CreateHuffmanCode(HuffmanTree HT, int n)
{
    HuffmanCode HC;
    char *cd;
    int start, c, f, i;

    HC = (HuffmanCode)malloc((n + 1) * sizeof(char *));
    cd = (char *)malloc(n * sizeof(char));
    cd[n - 1] = '\0';

    for (i = 1; i <= n; ++i)
    {
        // printf("Generating Huffman code for character %d...\n", i);
        // 把上面那个printf改成中文的
        printf("生成字符 %d 的哈夫曼编码...\n", i);

        start = n - 1;
        c = i;
        f = HT[i].parent;

        // printf("Starting from the leaf node and moving to the root...\n");
        // 把上面那个printf改成中文的
        printf("从叶子节点开始，向根节点移动...\n");

        while (f != 0)
        {
            --start;
            if (HT[f].lchild == c)
            {
                cd[start] = '0';
                // printf("Node %d is the left child of node %d, so add '0' to the code.\n", c, f);
                // 把上面那个printf改成中文的
                printf("节点 %d 是节点 %d 的左孩子，所以在编码中添加 '0'。\n", c, f);
            }
            else
            {
                cd[start] = '1';
                // printf("Node %d is the right child of node %d, so add '1' to the code.\n", c, f);
                // 把上面那个printf改成中文的
                printf("节点 %d 是节点 %d 的右孩子，所以在编码中添加 '1'。\n", c, f);
            }

            c = f;
            f = HT[f].parent;
        }

        HC[i] = (char *)malloc((n - start) * sizeof(char));
        strcpy(HC[i], &cd[start]);

        // printf("Huffman code for character %d: %s\n\n", i, HC[i]);
        // 把上面那个printf改成中文的
        printf("字符 %d 的哈夫曼编码: %s\n\n", i, HC[i]);
    }

    free(cd);
    return HC;
}

void SelectTwoSmallest(HuffmanTree HT, int n, int *s1, int *s2)
{
    int i;
    *s1 = 0;
    *s2 = 0;

    for (i = 1; i <= n; i++)
    {
        if (HT[i].parent == 0)
        {
            if (*s1 == 0 || HT[i].weight < HT[*s1].weight)
            {
                *s2 = *s1;
                *s1 = i;
            }
            else if (*s2 == 0 || HT[i].weight < HT[*s2].weight)
            {
                *s2 = i;
            }
        }
    }
    // printf("Selected two smallest nodes: %d and %d with weights: %d and %d\n", *s1, *s2, HT[*s1].weight, HT[*s2].weight);
    // 把上面那个printf改成中文的
    printf("选择了两个最小的节点: %d 和 %d，它们的权重分别为: %d 和 %d\n", *s1, *s2, HT[*s1].weight, HT[*s2].weight);
}

HuffmanTree CreateHuffmanTree(int *w, int n)
{
    int m = 2 * n - 1;
    HuffmanTree HT = (HuffmanTree)malloc((m + 1) * sizeof(Node));
    int i;

    for (i = 1; i <= n; ++i)
    {
        HT[i].weight = w[i - 1];
        HT[i].parent = 0;
        HT[i].lchild = 0;
        HT[i].rchild = 0;
    }

    for (i = n + 1; i <= m; ++i)
    {
        HT[i].weight = 0;
        HT[i].parent = 0;
        HT[i].lchild = 0;
        HT[i].rchild = 0;
    }

    for (i = n + 1; i <= m; ++i)
    {
        int s1, s2;
        SelectTwoSmallest(HT, i - 1, &s1, &s2);

        HT[s1].parent = i;
        HT[s2].parent = i;
        HT[i].lchild = s1;
        HT[i].rchild = s2;
        HT[i].weight = HT[s1].weight + HT[s2].weight;

        // printf("Connected nodes %d and %d to form new node %d with combined weight %d\n", s1, s2, i, HT[i].weight);
        // 把上面那个printf改成中文的
        printf("连接节点 %d 和 %d，形成新节点 %d，它们的权重之和为 %d\n", s1, s2, i, HT[i].weight);
    }
    PrintHuffmanTree(HT, n); // Printing the tree after it's constructed

    return HT;
}

void test_case(int *weights, int n)
{
    printf("Testing with weights: ");
    int j;
    for (j = 0; j < n; j++)
    {
        printf("%d ", weights[j]);
    }
    printf("\n");

    HuffmanTree HT = CreateHuffmanTree(weights, n);
    HuffmanCode HC = CreateHuffmanCode(HT, n);
    int i;
    for (i = 1; i <= n; ++i)
    {
        // printf("Character %d Huffman Code: %s\n", i, HC[i]);
        // 把上面那个printf改成中文的
        printf("字符 %d 的哈夫曼编码: %s\n", i, HC[i]);
        free(HC[i]);
    }

    free(HC);
    free(HT);
    printf("\n");
}

int main()
{
    int weights1[4] = {51, 9, 12, 13};
    test_case(weights1, 4);

    int weights2[6] = {5, 92, 112, 13, 16, 45};
    test_case(weights2, 6);

    int weights3[8] = {33, 17, 10, 15, 210, 25, 303, 35};
    test_case(weights3, 8);

    return 0;
}
