import clipboard
import requests
from bs4 import BeautifulSoup
from datetime import date
import time
from AnimeDB import DownloadAnimeDB
from os import system

sec = 40


# print("Anime-Download-Script")
def DLAnime(n, db):
    row = list(db.animeDB['Download_Anime_List'][n - 1].values())
    url = "https://nyaa.iss.one/?f=0&c=0_0&q="
    # print(row)
    ep = str(int(row[3]) + 1)
    if int(ep) < 10:
        ep = "0" + str(int(row[3]) + 1)

    for j in range(6):
        if row[j] == 'N/A':
            continue
        elif j == 3:
            url += ep + "+"
        else:
            url += row[j] + "+"
    # webbrowser.open(url, new=2)

    system(f'figlet -w $(tput cols) -c -f digital "{row[1]}\n'
           f' EP-{row[3]} -> {ep}" | lolcat')
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('td', class_='text-center')
        link = results[0].find_all('a')
        # download = "https://nyaa.iss.one/" + link[1]["href"]
        # webbrowser.open(download, new=2)
        db.update(n - 1, "EP", ep)
        clipboard.copy(link[1]["href"])
        system(f'''
                figlet -w $(tput cols) -c -f digital "COPIED TO CLIPBOARD" | lolcat
                open -a "Free Download Manager" {link[1]["href"]}
                figlet -w $(tput cols) -c -f straight UPDATED EPISODE COUNT | lolcat
        ''')
        return 40
    except:
        system(f"figlet -w $(tput cols) -c -f short Not Yet Available | lolcat")
        return 1


today = date.today().strftime("%A")
db = DownloadAnimeDB()

system(f"""clear
        if [ $(tput cols)  -le  100 ]
            then
              figlet -w $(tput cols) -c -f small Anime Downloader Script | lolcat
        else
              figlet -w $(tput cols) -c -f isometric3 Anime Downloader Script | lolcat
        fi
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


