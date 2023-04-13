import os
import pytube
import validators
from enum import Enum


class youtubeScraper():
    def __init__(self, url):
        if validators.url(url):
            self.url = url
        # print("downloading: ", self.url)
        self.download_options = Enum("type", ["video", "playlist", "channel"])
        print(self.parser(self.url))
        pass

    def parser(self, url):
        # if url is of a video
        if "watch" in url:
            return self.download_options.video
        if "playlist" in url:
            return self.download_options.playlist
        if "channel" in url:
            return self.download_options.channel
        pass

