import time
from datetime import date

from Downloader import Downloader

sec = 60
today = date.today().strftime("%A")
Downloader = Downloader()
Downloader.fancyPrint(f"Today-{today}", "straight")
Downloader.normalPrint("M. Manually Select from Database.\n"
                       "A. Automatic(Today) from Database.\n"
                       "N. New Anime from Input.\n"
                       "Choose....:)", end='\c')
op = input().upper()
if op == 'M':
    Downloader.show()
    Downloader.normalPrint("Select S_No.:", end='\c')
    n = int(input())
    sec = Downloader.downloadFromDB(n)
    if sec != -1:
        Downloader.commitToDb()

elif op == 'A':
    rows = Downloader.animedb['Downloader']
    rowCount = len(rows)
    for i in range(rowCount):
        if today == rows[i]['Air_Day']:
            sec = Downloader.downloadFromDB(i)
            time.sleep(sec)
    Downloader.commitToDb()

elif op == 'N':
    Downloader.normalPrint("Enter Anime Name from https://nyaa.iss.one/")
    Downloader.normalPrint("Enter Anime Full Name without EP: ", end='\c')
    name = input()
    Downloader.normalPrint("Enter Episode Count(From): ", end='\c')
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

# db = dbm()
# db.show()
# db.insert()
# db.insert("[SubsPlease],Boku No Hero Academia,N/A,(1080p),(SUB),Saturday,100")
# db.update(0, "EP", 2)
# db.commit()
# db.show()
# db.jsonToCSV()
