import time
from datetime import date
from sys import argv

from Database.DatabaseManager import insert
from Downloader import Downloader

if len(argv) > 1 and argv[1] == '-h':
    print('''
python3 [Path + /AnimeDownloader] : "For using Downloader shell."

python3 [Path + /AnimeDownloader/Database] <table_name_in_small>
    Options:
        [insert][multiple] : "For using insert with keys visible."
            example : AnimeDownloader/Database downloader insert multiple
            
        [insert] "<Provider>,<Anime Name>,<Season>,<Quality>,<Audio>,<Day>,<EP>" : "For Inserting Directly."
            example : AnimeDownloader/Database downloader
                            insert "[Golumpa],Tokyo Revengers,N/A,[CR-Dub 720p x264 AAC],(DUB),Saturday,01"
                            
        [delete] <row_number_to_delete> : "For Deleting a Row from the database."
            example : AnimeDownloader/Database downloader delete 7
            
        [update] <row_number_to_update> <Column_Name_""> <newValue> : "For updating a row."
            example : AnimeDownloader/Database downloader update 7 "EP" 2
            
        [show] : "For Showing Table."
            example : AnimeDownloader/Database downloader show
            
            
python3 [Path + /AnimeDownloader] [-h] : "For Help."
    ''')
    exit(1)


sec = 60
today = date.today().strftime("%A")
ads = Downloader()
table = ads.animedb['Downloader']

if len(table) != 0:
    ads.fancyPrint(f"Today-{today}", "straight")
    ads.show()
    ads.normalPrint("M. Manually Select from Database.\n"
                    "A. Automatic(Today) from Database.\n"
                    "N. New Anime from Input.\n\n"
                    "Choose....:)", end='\c')
    op = input().upper()
    if op == 'M':
        ads.normalPrint("Select S_No.:", end='\c')
        n = int(input())
        sec = ads.downloadFromDB(n - 1)
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
        ads.normalPrint("Enter First Episode Number: ", end='\c')
        i = int(input())
        ads.fancyPrint(name, "digital")
        i -= 1
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
