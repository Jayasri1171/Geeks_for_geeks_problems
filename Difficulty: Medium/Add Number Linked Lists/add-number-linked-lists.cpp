//{ Driver Code Starts
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

/* Linked list Node */
struct Node {
    int data;
    struct Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

Node* buildList() {
    vector<int> arr;
    string input;
    getline(cin, input);
    stringstream ss(input);
    int number;
    while (ss >> number) {
        arr.push_back(number);
    }
    if (arr.empty()) {
        return NULL;
    }
    int val = arr[0];
    int size = arr.size();

    Node* head = new Node(val);
    Node* tail = head;

    for (int i = 1; i < size; i++) {
        val = arr[i];
        tail->next = new Node(val);
        tail = tail->next;
    }

    return head;
}

void printList(Node* n) {
    while (n) {
        cout << n->data << " ";
        n = n->next;
    }
    cout << endl;
}


// } Driver Code Ends
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution {
  public:
    Node* addTwoLists(Node* num1, Node* num2) {
        // code here
        Node * cur1=num1;
        Node * prev1=NULL;
        Node * nex1=NULL;
        while(cur1){
            nex1=cur1->next;
            cur1->next=prev1;
            prev1=cur1;
            cur1=nex1;
        }
        Node * cur2=num2;
        Node * prev2=NULL;
        Node * nex2=NULL;
        while(cur2){
            nex2=cur2->next;
            cur2->next=prev2;
            prev2=cur2;
            cur2=nex2;
        }
        int carry=0;
        Node * dummyans=new Node(0);
        Node * tempans=dummyans;
        while(prev1!=NULL and prev2!=NULL){
            int z= prev1->data+prev2->data;
            // cout<<z<<endl;
            if (carry==1){
                z=z+1;
            }
            if(z==10){
                carry=1;
                z=0;
            }
            else if(z>10){
                carry=1;
                z=z%10;
            }
            else{
                carry=0;
            }
            // cout<<z<<endl;
            Node * qw=new Node(z);
            dummyans->next=qw;
            dummyans=dummyans->next;
            prev1=prev1->next;
            prev2=prev2->next;
        }
        if(prev1){
            while(prev1){
                int z=prev1->data;
                if(carry==1){
                    z=z+1;
                }
                if(z==10){
                    carry=1;
                    z=0;
                }
                else if(z>10){
                    carry=1;
                    z=z%10;
                }
                else{
                    carry=0;
                }
                Node * qw=new Node(z);
                dummyans->next=qw;
                dummyans=dummyans->next;
                prev1=prev1->next;
                
            }
        }
        if(prev2){
            while(prev2){
                int z=prev2->data;
                if(carry==1){
                    z=z+1;
                }
                if(z==10){
                    carry=1;
                    z=0;
                }
                else if(z>10){
                    carry=1;
                    z=z%10;
                }
                else{
                    carry=0;
                }
                Node * qw=new Node(z);
                dummyans->next=qw;
                dummyans=dummyans->next;
                prev2=prev2->next;
                
            }
        }
        
        if(carry==1){
            Node * er = new Node(1);
            dummyans->next=er;
            dummyans=dummyans->next;
        }
        
        Node * cur=tempans->next;
        Node * prev=NULL;
        Node * nex=NULL;
        while(cur){
            nex=cur->next;
            cur->next=prev;
            prev=cur;
            cur=nex;
        }
        
        
        while(prev){
            if(prev->data!=0){
                break;
            }
            else{
                prev=prev->next;
            }
        }
        
        return prev;
        
     
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To ignore the newline character after the integer input

    while (t--) {
        Node* num1 = buildList();
        Node* num2 = buildList();
        Solution ob;
        Node* res = ob.addTwoLists(num1, num2);
        printList(res);
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends