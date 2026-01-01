/*
class Node {
public:
    int data;
    Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};
*/

class Solution {
  public:
    Node* intersectPoint(Node* head1, Node* head2) {
        //  Code Here
        Node* temp1=head1;
    Node* temp2=head2;
    int c1=0,c2=0;
    while(temp1!=NULL){
        c1+=1;
        temp1=temp1->next;
    }
    while(temp2!=NULL){
        c2+=1;
        temp2=temp2->next;
    }
    temp1=head1;
    temp2=head2;
    if(c1>c2){
        int s=c1-c2;
        while(s!=0){
          temp1=temp1->next;
          s-=1;
        }
    }
    else if(c1==c2){
        temp1=head1;
        temp2=head2;
    }
    else{
        int s=c2-c1;
        while(s!=0){
            temp2=temp2->next;
            s-=1;
        }
    }
    while(temp1!=NULL){
        if(temp1==temp2){
            return temp1;
        }
        temp1=temp1->next;
        temp2=temp2->next;
    }
    return temp1;
        
    }
};