//////////////////////////////////////////////////////////////////////////////////
// AUTHOR:   Robert Morouney
// EMAIL:    robert@morouney.com 
// FILE:     test.c
// CREATED:  2016-11-19 03:01:15
// MODIFIED: 2016-11-19 03:35:33
//////////////////////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <time.h>
#include <Carbon/Carbon.h>

int main() {
		clock_t start, finish;
    
    start = clock();
    for (int i=0; i < 100000; i++);
    finish = clock();
    
    printf("detla = %f", (float)(finish-start)/CLOCKS_PER_SEC);

		return 0;
}
