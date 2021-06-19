import time
from datetime import date

from Downloader import Downloader
from Database.DatabaseManager import insert

sec = 60
today = date.today().strftime("%A")
ads = Downloader()
table = ads.animedb['Downloader']

if len(table) != 0:
    ads.fancyPrint(f"Today-{today}", "straight")
    ads.normalPrint("M. Manually Select from Database.\n"
                           "A. Automatic(Today) from Database.\n"
                           "N. New Anime from Input.\n\n"
                           "Choose....:)", end='\c')
    op = input().upper()
    if op == 'M':
        ads.show()
        ads.normalPrint("Select S_No.:", end='\c')
        n = int(input())
        sec = ads.downloadFromDB(n)
        if sec != -1:
            ads.commitToDb()

    elif op == 'A':
        rowCount = len(table)
        for i in range(rowCount):
            if today == table[i]['Air_Day']:
                sec = ads.downloadFromDB(i)
                time.sleep(sec)
        ads.commitToDb()

    elif op == 'N':
        ads.normalPrint("# [Golumpa] Kaguya-sama - Love is War [FuniDub 720p x264 AAC]\n"
                        "# [SubsPlease] Black Clover (1080p)\n"
                        "# [SubsPlease],Boku No Hero Academia,N/A,(1080p),N/A,N/A\n"
                        "Enter Anime Name from https://nyaa.iss.one/\n")
        ads.normalPrint("Enter Anime Full Name without EP: ", end='\c')
        name = input()
        ads.normalPrint("Enter Episode Count(From): ", end='\c')
        i = int(input())
        ads.fancyPrint(name, "digital")
        while sec != 1:
            sec = ads.downloadFromInput(name, i)
            i += 1
            time.sleep(sec)

        # "https://nyaa.iss.one/?f=0&c=0_0&q=[SubsPlease] Black Clover (1080p)"

else:
    ads.normalPrint("Table is Empty Insert some data.")
    # [SubsPlease],Boku No Hero Academia,N/A,(1080p),(SUB),Saturday,100
    insert(ads)
    ads.show()
