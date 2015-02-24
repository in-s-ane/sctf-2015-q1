//intended for use on 32 bit little endian systems

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <signal.h>

void printfile(const char* fname)
{
    FILE *file=fopen(fname,"rt");
    char c;
    while( !feof(file) && (c=fgetc(file))!=EOF ) putchar(c);
    fclose(file);
}

void show_soln(void)
    {
    printfile("flag.txt");
    fflush(stdout);
    }

void test(void)
{
    char name[32];
    

    printf("What is your name? ");
    fgets(name,256,stdin);
    
    srand(time(NULL));

    if( (rand()%100)==(rand()%100) )
    {
        printf("You have good luck, but it still won't be that easy.\n");
        //show_soln();
    }
    else
    {
        printf("You have bad luck.\n");
    }
}

//This function will run when the program segfaults.
//This is a workaround for a "feature" of the wrapper program
//making this a network service.
void handle_segfault(int snum)
{
    printf("segmentation fault\n");
    exit(0);
}

int main(void)
{
    //use a custom handler for any segfaults that occur
    signal(SIGSEGV,handle_segfault);
    
    printf("Let's play a little game of luck!\n");
    test();
    printf("Goodbye.\n");
    return 0;
}

