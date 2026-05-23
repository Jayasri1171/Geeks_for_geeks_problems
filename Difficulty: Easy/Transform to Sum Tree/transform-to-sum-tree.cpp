/* Structure for Tree Node
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = nullptr;
        right = nullptr;
    }
};
*/

class Solution {
  public:
    int sri(Node *root){
        if(!root) return 0;
        int v = root->data;
        int l = sri(root->left);
        int r = sri(root->right);
        
        root->data = l+r;
        return l+r+v;
    }
    void toSumTree(Node *root) {
        // code here
        sri(root);
        
    }
};