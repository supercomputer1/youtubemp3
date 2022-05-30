# https://pytube.io/en/latest/user/install.html
from pytube import YouTube, Playlist
import argparse

# parse args 
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True, type=str)
args = parser.parse_args()

print(args.url)

video = YouTube(args.url) 

print(video.title)

streams = video.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('abr')

print(streams) 

# download the highest quality i think
streams[-1].download()

