/* author: James Lyons
Aug 2012
this code is from http://www.practicalcryptography.com/cryptanalysis/breaking-machine-ciphers/cryptanalysis-enigma/
*/
#include "NBestList.h"
#include <stdlib.h>
#include <stdio.h>

NBestList *newListElem(EnigmaKey *key, float score){
    NBestList *ret = malloc(sizeof(NBestList));
    ret->score = score;
    ret->next = NULL;
    ret->prev = NULL;
    ret->key = *key;
    return ret;
}

NBestList *nbest_add(NBestList *base,EnigmaKey *key, float score){
    NBestList *elem = newListElem(key,score);
    NBestList *current;
    int i,added = FALSE;
    if(base==NULL){ 
        base = elem;
        return base;
    }
    current = base;
    i = 0;
    while(current != NULL){
        //printf("@ %d, %f\n",i,current->score);
        if((score < current->score) && (added==FALSE)){
            if(current == base){
                base->prev = elem;
                elem->next = base;
                base = elem;
            }else{
                elem->prev = current->prev;
                elem->prev->next = elem;
                elem->next = current; 
                current->prev = elem;            
            }
            added = TRUE;
        }
        if(i >= MAXLEN){
            if(!added) free(elem);
            else{ 
                current->prev->next = NULL;
                freeList(current);
            }
            break;
        }
        i++;
        if((current->next == NULL) && (added==FALSE)){
            current->next = elem;
            elem->prev = current;
            break;
        }
        current = current->next;
    }
    return base;
}

/*************************************************
free a NBestList list, given an element, it frees the current element
and everything that follows it.
*************************************************/
void freeList(NBestList *base){
    NBestList *current = base;
    int i = 0;
    while(current->next != NULL){
        current = current->next;
        free(current->prev);
    }
    free(current);
}


/*************************************************
prints a NBestList list, useful for debugging
*************************************************/
void printList(NBestList *base){
    NBestList *current = base;
    int i = 0;
    while(current != NULL){
        printf("> %d, %f\n",i++,current->score);
        current = current->next;
    }
}
