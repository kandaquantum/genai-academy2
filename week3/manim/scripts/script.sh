#!/bin/bash
# MOEのビデオと音声を結合する
ffmpeg -i media/videos/moe/1080p60/MixtureOfExperts.mp4 -i speech_moe.mp3 -c:v copy -b:a 192k -af "apad" -shortest temp.mp4
# 字幕を追加して最終的なビデオを作成する
ffmpeg -i temp.mp4 -vf "subtitles=moe.srt" output.mp4
# 処理完了のメッセージを表示する
echo "Video processing completed. The output file is "output.mp4"."
