/*

下面的例子树是：
         1
        / \
       2   3
      / \
     4   5
    /
   6

*/
#include <iostream>
using namespace std;

struct Node
{
    int value;
    Node *left;
    Node *right;
    Node(int val) : value(val), left(NULL), right(NULL) {}
};

int maxDepth(Node *root, Node *parent = NULL, string direction = "root")
{
    if (root == NULL)
    {
        cout << "========================================" << endl;
        if (parent)
            cout << "maxDepth(NULL)开始递归，此为节点" << parent->value << "的" << direction << "子树" << endl;
        else
            cout << "maxDepth(NULL)开始递归" << endl;
        cout << "maxDepth(NULL)结束，返回值为：0" << endl;
        cout << "========================================" << endl;
        return 0;
    }
    cout << "========================================" << endl;
    if (parent)
        cout << "从节点" << parent->value << "进入其" << direction << "子节点" << root->value << endl;
    cout << "maxDepth(" << root->value << ")开始递归" << endl;
    cout << "----------------------------------------" << endl;
    int leftDepth = maxDepth(root->left, root, "左");
    int rightDepth = maxDepth(root->right, root, "右");
    cout << "节点" << root->value << "的左子树深度为：" << leftDepth << endl;
    cout << "节点" << root->value << "的右子树深度为：" << rightDepth << endl;
    int result = max(leftDepth, rightDepth) + 1;
    cout << "取其最大值，所以节点" << root->value << "的深度为：" << result << endl;
    cout << "maxDepth(" << root->value << ")结束，返回值为：" << result << endl;
    if (parent)
        cout << "此时从节点" << root->value << "返回节点" << parent->value << "，继续调用maxDepth" << endl;
    cout << "========================================" << endl;
    return result;
}

int main()
{
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->left->left->left = new Node(6);

    cout << "计算二叉树深度：" << endl;
    cout << "二叉树的深度为：" << maxDepth(root) << endl;

    delete root->left->left->left;
    delete root->left->right;
    delete root->left->left;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
