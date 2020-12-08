#include<stdio.h>
#include<stdlib.h>

void fetchweb(){
    printf("\n\n\t FETCHING THE WEB PAGE... \n\n");
    system("curl https://www.ietf.org/rfc/bcp-index.txt > op.txt");
    printf("\n\n\t FETCHED.\n");
}

int show(){
    FILE *fp;
    fp = fopen("op.txt","r");

    if (fp==NULL){
        printf("not found");
        return 0;
    }else{
        char c = getc(fp);
        while(c!=EOF){
            putchar(c);
            c = getc(fp);
        }
    }

    fclose(fp);
    return 1;
}

int main(){

    fetchweb();
    show();

    return 0;
}