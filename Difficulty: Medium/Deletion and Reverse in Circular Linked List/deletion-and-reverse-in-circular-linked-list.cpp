//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Structure for the linked list node
struct Node {
    int data;
    struct Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

// Function to print nodes in a given circular linked list
void printList(struct Node *head) {
    if (head != NULL) {
        struct Node *temp = head;
        do {
            cout << temp->data << " ";
            temp = temp->next;
        } while (temp != head);
    } else {
        cout << "empty" << endl;
    }
    cout << endl;
}


// } Driver Code Ends
class Solution {
  public:
    // Function to reverse a circular linked list
    Node* reverse(Node* head) {
        // code here
        Node* prev_node=NULL;
        Node* cur_node=head;
        Node* next_node=NULL;
        while(cur_node!=NULL){
            next_node=cur_node->next;
            cur_node->next=prev_node;
            prev_node=cur_node;
            cur_node=next_node;
        }
        return prev_node->next;
    }

    // Function to delete a node from the circular linked list
    Node* deleteNode(Node* head, int key) {
    if (!head) return nullptr;  // If list is empty

    // If the head node itself holds the key to be deleted
    if (head->data == key) {
        Node *temp = head;

        // If there's only one node in the circular list
        if (head->next == head) {
            delete head;
            return nullptr;
        }

        // Find the last node to fix the circular reference
        while (temp->next != head) {
            temp = temp->next;
        }

        // Point last node's next to the second node
        temp->next = head->next;
        Node *toDelete = head;
        head = head->next;  // Update the head
        delete toDelete;    // Delete the old head

        return head;
    }

    // If the node to be deleted is not the head node
    Node *curr = head;
    Node *prev = nullptr;
    do {
        // Find the node to delete
        if (curr->data == key) {
            prev->next = curr->next;  // Remove the node
            delete curr;              // Free memory
            return head;
        }
        prev = curr;
        curr = curr->next;
    } while (curr != head);

    return head;  // If the key was not found
}

};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;

        // Reading input into a vector
        while (ss >> number) {
            arr.push_back(number);
        }

        int key;
        cin >> key;
        cin.ignore();

        // Creating the circular linked list
        struct Node *head = new Node(arr[0]);
        struct Node *tail = head;
        for (int i = 1; i < arr.size(); ++i) {
            tail->next = new Node(arr[i]);
            tail = tail->next;
        }
        tail->next = head; // Make the list circular

        Solution ob;

        // Delete the node with the given key
        head = ob.deleteNode(head, key);

        // Reverse the circular linked list
        head = ob.reverse(head);

        // Print the modified list
        printList(head);
    }
    return 0;
}

// } Driver Code Ends