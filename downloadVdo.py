try:
    import os
    import pytube

except ImportError: 
    import fixImport


# Enter the URL of the YouTube video you want to download
video_url = input("Enter the URL of the video: ")

try:
    # Create a YouTube object using the video URL
    youtube = pytube.YouTube(video_url)

    # Get all available video streams
    video_streams = youtube.streams.filter(progressive=True)

    # Print a list of available video formats and resolutions
    for i, stream in enumerate(video_streams):
        print(f"{i+1}. {stream.resolution} ({stream.mime_type})")

    # Prompt the user to select the desired video format and resolution
    selection = int(input("Enter the number corresponding to the desired video format and resolution: "))

    # Get the selected video stream
    video_stream = video_streams[selection - 1]

    # Download the video to the current working directory
    video_stream.download()

except Exception as e:
    print(f"Error: {e}")