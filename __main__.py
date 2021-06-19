import subprocess
import time
from datetime import date

from Downloader import Downloader

sec = 60
today = date.today().strftime("%A")
Downloader = Downloader()
Downloader.fancyPrint(f"Today-{today}", "straight")
subprocess.run(f'echo "Auto(A) or Manual(M):\c" | lolcat', shell=True)

if input().upper() == 'M':
    Downloader.show()
    subprocess.run(f'echo "Choose Anime S_No.:\c" | lolcat', shell=True)
    n = int(input())
    sec = Downloader.downloadFromDB(n)

else:
    rows = Downloader.animedb['Downloader']
    rowCount = len(Downloader.animedb['Downloader'])
    for i in range(rowCount):
        if today == rows[i][6]:
            sec = Downloader.downloadFromDB(i)
            time.sleep(sec)

if (sec != 1):
    Downloader.commitToDb()


def New():
    global sec
    print("Enter Anime Name from nyaa.iss.one")
    name = input("Enter Anime Full Name without EP:")
    i = int(input("Enter Episode Count(From):"))
    Downloader.fancyPrint(name, "digital")
    while sec != 1:
        sec = Downloader.downloadFromInput(name, i)
        i += 1
        time.sleep(sec)

    # [Golumpa] Kaguya-sama - Love is War [FuniDub 720p x264 AAC]
    # [SubsPlease] Black Clover (1080p)

    # "https://nyaa.iss.one/?f=0&c=0_0&q=[SubsPlease] Black Clover (1080p)"
