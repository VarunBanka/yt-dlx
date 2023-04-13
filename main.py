print("Welcome to YT-dLx \n")
print("---------- Software by Varun Banka && Kusti420  ----------\n")


def mainApp():
    print("Please select: \n")
    print("1. Download youtube video \n")
    print("2. Download playlist")
    work = input("3. Exit  \n")

    if work == "1":
        import downloadVdo

    if work == "2":
        import downloadPlaylist

    if work == "3":
        exit

    
mainApp()


while(True):
    restart = input("Would you like to restart? (y/n)   ")
    if restart == "y":
        mainApp()
    elif restart == "n":
        exit()
    else:
        print("Thanks for using DataHive")
        exit()