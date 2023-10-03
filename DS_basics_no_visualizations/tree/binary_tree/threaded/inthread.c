#include <stdio.h>
#include <stdlib.h>

// 定义线索二叉树的结构
typedef struct ThreadNode
{
    char data;                          // 数据域
    struct ThreadNode *lchild, *rchild; // 左、右子树指针
    int ltag, rtag;                     // 左、右线索标志
} ThreadNode, *ThreadTree;

// 中序线索化函数
void InThreaded(ThreadNode *p, ThreadNode **pre)
 // pre是指向前驱节点的指针，**说明pre是指针的指针，不太好理解，举个例子，假设pre指向节点B，那么*pre就是节点B
{
    if (p != NULL)
    {
        InThreaded(p->lchild, pre); // 递归处理左子树

        // 如果左子树为空，建立前驱线索
        if (p->lchild == NULL)
        {
            p->lchild = *pre; // *pre是前驱节点
            p->ltag = 1;
            printf("节点 %c 的左子树为空，前驱是 %c\n", p->data, *pre ? (*pre)->data : ' ');
        }

        // 如果右子树为空，并且前一个节点不为空，则建立后继线索
        if (p->rchild == NULL && *pre != NULL)
        {
            (*pre)->rchild = p;
            (*pre)->rtag = 1;
            printf("节点 %c 的右子树为空，后继是 %c\n", (*pre)->data, p->data);
        }

        *pre = p;                   // 更新pre为当前节点
        InThreaded(p->rchild, pre); // 递归处理右子树
    }
}

// 初始化中序线索化二叉树
void createInThread(ThreadTree T)
{
    ThreadNode *pre = NULL; // 初始化pre
    InThreaded(T, &pre);    // 开始线索化
    pre->rchild = NULL;     // 最后一个节点的右子树为空
    pre->rtag = 1;
}

// 创建新的节点
ThreadNode *newNode(char data)
{
    ThreadNode *node = (ThreadNode *)malloc(sizeof(ThreadNode));
    node->data = data;
    node->lchild = node->rchild = NULL;
    node->ltag = node->rtag = 0;
    return node;
}

// 中序遍历线索二叉树
void inOrder(ThreadTree T)
{
    ThreadTree p = T;
    // 找到最左边的节点
    while (p && p->ltag == 0)
        p = p->lchild;

    while (p != NULL)
    {
        printf("%c ", p->data);

        // 如果右子树是线索，直接访问后继节点
        if (p->rtag == 1)
        {
            p = p->rchild;
        }
        else
        {
            // Otherwise, move to the leftmost node of the right subtree
            p = p->rchild;
            while (p && p->ltag == 0)
                p = p->lchild;
        }
    }
}

int main()
{
    // 创建一个简单的二叉树
    ThreadTree root = newNode('A');
    root->lchild = newNode('B');
    root->rchild = newNode('C');
    root->lchild->lchild = newNode('D');
    root->lchild->rchild = newNode('E');
    root->rchild->rchild = newNode('F');

    printf("开始线索化二叉树...\n");
    createInThread(root);
    printf("线索化完成!\n");

    printf("中序遍历线索二叉树:\n");
    inOrder(root);
    printf("\n");

    return 0;
}
