#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	struct Node *next; //A pointer which is of type struct and the name of the struct is Node
};

//Program to create a simple linked list with 3 nodes



void printList(struct Node *n);
void addANodeEnd(struct Node *n,int new_data);

int main()
{
	struct Node* head = (struct Node*)malloc(sizeof(struct Node));
	//struct Node **head_ref = (&head); //Not using pointer to pointer as this
	//it would be diffcult to implement the while loop when it is not pointing to NULL
	head->data =0;
	head->next = NULL;
	addANodeEnd(head,1);
	printf("head1=%d\n",head->data);
	addANodeEnd(head,2);
	printf("head2=%d\n",head->data);
	addANodeEnd(head,3);
	printf("head3=%d\n",head->data);
	
	addANodeEnd(head,4);
	
	addANodeEnd(head,5);
	
	
	printList(head);
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
	//head_ref = &newNode;
	printf("in addANodeEnd, head=%d\n",head->data);
}

void printList(struct Node *n)
{
	while(n!= NULL)
	{
		printf("%d\n",n->data);
		n = n->next;
	}
}
	
