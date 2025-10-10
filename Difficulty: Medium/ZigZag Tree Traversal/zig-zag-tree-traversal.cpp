/*
class Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
    vector<int> zigZagTraversal(Node* root) {
        // code here
        Node* temp=root;
        queue<Node*>q;
        vector<vector<int>>main;
        q.push(temp);
        while(!q.empty()){
            vector<int>dummy;
            int s = q.size();
            for(int i=0;i<s;i++){
                dummy.push_back(q.front()->data);
                if(q.front()->left) q.push(q.front()->left);
                if(q.front()->right) q.push(q.front()->right);
                q.pop();
            }
            main.push_back(dummy);
        }
        
        vector<int>ans;
        for(int i=0;i<main.size();i++){
            vector<int>z=main[i];
            if(i%2==0){
               ans.insert(ans.end(), z.begin(), z.end());
            }
            else{
                reverse(z.begin(),z.end());
                ans.insert(ans.end(), z.begin(), z.end());
            }
            
            
            
        }
        return ans;
    }
};