#include <stdio.h> 
 

int main(void){
int fibonacci1;
int fibonacci2;
int temp;
int count;
printf("First ten Fibonacci numbers are: \n");
count = 0;
fibonacci1 = 0;
fibonacci2 = 1;
do { 
printf(fibonacci2 / 7);
temp = fibonacci2;
fibonacci2 = fibonacci1 + fibonacci2;
fibonacci1 = temp;
count = count + 1;
} while(!(count == 10));
printf("\n");
return 0; 
}