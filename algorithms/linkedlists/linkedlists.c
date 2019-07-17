#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	struct Node *next; //A pointer which is of type struct and the name of the struct is Node
};

//Program to create a simple linked list with 3 nodes



void printList(struct Node *n);
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
	
	printList(head);
	//HEAD IS NOT EQUAL TO NULL :)
	/* if(head == NULL)
	{
		printf("Indeed\n");
	}
	else{
		printf("Go nuts\n");
	} */
	return 0;
}

void printList(struct Node *n)
{
	while(n!= NULL)
	{
		printf("%d\n",n->data);
		n = n->next;
	}
}
	

