import pytube

print("YT_SCRAPER\n")

url_link = input("#url of the video:\n")
if url_link == "":
    print("incorrect url exiting!!!")
    exit()

url_res = input("\n\n\n\n###LIST###\n"
                "#144p\n"
                "#240p\n"
                "#360p\n"
                "#480p\n"
                "#720p\n"
                "#1080p\n"
                "#1440p\n"
                "#2160\n\n"
                "#which video resolution:\n")

if url_res == "":
    print("incorrect resolution exiting!!!")
    exit()

req_youtube = pytube.YouTube(url_link)
video = req_youtube.streams.filter(res=url_res).first()
url_title = req_youtube.title
print(f"\n\ndownloading {url_title}")
video.download()

print("\ndownloading successful")