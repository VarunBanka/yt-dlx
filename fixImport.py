import os

install_dependencies = input(
    "Some dependencies aren't installed. Would you like to install them? (y/n) ")
if install_dependencies.lower() == "y":
    try:
        os.system("pip install pytube")
        from pytube import *
    
    except Exception as e:
        print(f"Error: {e}")
        input("Press any key to exit...")
        exit()
else:
    input("Apart from power key, press any key to exit...")
    exit()