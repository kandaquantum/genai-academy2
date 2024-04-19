# プロジェクトのまとめ
## 目標
ビデオファイル `MixtureOfExperts.mp4`に音声ファイル `speech_moe.mp3`と字幕ファイル `moe.srt`を追加する。
## 手順
1. 音声をビデオに追加する：
```shell
ffmpeg -i media/videos/moe/1080p60/MixtureOfExperts.mp4 -i speech_moe.mp3 -c:v copy -b:a 192k -af "apad" -shortest temp.mp4
```
2. 字幕をビデオに追加する：
```shell
ffmpeg -i temp.mp4 -vf "subtitles=moe.srt" output.mp4
```
最終成果物は、音声と字幕が追加された output.mp4 ファイルとなります。

---
そして同じ手順をシェルスクリプトにまとめてみました:
```shell
#!/bin/bash
ffmpeg -i media/videos/moe/1080p60/MixtureOfExperts.mp4 -i speech_moe.mp3 -c:v copy -b:a 192k -af "apad" -shortest temp.mp4
ffmpeg -i temp.mp4 -vf "subtitles=moe.srt" output.mp4
echo "Video processing completed. The output file is output.mp4"
```
このスクリプトはシェルから直接実行できます。たとえば、このスクリプトを script.sh という名前で保存し、実行権限を付与した場合、以下のコマンドで実行できます：
```shell
chmod +x script.sh
./script.sh
```
