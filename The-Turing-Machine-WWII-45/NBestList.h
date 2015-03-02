/* author: James Lyons
Aug 2012
this code is from http://www.practicalcryptography.com/cryptanalysis/breaking-machine-ciphers/cryptanalysis-enigma/
*/
#include "enigma.h"

#ifndef NBESTLISTH
#define NBESTLISTH

#define MAXLEN 1000
#define TRUE 1
#define FALSE 0

typedef struct nbest__{
    struct nbest__ *next;
    struct nbest__ *prev;
    float score;
    EnigmaKey key;
} NBestList;

NBestList *newListElem(EnigmaKey *key, float score);
NBestList *nbest_add(NBestList *base,EnigmaKey *elem, float score);
void printList(NBestList *base);
void freeList(NBestList *base);

#endif
