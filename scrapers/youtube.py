import os
import pytube
import validators


class youtubeScraper():
    def __init__(self, url):
        if validators.url(url):
            self.url = url
        print("downloading: ", self.url)
        pass


pass
# sc = youtubeScraper()
