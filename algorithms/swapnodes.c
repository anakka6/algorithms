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
void swapKthPositionNodes(struct Node* head, int kthPosition);

int main()
{
	struct Node* head = (struct Node*)malloc(sizeof(struct Node));
	head->next = NULL;
	head->data = 0;
	
	addANodeEnd(head,1);
	addANodeEnd(head,2);
	addANodeEnd(head,3);
	addANodeEnd(head,4);
	addANodeEnd(head,5);
	addANodeEnd(head,6);
	addANodeEnd(head,8);
	addANodeEnd(head,8);
	swapKthPositionNodes(head,2);
	//printList(head);
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

void swapKthPositionNodes(struct Node* head, int kthPosition)
{
	lengthOfList = getLengthOfTheList(head);
	printf("Length of list:%d\n",lengthOfList);
}

int getLengthOfTheList(struct Node *head)
{
	lengthOfList = 0
	while(head!=NULL)
	{
		lengthOfList++;
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



