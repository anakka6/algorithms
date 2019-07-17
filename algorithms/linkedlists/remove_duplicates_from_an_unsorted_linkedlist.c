#include<stdio.h>
#include<stdlib.h>

/* Remove duplicates from an unsorted linked list*/

struct Node
{
	int data;
	struct Node * next;
};

void printList(struct Node *n);
void addANodeEnd(struct Node *head,int new_data);