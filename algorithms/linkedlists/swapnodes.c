#include<stdio.h>
#include<stdlib.h>

/*Swap Kth node from beginning with Kth node from end in a Linked List*/

struct Node
{
	int data;
	struct Node *next;
};

void printList(struct Node *n);
void addANodeEnd(struct Node *head,int new_data);
int getLengthOfTheList(struct Node *head);
struct Node* nthPositionNode(struct Node* head, int nthPosition);
void swapKthPositionNodes(struct Node* head, int kthPosition);


int main()
{
	struct Node* head = (struct Node*)malloc(sizeof(struct Node));
	head->next = NULL;
	head->data = 1;
	int lengthOfList;
	
	addANodeEnd(head,2);
	addANodeEnd(head,3);
	addANodeEnd(head,4);
	addANodeEnd(head,5);
	addANodeEnd(head,6);
	addANodeEnd(head,7);
	addANodeEnd(head,8);
	addANodeEnd(head,9);
	
	printList(head);
	swapKthPositionNodes(head,5);
	printList(head);
	//printf("Length of List: %d\n",getLengthOfTheList(head));
	return 0;
}

void addANodeEnd(struct Node *head,int new_data)
{
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = new_data;
	while((head->next) != NULL)
	{
		head = head->next;
	}
	head->next = newNode;
	newNode->next = NULL;

}

struct BinaryNode{
	struct Node *node1;
	struct Node *node2;
};

struct BinaryNode* nthPositionNodes(struct Node* head, int kthPosition,int lengthOfList);

struct BinaryNode* nthPositionNodes(struct Node* head, int kthPosition,int lengthOfList)
{
	int currentPosition = 1;
	struct BinaryNode* myBinaryNode = (struct BinaryNode*)malloc(sizeof(struct BinaryNode));
	while (currentPosition != kthPosition)
	{
		head = head-> next;
		currentPosition++;
	}
	
	myBinaryNode->node1 = head;
	
	//printf("Value of head at kfrom beginning:%d\n",(myBinaryNode->node1)->data);
	//printf("length of kth position from end:%d\n",lengthOfList-kthPosition);
	while(currentPosition != (lengthOfList-kthPosition+1))
	{
		//printf("Entered while loop\n");
		head = head->next;
		currentPosition++;
	}
	//printf("here too\n");
	myBinaryNode->node2 = head;
	//printf("Value of head at k from end:%d\n",(myBinaryNode->node2)->data);
	return myBinaryNode;
}

void swapKthPositionNodes(struct Node* head, int kthPosition)
{
	int lengthOfList = getLengthOfTheList(head);
	printf("Length of list:%d\n",lengthOfList);
	struct Node* k_beginning;
	struct Node* k_end;
	int k_temp_data;
	
	struct BinaryNode* M = (struct BinaryNode*)malloc(sizeof(struct BinaryNode)); ;
	M = nthPositionNodes(head,kthPosition,lengthOfList);
	k_beginning = M-> node1;
	k_end = M->node2;
	
	/*k_beginning = nthPositionNode(head,kthPosition - 1);
	k_end = nthPositionNode(head,(lengthOfList-kthPosition));*/
	k_temp_data = k_beginning->data;
	k_beginning->data = k_end->data;
	k_end->data = k_temp_data;
	
}

struct Node* nthPositionNode(struct Node* head, int nthPosition)
{
	int currentPosition = 0;
	while (currentPosition != nthPosition)
	{
		head = head-> next;
		currentPosition++;
	}
	return head;
}

int getLengthOfTheList(struct Node *head)
{
	int lengthOfList = 0;
	//head->data = 24;
	while(head!=NULL)
	{
		lengthOfList++;
		head = head->next;
	}
	return lengthOfList;
}
void printList(struct Node *n)
{
	while(n!=NULL)
	{
		printf("%d\n",n->data);
		n= n->next;
	}
}



