#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char **argv){
char buffer[96]={0};

printf("- %p -\\n",&buffer);

strcpy(buffer,getenv("KIRIKA"));

return 0;
}
