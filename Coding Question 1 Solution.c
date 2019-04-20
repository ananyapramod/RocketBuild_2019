#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct
{
	char *key;
	char *value;
}HashMap;
HashMap LinkedList[100000];

void addData()
{
	int i=0,k=0;
	int n;
	char key[100];
	char value[100];

	printf("Enter number of k,v pairs : ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("Enter key : \n");
		scanf("%s",&key);
		printf("Enter value : \n");
		scanf("%s",&value);
		if(i==0)
		{
			LinkedList[i].key=key;
			LinkedList[i].value=value;
		}
		else
		{
			if(KeyPresent(key,n)==0)
			{
				k++;
				LinkedList[k].key=key;
				LinkedList[k].value=value;
			}
		}
	}
	printData(n);
}
int KeyPresent(char k[100],int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(strcmp(k,LinkedList[i].key)==0)
			return 1;
	}
	return 0;
}
void printData(int n)
{
	int i=0;
	for(i=0;i<n;i++)
	{
		printf("%s %s\n",LinkedList[i].key,LinkedList[i].value);
	}
}
int main()
{
	addData();
	return 0;
}