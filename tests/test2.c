#include <stdio.h> 
 
void scopeinner(){
int ten;
ten = 10;
printf(ten);
if(ten == 10){
ten = 1;
}
}

int summation(int num){
int summation;
if(num == 1){
summation = 1;
} else {
summation = 2;
}
return summation;
}


int main(void){
int a;
a = 20;
printf(a + 1 * 2);
scopeinner();
a = a + summation(10);
printf(a);
return 0; 
}