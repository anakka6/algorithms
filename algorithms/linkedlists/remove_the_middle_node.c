#include<stdio.h>
#include<stdlib.h>

/* Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked
list, given only access to that node.
EXAMPLE:
Input: the node c from the linked list a->b->c->d->e->f
Output: nothign is returned, new list a->b->d->e->f */

struct Node{
	int data;
	struct Node * next;
};

void printList(struct Node *n);
void addANodeEnd(struct Node *head,int new_data);
void removeMiddleNode(struct Node* n);

int main()
{
	struct Node * head = (struct Node*)malloc(sizeof(struct Node));
	struct Node * second = (struct Node*)malloc(sizeof(struct Node));
	struct Node * third = (struct Node*)malloc(sizeof(struct Node));
	struct Node * forth = (struct Node*)malloc(sizeof(struct Node));
	struct Node * fifth = (struct Node*)malloc(sizeof(struct Node));
	head-> next = second;
	head-> data = 1;
	
	second-> next = third;
	second-> data = 2;
	third-> next = forth;
	third-> data = 3;
	forth-> next = fifth;
	forth-> data = 4;
	fifth-> next = NULL;
	fifth-> data = 5;
	
	printList(head);
	removeMiddleNode(third);
	printf("After removing\n");
	printList(head);
	
}


void removeMiddleNode(struct Node* n)
{
	if (n!=NULL && n->next != NULL)
	{
		struct Node* k;
		k = n->next;
		n->next = k->next;
		free(k);
		
	}
}
void printList(struct Node *n)
{
	while(n!= NULL)
	{
		printf("%d\n",n->data);
		n = n->next;
	}
}
	