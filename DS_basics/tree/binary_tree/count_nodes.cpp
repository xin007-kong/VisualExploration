#include <iostream>
using namespace std;

struct Node {
    int value;
    Node *left;
    Node *right;
    Node(int val) : value(val), left(NULL), right(NULL) {}
};

int NodeCount(Node *T, Node *parent = NULL, string direction = "") {
    if (T == NULL) {
        if (parent != NULL) {
            cout << "count_nodes(NULL)开始递归，此为节点" << parent->value << "的" << direction << "子树" << endl;
        } else {
            cout << "count_nodes(NULL)开始递归" << endl;
        }
        cout << "--------------------------------------------------" << endl;
        cout << "count_nodes(NULL)结束，返回值为：0" << endl;
        cout << "--------------------------------------------------" << endl;
        return 0;
    } else {
        if (parent != NULL) {
            cout << "从节点" << parent->value << "进入其" << direction << "子节点" << T->value << endl;
        }
        cout << "count_nodes(" << T->value << ")开始递归" << endl;
        int left_count = NodeCount(T->left, T, "左");
        int right_count = NodeCount(T->right, T, "右");
        int result = left_count + right_count + 1;
        cout << "--------------------------------------------------" << endl;
        cout << "节点" << T->value << "的左子树节点总数为：" << left_count << endl;
        cout << "节点" << T->value << "的右子树节点总数为：" << right_count << endl;
        cout << "加上节点" << T->value << "本身，所以节点" << T->value << "的节点总数为：" << result << endl;
        cout << "count_nodes(" << T->value << ")结束，返回值为：" << result << endl;
        if (parent != NULL) {
            cout << "从节点" << T->value << "返回节点" << parent->value << "，继续调用count_nodes" << endl;
        }
        cout << "--------------------------------------------------" << endl;
        return result;
    }
}

int main() {
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->left->left->left = new Node(6);

    cout << "计算二叉树节点总数：" << endl;
    cout << "--------------------------------------------------" << endl;
    int count = NodeCount(root);
    cout << "--------------------------------------------------" << endl;
    cout << "二叉树的节点总数为：" << count << endl;

    return 0;
}