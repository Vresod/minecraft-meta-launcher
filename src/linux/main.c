#include <stdio.h>
#include <stdlib.h>
#include "main.h"
int choice;

int main(int argc, char* argv[]){
	printf("1. Minecraft Launcher\n");
	printf("2. MultiMC5\n");
	printf("3. mcpelauncher\n");
	printf("> ");
	scanf("%d",choice);
	printf("You have chosen %d.",choice);
}