# YouTube Playlist Downloader

This Python script allows you to download a YouTube playlist as MP3 files. It utilizes the `pytube` library to fetch the video URLs from the playlist and download the audio streams of each video as MP3 files.

## How it works

1. Clone or download the repository to your local machine:
   `git clone https://github.com/BenHmidaMohammadAli/download_playlist_mp3.git`
   
2. Navigate to the project directory:
    `cd youtube_playlist_downloader`

3. Create a virtual environment (optional but recommended):
    `python3 -m venv myenv   # Create a virtual environment named myenv`

4. Activate the virtual environment:
    `source myenv/bin/activate   # For Linux/Mac`
    `myenv\Scripts\activate      # For Windows`

5. Install the required dependencies:
    `pip install -r  requirements.txt`

6. Run the script:
    `python youtube_playlist_downloader.py`
    
7. Enter the URL of the YouTube playlist when prompted.

8. The script will download the audio streams of each video in the playlist as MP3 files in a folder named "downloads" within the current directory.

9. Once done, deactivate the virtual environment: 
    `deactivate`
    
    
# Requirements
Python 3.x
    pytube library
# Author
    [https://github.com/BenHmidaMohammadAli]
