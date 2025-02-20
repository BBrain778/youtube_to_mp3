import yt_dlp
import os

def download_youtube_audio(url, output_folder="downloads"):
    try:
        # 確保輸出資料夾存在
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 設定 yt-dlp 下載選項
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # 下載並轉換音訊
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("轉換完成！MP3 檔案已儲存至 downloads 資料夾")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 測試用
if __name__ == "__main__":
    video_url = input("請輸入 YouTube 影片網址: ")
    download_youtube_audio(video_url)
