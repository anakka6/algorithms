#include<stdio.h>
#include<stdlib.h>

/* Remove every kth node of the linked list*/

struct Node
{
	int data;
	struct Node * next;
};

void printList(struct Node *n);
void addANodeEnd(struct Node *head,int new_data);
void removeEveryKthNode(struct Node* head, int k);
int main()
{
	struct Node * head = (struct Node*)malloc(sizeof(struct Node));
	head-> next = NULL;
	head-> data = 0;
	
	addANodeEnd(head,1);
	addANodeEnd(head,2);
	addANodeEnd(head,3);
	addANodeEnd(head,4);
	addANodeEnd(head,5);
	addANodeEnd(head,6);
	addANodeEnd(head,7);
	addANodeEnd(head,8);
	
	printList(head);
	removeEveryKthNode(head,2);
	printf("After removing\n");
	printList(head);
	
}

void removeEveryKthNode(struct Node* head, int k)
{
	int currentPosition = 1;
	struct Node* k_1;
	struct Node* n;
	while(head->next != NULL)
	{
		if ((currentPosition%(k-1)) == 0)
		{
			k_1 = head;
			head = head->next;
			n = head;
			//temp_k = head;
			k_1->next = head->next;
			//printf("Before freeing head:%d\n",head->data);
			//printList(head);
			free(n);
			//printf("After freeing head:%d\n",head->data);
			//printList(head);
		}
		currentPosition++;
		head = head->next;
	}
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

int getLengthOfTheList(struct Node *head)
{
	int lengthOfList = 0;
	//head->data = 24;
	while(head!=NULL)
	{
		lengthOfList++;
		head = head->next;
		//printf("in addANodeEnd, head=%d\n",head->data);
		
	}
	
	//head->data = 24;
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