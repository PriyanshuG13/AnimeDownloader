from datetime import date
import time
from AnimeDatabase.AnimeDB import DatabaseManager as Animedb
from DownloadAnime import Downloader
from os import system

sec = 60
today = date.today().strftime("%A")
db = Animedb()

system(f"""
        figlet -w $(tput cols) -c -f straight Today-{today} | lolcat
        echo "Auto(A) or Manual(M):\c" | lolcat
        """)

if input().upper() == 'M':
    db.show()
    system('echo "Choose:\c" | lolcat')
    n = int(input())
    sec = DLAnime(n, db)

else:
    if today == "Monday":
        sec = DLAnime(3, db)
    elif today == "Tuesday":
        pass
    elif today == "Wednesday":
        sec = DLAnime(2, db)
    elif today == "Thursday":
        pass
    elif today == "Friday":
        pass
    elif today == "Saturday":
        sec = DLAnime(6, db)
        time.sleep(sec)
        sec = DLAnime(7, db)
        time.sleep(sec)
        sec = DLAnime(8, db)
    elif today == "Sunday":
        sec = DLAnime(1, db)
        time.sleep(sec)
        sec = DLAnime(4, db)

if (sec != 1):
    system('echo "Commit?? : \c" | lolcat')
    if input().upper() == 'Y':
        db.commit()
        system('echo "Committed........." | lolcat')




def New():
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
