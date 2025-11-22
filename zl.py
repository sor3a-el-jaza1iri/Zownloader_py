import json
import yt_dlp

json_path = 'C:\\Users\\ASUS ZENBOOK\\zp\\Zownloader_py\\info_jsons\\video_info.json'




def init_d(): # sets the download path and url
    
    global url , download_path
    
    url = input("insert the url of the video : ")
    category = input("select the category of your video: ")
    download_path = f'C:\\Users\\ASUS ZENBOOK\\zp\\Zownloader_py\\zl_vids\\{category}\\%(title)s.%(ext)s'
    
    print(f"so your url is {url} and your download path is {download_path} all set then")

# downloads json file  
def save_video_info(url, json_path): 
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        with open(json_path, 'w') as json_file:
            json.dump(info_dict, json_file, indent=4)


def download_best_audio_video(url, download_path):
    ydl_opts = {
        'outtmpl': download_path,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        },
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
            }
        },
        'throttled_rate': '100K',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_best_audio_only(url, download_path):
    ydl_opts = {
        'format': 'bestaudio',  # Automatically selects the best audio quality
        'outtmpl': download_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_best_video_only(url, download_path):
    ydl_opts = {
        'format': 'bestvideo',  # Automatically selects the best video quality (no audio)
        'outtmpl': download_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def choose_format(): # selects from three formats depending on prefrence
    f = input("vid/aud = 0 , aud = 1 , vid = 2 , exit = 3 : ")

    if f == "0":
        download_best_audio_video(url, download_path)
    elif f == "1":
        download_best_audio_only(url, download_path)
    elif f =="2":
        download_best_video_only(url, download_path)
    elif f == "3":
        return 1
    else:
        print("Wrong notation try again.")
        choose_format()

# step 1 get the nmb of videos the url and category of the video


while True:
    try:
        n = int(input("Hello, how many downloads ? : "))
        break
    except ValueError:
        print("That's not a valid integer. Please try again.")


def h_many(n):
    i = 0
    while i < n :
        init_d()
        
        print(f"{url}/n ,{download_path} ")
        # Step 2: Save video info to JSON file

        save_video_info(url, json_path)

        #step 3: download the video according to the selected format

        choose_format()

        i =+ 1

h_many(n)