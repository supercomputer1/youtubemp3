#!/usr/bin/env python3
import argparse
import time
from pytube import YouTube, Playlist

# parse args 
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=False, type=str)
parser.add_argument('--playlist', required=False, type=str)
args = parser.parse_args()

def get_playlist_urls(url): 
    return Playlist(url).video_urls

def get_song(url): 
    return YouTube(url) 

def get_highest_quality_audio_stream(song): 
    streams = song.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('abr') 
    return streams[-1] 


def download_stream(stream, title): 
    print(f"Downloading {title}..") 
    stream.download()
    print("Download complete..")


if args.url: 
    song = get_song(args.url)
    stream = get_highest_quality_audio_stream(song)
    download_stream(stream, song.title)

if args.playlist:         
    for url in get_playlist_urls(args.playlist): 
        song = get_song(url)
        stream = get_highest_quality_audio_stream(song)
        download_stream(stream)
        time.sleep(3)
