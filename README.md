#include<stdio.h> 
void sort(int ary[],int n)
{ 
	int i,j,temp; 
	for(i=0;i<n;i++) 
	{ 
		for(j=0;j<n;j++)
		 { 
			if(ary[i]<ary[j]) 
			{ 
				temp=ary[i]; 
				ary[i]=ary[j]; 
				ary[j]=temp;
			 }
		 } 
	} 
} 
void displayarray(int ary[],int n) 
{ 
	int i; 
	for(i=0;i<n;i++) 
	{ 
		printf("%d ",ary[i]); 
	}
 } 
int main() 
{ 
int ary1[100],ary2[100],arym[200],i,j,n1,n2,m;
 printf("Enter number of elements of first array :"); 
scanf("%d",&n1);
printf("\nEnter %d elements of first array :\n",n1);
for(i=0;i<n1;i++) 
{ 	
	scanf("%d",&ary1[i]); 
} 
printf("Enter number of elements of second array :");
scanf("%d",&n2); 
printf("\nEnter %d elements of second array :\n",n2); 
for(i=0;i<n2;i++) 
{ 
	scanf("%d",&ary2[i]); 
} 
printf("\n First array before sort :\n"); 
displayarray(ary1,n1); 
sort(ary1,n1);
printf("\n First array after sort :\n"); 
displayarray(ary1,n1); 
printf("\n Second array before sort :\n"); 
displayarray(ary2,n2); 
sort(ary2,n2);
printf("\n Second array after sort :\n"); 
displayarray(ary2,n2);
 m=n1+n2; 
for(i=0;i<n1;i++) 
arym[i]=ary1[i]; 
for(i=0;i<n2;i++)
arym[n1+i]=ary2[i]; 
printf("\n Merged array before sort :\n");
displayarray(arym,m);
printf("\n Merged array after sort :\n");
sort(arym,m);
 displayarray(arym,m); 
return(0); 
}