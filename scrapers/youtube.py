import os
import pytube
import validators
from enum import Enum
import json


class youtubeScraper():
    def __init__(self, url):
        if validators.url(url):
            self.url = url
        # print("downloading: ", self.url)
        self.download_options = Enum("type", ["video", "playlist", "channel"])
        print(self.parser(self.url))

        # Download video metadata and thumbnail if URL is of a video
        if self.parser(self.url) == self.download_options.video:
            self.download_metadata()
            self.download_thumbnail()

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
    
    def download_metadata(self):
        # Create a YouTube object and get the video metadata
        youtube = pytube.YouTube(self.url)
        metadata = youtube.player_response['videoDetails']

        # Write the metadata to a JSON file
        with open('video_metadata.json', 'w') as f:
            json.dump(metadata, f)

        print("Metadata downloaded successfully!")
        pass
    
    def download_thumbnail(self):
        # Create a YouTube object and get the video thumbnail URL
        youtube = pytube.YouTube(self.url)
        thumbnail_url = youtube.thumbnail_url

        # Download the thumbnail
        thumbnail = pytube.request.get(thumbnail_url)
        with open('video_thumbnail.jpg', 'wb') as f:
            f.write(thumbnail.content)

        print("Thumbnail downloaded successfully!")
        pass
