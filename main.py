import sys
# print("cmd entered: ", sys.argv)
import validators
# print(validators.url(sys.argv[1]))

# python main.py https://www.google.com arg1, arg2, arg3, etc

class yt_dlx():
    def __init__(self, args):
        print(args)

        if "-h" in args or "--help" in args or len(args) == 0:
            self.__help__()
        elif "-v" in args or "--version" in args:
            self.__version__()
        pass

    def __help__(self):
        """Prints help message"""
        print("not implemented yet")
        # perhaps write some readme file and print that here

    def __version__(self):
        """Prints version"""
        print("yt-dlx version 0.0.1")

if __name__ == "__main__":
    yt = yt_dlx(sys.argv[1::])
