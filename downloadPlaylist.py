try:
    import os
    import pytube

except ImportError: 
    import fixImport


# Enter the URL of the YouTube video you want to download
playlist_url = input("Enter the URL of the playlist: ")

try:
    # Create a Playlist object using the playlist URL
    playlist = pytube.Playlist(playlist_url)

    # Loop through each video in the playlist and download the highest resolution video stream
    for video_url in playlist.video_urls:
        # Create a YouTube object using the video URL
        youtube = pytube.YouTube(video_url)
        
        # Get the highest resolution video stream that is either MP4 or WebM format
        video_stream = youtube.streams.filter(progressive=True, file_extension=("mp4", "webm")).order_by('resolution').desc().first()
        
        # Download the video to the current working directory
        video_stream.download()


except Exception as e:
    print(f"Error: {e}")