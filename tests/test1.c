#include <stdio.h> 
 
void foo(){
int i;
i = 1;
}


int main(void){
int i;
while(i == 1) {
printf(i);
}
do { 
printf(i);
i = i + 1;
} while(i == 0);
for(i = 0;  i <= 2 ; i++){ 
if(i == 1){
i = 0;
} else {
i = 1;
}
}
return 0; 
}