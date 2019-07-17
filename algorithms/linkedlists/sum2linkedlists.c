#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct Node{
	int data;
	struct Node * next;
};

void printList(struct Node *n);
void addANodeEnd(struct Node *head,int new_data);
int getNumber(struct Node* head1);

int main()
{
	struct Node * head = (struct Node*)malloc(sizeof(struct Node));
	head-> next = NULL;
	head-> data = 3;
	
	addANodeEnd(head,5);
	addANodeEnd(head,8);
	
	struct Node * head1 = (struct Node*)malloc(sizeof(struct Node));
	head1-> next = NULL;
	head1-> data = 3;
	addANodeEnd(head1,5);
	addANodeEnd(head1,2);

	printf("Printing head\n");
	printList(head);
	printf("Printing head1\n");
	printList(head1);
	
	int firstNumber = getNumber(head);
	int secondNumber = getNumber(head1);
	printf("First Number:%d\n",firstNumber);
	printf("Second Number:%d\n",secondNumber);
	printf("Summation: %d\n", firstNumber+secondNumber);
	return 0;
	
}

int getNumber(struct Node* head1)
{
	int num = 0;
	int coeff = 0;
	int digit;
	while(head1!=NULL)
	{
		digit = head1->data;
		printf("Digit:%d\n",digit);
		num = num+ (int)digit*pow(10,coeff);
		printf("Num:%d\n",num);
		coeff++;
		head1 = head1->next;
	}
	return num;
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