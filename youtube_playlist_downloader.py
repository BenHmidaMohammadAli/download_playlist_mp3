from pytube import Playlist
import os
import re  

# Function to download YouTube playlist as MP3
def download_playlist(url):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for video in playlist.videos:
        try:
            print(f"Downloading: {video.title}")
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_stream.download(output_path="downloads")
        except Exception as e:
            print(f"Error downloading {video.title}: {e}")


if __name__ == "__main__":
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    download_playlist(playlist_url)

