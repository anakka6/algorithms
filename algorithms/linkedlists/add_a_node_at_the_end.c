#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	struct Node *next; //A pointer which is of type struct and the name of the struct is Node
};

//Program to create a simple linked list with 3 nodes



void printList(struct Node *n);
void addANode(struct Node **n, int);
void insertAfter(struct Node *n, int);
void addANodeEnd(struct Node *n,int new_data);

int main()
{
	struct Node* head = NULL;
	struct Node* second = NULL;
	struct Node* third = NULL;

	//allocate 3 nodes in the heap..interesting!
	head = (struct Node*)malloc(sizeof(struct Node));
	second = (struct Node*)malloc(sizeof(struct Node));
	third = (struct Node*)malloc(sizeof(struct Node));

	head->data =1;
	head->next = second;

	second->data = 2;
	second->next = third;

	third->data =3;
	third->next = NULL;
	int new_data = 0;
	struct Node **head_ref = (&head);
	printList(head);
	//addANode(head_ref,new_data);
	//insertAfter(second,new_data);
	addANodeEnd(head,4);
	printf("after adding a node\n");
	printList(head);
	
	return 0;
}

void addANodeEnd(struct Node *n,int new_data)
{
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = new_data;
	while((n->next) != NULL)
	{
		n = n->next;
	}
	newNode->next = NULL;
	n->next = newNode;

}

void insertAfter(struct Node *n, int new_data)
{
	if(n == NULL)
	{
		printf("Check the previous node is pointing to NULL\n");
	}
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = new_data;
	newNode->next = n->next;
	n->next = newNode;
}
void printList(struct Node *n)
{
	while(n!= NULL)
	{
		printf("%d\n",n->data);
		n = n->next;
	}
}
	
void addANode(struct Node **head_ref,int new_data)
{
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	
	newNode->data = new_data;
	newNode->next = (*head_ref);
	(*head_ref) = newNode;
		
}

