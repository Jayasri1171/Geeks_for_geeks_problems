/*
class Node {
public:
    int data;
    Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};
*/
class Solution {
  public:
    Node* mergeSort(Node* head) {
        // code here
        Node* temp=head;
        vector<int>v;
        while(temp){
            v.push_back(temp->data);
            temp=temp->next;
        }
        sort(v.begin(),v.end());
        Node* ans=new Node(v[0]);
        Node* anss=ans;
        int i=1;
        while(i<v.size()){
            Node* tmp = new Node(v[i]);
            ans->next=tmp;
            ans=ans->next;
            i+=1;
        }
        return anss;
    }
};