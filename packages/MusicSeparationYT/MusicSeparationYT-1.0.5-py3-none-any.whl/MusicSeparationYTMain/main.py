from pytube import YouTube
from moviepy.editor import *
import demucs.separate
import os


def download_youtube_audio_as_mp3(url):
    # YouTube動画をロード
    yt = YouTube(url)

    # 最高品質のオーディオストリームを選択
    audio_stream = yt.streams.filter(only_audio=True).first()

    # オーディオを一時ファイルとしてダウンロード
    temp_file = audio_stream.download()

    # MoviePyを使用してオーディオをMP3に変換
    audio_clip = AudioFileClip(temp_file)
    # 一時ファイルを削除
    os.remove(temp_file)
    # MP3ファイルとして保存
    audio_clip.write_audiofile('sample.mp3', codec="libmp3lame")

    options = ['sample.mp3',
               "-n", "htdemucs",
               "-o music-separated",
               "--two-stems STEM"
               "--mp3"]

    separated = demucs.separate.main(options)
    
    os.remove('sample.mp3')


if __name__ == '__main__':
    # YouTube動画のURLと保存先のファイル名（拡張子なし）を指定
    download_youtube_audio_as_mp3(input('Enter the URL of the video: '))
