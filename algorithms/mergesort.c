#include<stdio.h>
#if !defined(ARRAY_SIZE)
	#define ARRAY_SIZE(x) (sizeof(x)) / sizeof((x)[0])
#endif
int *mergeSort(int *,int);
//void mergeSort(int *,int);


int main()
{
	int A = (int *)malloc(8*sizeof(int));
	A = {5,4,1,8,7,2,6,3};
	int len_A = ARRAY_SIZE(A);
	int *b;
	int i;
	b = mergeSort(A,len_A);
	/*B = mergeSort(A);
	len_B = sizeof(B)/sizeof(int);*/
	for(i=0;i<8;i++)
	{
		printf("%d\n",*(b+i));
	}
	return 0;
}


int *mergeSort(int *A,int len_A)
{
	int i = 0,size = 0;
	printf("%d\n",len_A);
	if (len_A == 1)
	{
		return A;
	}
	else
	{
		int B[len_A];
		int A1[(int)len_A/2];
		int A2[(int)len_A/2];
		int i;
		//printf("%d\n",(int)len_A/2 );
		for(i = 0;i<(int)len_A/2;i++)
		{
			A1[i] = A[i];
			A2[i] = A[i + (int)len_A/2];
		}
		i = 0;
		int j = 0,k = 0;
		int mergeSize = len_A;
		for(k = 0;k<mergeSize;k++)
		{
			if (i<(int)len_A/2 && j < (int)len_A/2)
			{
				if (A1[i] < A2[j])
				{
					B[k] = A1[i];
					i++;
				}
				else
				{
					B[k] = A2[j];
					j++;
				}
			}
			else if (i >= (int)len_A/2)
			{
				B[k] = A2[j];
				j++;
			}
			else
			{
				B[k] = A1[i];
				i++;
			}
		}
		return B;
	}
}
