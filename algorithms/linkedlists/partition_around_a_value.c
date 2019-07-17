#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node * next;
};

void printList(struct Node *n);
void addANodeEnd(struct Node *head,int new_data);
void partitionList(struct Node* head, int value);

int main()
{
	struct Node * head = (struct Node*)malloc(sizeof(struct Node));
	head-> next = NULL;
	head-> data = 3;
	
	addANodeEnd(head,5);
	addANodeEnd(head,8);
	addANodeEnd(head,5);
	addANodeEnd(head,10);
	addANodeEnd(head,2);
	addANodeEnd(head,1);
	//addANodeEnd(head,4);
	//addANodeEnd(head,0);
	printf("Before partitioning around 5\n");
	printList(head);
	partitionList(head,5);
	printf("After partitioning around 5\n");
	printList(head);
	
	return 0;
	
}

void partitionList(struct Node* head, int value)
{
	struct Node* p1 = head;
	struct Node* p2 = head;
	struct Node* temphead = (struct Node*)malloc(sizeof(struct Node));
	struct Node* temp1= (struct Node*)malloc(sizeof(struct Node));
	/* pl = head;
	p2 = head */;
	while(p1->next != NULL)
	{
		if(((p1->next)->data) < value && p1 != p2)
		{
			temp1 = p1->next;
			p1->next = temp1->next; //temp1 to store the node 
			temphead->data = head->data;
			temphead->next = head->next;
			head->data = temp1->data;
			head->next = temp1;
			temp1->data = temphead->data;
			temp1->next = temphead->next;
			p2 = head;
		}
		if (p1->next != NULL && ((p1->next)->data) >= value)
		{
			p1 = p1->next;
		}
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