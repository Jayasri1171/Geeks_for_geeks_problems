/*
class Node {
  public:
    int data;
    Node *next;
    Node *prev;
    Node(int val) {
        data = val;
        next = NULL;
        prev = NULL;
    }
};

*/
class Solution {
  public:
    Node *reverse(Node *head) {
        // code here
        Node* temp=head;
        while(temp){
            // cout<<temp->data<<" ";
            Node * pretemp = temp->next;
            temp->next=temp->prev;
            temp->prev=pretemp;
            if(temp->prev == NULL){
                return temp;
            }
            temp=temp->prev;
        }
        return temp;
    }
};