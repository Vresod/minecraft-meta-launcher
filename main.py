#!/usr/bin/env python3

import subprocess
import extra

print("1. Minecraft Launcher")
print("2. MultiMC")
print("3. MCPElauncher")
launcher_choice = input("> ")

if(launcher_choice == "1"):
	print("You picked Minecraft Launcher. Opening minecraft-launcher...")
	subprocess.run(["minecraft-launcher"])
elif(launcher_choice == "2"):
	print("You picked MultiMC. Opening multimc...")
	subprocess.run(["multimc"])
elif(launcher_choice == "3"):
	print("You picked MCPElauncher.")
	if(not extra.file_exists("MCPE.AppImage")):
		download_choice = "Y"
	else:
		download_choice = input("Would you like to update MCPE.AppImage? (Y/n) > ")
	if(download_choice == "Y"):
		print("Downloading MCPE.AppImage...")
		subprocess.run(["curl", "-L", "https://github.com/ChristopherHX/linux-packaging-scripts/releases/download/appimage/Minecraft_Bedrock_Launcher-x86_64.0.0.510.AppImage", "--output", "MCPE.AppImage"])
	subprocess.run(["chmod", "+x", "MCPE.AppImage"])
	subprocess.run(["./MCPE.AppImage"])