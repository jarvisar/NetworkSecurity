/* Vunlerable program: stack.c */
/* You can get this program from the lab’s website */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/* Changing this size will change the layout of the stack.
* Instructors can change this value each year, so students
* won’t be able to use the solutions from the past.
* Suggested value: between 0 and 400 */
#ifndef BUF_SIZE
#define BUF_SIZE 100
#endif

int bof(char *str)
{
	char buffer[BUF_SIZE];
	printf("ebp: %p\n", __builtin_frame_address(0));
	void* ret_addr = __builtin_return_address(0);
    	printf("Return address: %p\n", ret_addr);
	/* The following statement has a buffer overflow problem */
	strcpy(buffer, str); 
	printf("Buffer address: %p\n", buffer);
	return 1;
}
int main(int argc, char **argv)
{
	char str[300];
	FILE *badfile;
	/* Change the 
	size of the dummy array to randomize the parameters
	for this lab. Need to use the array at least once */
	char dummy[BUF_SIZE]; memset(dummy, 0, BUF_SIZE);
	badfile = fopen("badfile", "r");
	fread(str, sizeof(char), 300, badfile);
	int return_val = bof(str);
    	if (return_val == 1) {
     	   printf("Returned Properly!\n");
    	} else {
    	    printf("Error\n");
   	}
   	return 1;
}
