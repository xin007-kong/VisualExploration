#include <stdio.h>
#include <stdlib.h>

// 定义二叉树节点结构
struct TreeNode
{
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

// 创建一个新的二叉树节点
struct TreeNode *createNode(int data)
{
    struct TreeNode *newNode = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// 计算二叉树节点个数的递归函数
int countNodes(struct TreeNode *root)
{
    if (root == NULL)
    {
        printf("countNodes(NULL)开始递归\n");
        printf("countNodes(NULL)结束，返回值为：0\n");
        return 0;
    }
    printf("countNodes(%d)开始递归\n", root->data);
    int left_count = countNodes(root->left);
    int right_count = countNodes(root->right);
    int result = 1 + left_count + right_count;
    printf("节点%d的左子树节点总数为：%d\n", root->data, left_count);
    printf("节点%d的右子树节点总数为：%d\n", root->data, right_count);
    printf("加上节点%d本身，所以节点%d的节点总数为：%d\n", root->data, root->data, result);
    printf("countNodes(%d)结束，返回值为：%d\n", root->data, result);
    return result;
}

int main()
{
    // 创建一个二叉树
    struct TreeNode *root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->left->left->left = createNode(6);

    // 计算二叉树节点个数
    printf("计算二叉树节点个数：\n");
    printf("--------------------------------------------------\n");
    int count = countNodes(root);
    printf("--------------------------------------------------\n");
    printf("二叉树的节点总数为：%d\n", count);

    return 0;
}