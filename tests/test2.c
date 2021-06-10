#include <stdio.h> 
 
void scopeinner(){
int a;
a = 10;
writeln(a);
if(num == 1){
summation = 1;
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
writeln(a + 1 * 2);
scopeinner();
a = a + summation(10);
writeln(a);
writeln(a);
return 0; 
}