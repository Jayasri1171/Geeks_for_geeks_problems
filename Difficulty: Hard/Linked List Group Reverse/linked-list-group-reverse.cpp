/*
  Node is defined as
    struct node
    {
        int data;
        struct Node* next;

        Node(int x){
            data = x;
            next = NULL;
        }

    }*head;
*/

class Solution {
  public:
    Node *reverseKGroup(Node *head, int k) {
        // code here
        int count=1;
        Node * ans =NULL;
        Node * cur= head;
        Node * mainans=ans;
        while(cur){
            Node * prev=NULL;
            Node * nex=NULL;
            while(count<=k and cur){
                nex=cur->next;
                cur->next=prev;
                prev=cur;
                cur=nex;
                count+=1;
            }
            count=1;
            
            if (ans== NULL){
                ans=prev;
                mainans=prev;
            }
            else{
                ans->next=prev;
            }
            while(ans->next){
                ans=ans->next;
            }
            
            
        }
        return mainans;
    }
};

