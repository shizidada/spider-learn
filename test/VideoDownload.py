import requests


def download_video(link):
    root = 'E:\\Code\\python-workspace\\spider-learn\\MooseSpider\\mp4\\'
    r = requests.get(link)
    with open(root + "4k盛放的花朵.mp4", 'wb') as f:
        f.write(r.content)
    print("所有视频下载完成!")


if __name__ == "__main__":
    video_link = "https://video.699pic.com/videos/27/20/14/a_px8biQt0w0Dp1563272014.mp4"
    download_video(video_link)
