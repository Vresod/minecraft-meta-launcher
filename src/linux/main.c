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
	switch(atoi(choice)) {
		case 1:
			printf("Opening minecraft-launcher...");
			minecraft_launcher();
			break;
		case 2:
			printf("Opening MultiMC5...");
			multimc();
			break;
		case 3:
			printf("Opening mcpelauncher...");
			MCPEApp();
			break;
	}
}