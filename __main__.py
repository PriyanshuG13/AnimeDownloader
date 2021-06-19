import time
from datetime import date

from Downloader import Downloader

sec = 60
today = date.today().strftime("%A")
Downloader = Downloader()
Downloader.fancyPrint(f"Today-{today}", "straight")
Downloader.normalPrint("Auto(A) or Manual(M):\c")

if input().upper() == 'M':
    Downloader.show()
    Downloader.normalPrint("Choose Anime S_No.:\c")
    n = int(input())
    sec = Downloader.downloadFromDB(n)

else:
    rows = Downloader.animedb['Downloader']
    rowCount = len(rows)
    for i in range(rowCount):
        if today == rows[i]['Air_Day']:
            sec = Downloader.downloadFromDB(i)
            time.sleep(sec)

Downloader.commitToDb()


def New():
    global sec
    Downloader.normalPrint("Enter Anime Name from https://nyaa.iss.one/")
    Downloader.normalPrint("Enter Anime Full Name without EP: \c")
    name = input()
    Downloader.normalPrint("Enter Episode Count(From): \c")
    i = int(input())
    Downloader.fancyPrint(name, "digital")
    while sec != 1:
        sec = Downloader.downloadFromInput(name, i)
        i += 1
        time.sleep(sec)

    # [Golumpa] Kaguya-sama - Love is War [FuniDub 720p x264 AAC]
    # [SubsPlease] Black Clover (1080p)
    # [SubsPlease],Boku No Hero Academia,N/A,(1080p),N/A,N/A
    # "https://nyaa.iss.one/?f=0&c=0_0&q=[SubsPlease] Black Clover (1080p)"
