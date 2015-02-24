//intended for use on 32 bit little endian systems

//Yes, this *is* the source code for the program
//you're interacting with.

#include <stdio.h>

typedef struct
{
const char *fname;
const unsigned int authlevel;
}FENTRY;

#define NUM_FENTRY 2

const FENTRY flist[]={
    {"main.c",3},
    {"flag.txt",126}
    };


void printfile(const char* fname)
{
    FILE *file=fopen(fname,"rt");
    char c;
    while( !feof(file) && (c=fgetc(file))!=EOF ) putchar(c);
    fclose(file);
}

int main(void)
{
    unsigned int authlevel=5;
    char name[32];
    int i;
    int choice;

    printf("Welcome to remote file viewing, guest access mode.\n");
    printf("What is your name? ");
    fgets(name,34,stdin);
    printf("Your authorization level is %03d.\n",authlevel);

    for(;;)
    {
        printf("0: exit\n");
        for(i=0;i<NUM_FENTRY;++i)
            printf("%d: Level %03d: view \"%s\"\n",i+1,
                flist[i].authlevel,flist[i].fname);
        
        if(scanf("%d",&choice)!=1)
        {
            scanf("%*[^\n]%1*[\n]");
            continue;
        }
        
        if(choice==0) return 0;

        if(choice>NUM_FENTRY)
        {
            printf("Invalid choice\n");
            continue;
        }

        if(authlevel>=flist[choice-1].authlevel)
            printfile(flist[choice-1].fname);
        else printf("Error: Authorization level of %03d+ required.  "
            "Your level is %03d.\n",flist[choice-1].authlevel,
            authlevel);

    }

    return 0;
}
