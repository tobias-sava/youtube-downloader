# YouTube Video Downloader - 01/09/2025

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

# video download method
def download_video(url, save_path):
  try:
      yt = YouTube(url) # grabs instance of yt video
      streams = yt.streams.filter(progressive=True, file_extension='mp4') # accessing all streams
      highest_res_stream = streams.get_highest_resolution() # gets the highest resolution stream
      highest_res_stream.download(output_path=save_path) # downloads the video
      print(f"Downloaded {yt.title} to {save_path} !")
  except Exception as e:
    print(e)

# input youtube url of video
url = ""
# input path in which video will be saved
save_path = ""

# code below is for ease of use. remove if not needed

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
      print(f"Selected folder: {folder}")

    return folder



if __name__ == "__main__":
  root = tk.Tk()
  root.withdraw()

  video_url = input("Enter the YouTube video URL: ")
  save_dir = open_file_dialog()

  if not save_dir:
     print("Started download...")
     download_video(video_url, save_dir)
  else:
      print("Invalid save location.")

# github.com/tobias-sava