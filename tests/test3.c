#include <stdio.h> 
 
char* summation(int num, float real1, int bool1, char *str){
char *summation;
if(num == 1){
summation = "Hello";
} else {
summation = "World";
}
return summation;
}


int main(void){
float a;
int b;
int c;
a = 22.5f;
a = a + summation(10);
b = 1;
c = 0;
return 0; 
}