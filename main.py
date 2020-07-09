#!/usr/bin/env python3

import subprocess
import os
import extra
import requests
from pathlib import Path
home = str(Path.home())

instances = os.listdir("{0}/.local/share/multimc/instances".format(home))
instances.remove("_MMC_TEMP");instances.remove("instgroups.json")

print("1. Minecraft Launcher")
print("2. MultiMC")
print("3. MCPElauncher")
for instance in instances:
	print("{0}. {1}".format(instances.index(instance) + 4,instance))
launcher_choice = int(input("> "))

if(launcher_choice == 1):
	print("You picked Minecraft Launcher. Opening minecraft-launcher...")
	subprocess.run(["minecraft-launcher"])
elif(launcher_choice == 2):
	print("You picked MultiMC. Opening multimc...")
	subprocess.run(["multimc"])
elif(launcher_choice == 3):
	print("You picked MCPElauncher.")
	if(not extra.file_exists("MCPE.AppImage")):
		download_choice = "Y"
	else:
		download_choice = input("Would you like to update MCPE.AppImage? (Y/n) > ")
	if(download_choice == "Y"):
		print("Downloading MCPE.AppImage...")
		appimage = requests.get("https://github.com/ChristopherHX/linux-packaging-scripts/releases/download/appimage/Minecraft_Bedrock_Launcher-x86_64.0.0.510.AppImage", allow_redirects=True)
		open("MCPE.AppImage", 'wb').write(appimage.content)
	subprocess.run(["chmod", "+x", "MCPE.AppImage"])
	subprocess.run(["./MCPE.AppImage"])
elif(launcher_choice >= 4):
	print("You picked {0} on MultiMC. Opening multimc...".format(instances[launcher_choice - 4]))
	subprocess.run(["multimc","-l",instances[launcher_choice - 4]])
