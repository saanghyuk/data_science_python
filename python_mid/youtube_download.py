import youtube_download
import os

# 실행되는 폴더 안에 '영상제목.확장자' 형식으로 다운로드
output_dir = os.path.join('./', '%(title)s.%(ext)s')

# 여러 영상을 받을 수 있고 플레이리스트도 가능함
download_list = [
    'https://www.youtube.com/watch?v=S6B5Sbh2U0Y',
    ]

ydl_opt = {
    'outtmpl': output_dir,
    'format': 'bestvideo/best', #최상 품질의 비디오 형식 선택
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(download_list)

print('다운로드 완료했습니다.')