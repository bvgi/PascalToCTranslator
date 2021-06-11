#include <stdio.h> 
 
void foo(){
int j;
j = 1;
do { 
printf(j);
j = j + 1;
} while(!(j == 3));
}


int main(void){
int i;
int k;
foo();
i = 0;
while(i != 4) {
printf(i);
i = i + 1;
}
for(k = 0; k <= 2; k++){ 
printf("Hello");
}
for(k = 4; k >= 0; k--){ 
printf("World");

}
return 0; 
}