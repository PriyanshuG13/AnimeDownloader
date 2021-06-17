import webbrowser
import clipboard
import requests
from bs4 import BeautifulSoup
import time
from os import system

sec = 60

def DLNAnime(name, ep):
    url = "https://nyaa.iss.one/?f=0&c=0_0&q="

    for i in name:
        if i == " ":
            url += "+"
            continue
        url += i

    ep = str(int(ep) + 1)
    if int(ep) < 10:
        ep = "0" + str(int(ep) + 1)

    url += ep
    # webbrowser.open(url, new=2)
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('td', class_='text-center')
        link = results[0].find_all('a')
        # download = "https://nyaa.iss.one/" + link[0]["href"]
        # webbrowser.open(download, new=2)
        clipboard.copy(link[1]["href"])
        system(f'figlet -w $(tput cols) -c -f digital "Downloading {ep}" | lolcat')
        system(f'open -a "Free Download Manager" {link[1]["href"]}')
        return 30
    except:
        system(f"figlet -w $(tput cols) -c -f short Not Yet Available | lolcat")
        return 1


system(f"""clear
        if [ $(tput cols)  -le  100 ]
            then
              figlet -w $(tput cols) -c -f small Anime Downloader Script | lolcat
        else
              figlet -w $(tput cols) -c -f isometric3 Anime Downloader Script | lolcat
        fi
        """)

print("Enter Anime Name from nyaa.iss.one")
name = input("Enter Anime Full Name without EP:")
se = int(input("Enter Episode Count(From):"))
i = se
system(f'figlet -w $(tput cols) -c -f digital "{name}" | lolcat')
while sec != 1:
    sec = DLNAnime(name, i)
    i += 1
    time.sleep(sec)

# [Golumpa] Kaguya-sama - Love is War [FuniDub 720p x264 AAC]
# [SubsPlease] Black Clover (1080p)
