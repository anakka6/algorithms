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
void addANodeEndPointer(struct Node **n,int new_data);

int main()
{
	struct Node* head = (struct Node*)malloc(sizeof(struct Node));
	struct Node **head_ref = (&head); //Not using pointer to pointer as this
	//it would be diffcult to implement the while loop when it is not pointing to NULL
	/*head->data =6;
	head->next = NULL;*/
	//printf("NULL->data: %d\n",NULL);
	addANodeEndPointer(head_ref,1);
	addANodeEndPointer(head_ref,2);
	addANodeEndPointer(head_ref,3);
	addANodeEndPointer(head_ref,4);
	printList(head);
	return 0;
}

void addANodeEndPointer(struct Node **head_ref,int new_data)
{
	/*struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = new_data;
	while(((*head_ref)->next) != NULL)
	{
		(*head_ref) = (*head_ref)->next;
	}
	(*head_ref)->next = newNode;
	newNode->next = NULL;*/
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	struct Node* lastNode = *head_ref;
	newNode->data = new_data;
	/*if(*head_ref == NULL)
	{
		*head_ref = newNode;
	}*/
	while((lastNode->next) != NULL)
	{
		lastNode = lastNode->next;
	}
	lastNode->next = newNode;
	newNode->next = NULL;

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

}


void printList(struct Node *n)
{
	while(n!= NULL)
	{
		printf("%d\n",n->data);
		n = n->next;
	}
}
	
