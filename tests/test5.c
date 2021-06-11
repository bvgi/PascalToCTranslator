#include <stdio.h> 
 

int main(void){
int numperline;
int maxnum;
int base;
int number;
int linecount;
numperline = 5;
maxnum = 20000;
base = 2;
printf("Powers of ", base, ", 1 <= x <= ", maxnum, ':');
number = 1;
linecount = 0;
while(number <= maxnum) {
linecount = linecount + 1;
if(linecount > 1){
printf(", ");
}
printf(number);
if((linecount == numperline) && !(number * 2 > maxnum)){
printf(",\n");
linecount = 0;
}
number = number * base;
}
printf("\n");
return 0; 
}