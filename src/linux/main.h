// headers
#include <stdio.h>
#include <stdlib.h>

// functions

// launch functions



void MCPEApp(){
    // curl the file
    system("curl -L https://github.com/ChristopherHX/linux-packaging-scripts/releases/download/appimage/Minecraft_Bedrock_Launcher-x86_64.0.0.510.AppImage --output MCPE.AppImage");
    // run the file
    system("MCPE.AppImage");
}

void multimc(){
    system("multimc");
}

void minecraft_launcher(){
    system("minecraft-launcher");

}
