#include <stdio.h>
#include <stdlib.h>
#include "main.h"
char choice[0];

int main(int argc, char* argv[]){
	printf("1. Minecraft Launcher\n");
	printf("2. MultiMC5\n");
	printf("3. mcpelauncher\n");
	printf("> ");
	scanf ("%s",choice);
	printf("You have chosen %s",choice);
}