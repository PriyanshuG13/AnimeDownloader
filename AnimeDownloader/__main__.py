import clipboard
import requests
from bs4 import BeautifulSoup
from datetime import date
import time
from AnimeDatabase.AnimeDB import databaseManager as Animedb
from os import system


class Downloader:
    def __init__(self, n=-1, font=None):
        self.font = font
        self.db = Animedb()
        self.n = n
        self.showHeader()

    def showHeader(self):
        if self.font is not None:
            system(f"figlet -w $(tput cols) -c -f {self.font} Anime Downloader Script | lolcat")
        else:
            system(f"""clear
            if [ $(tput cols)  -le  100 ]
                then
                  figlet -w $(tput cols) -c -f small Anime Downloader Script | lolcat
            else
                  figlet -w $(tput cols) -c -f isometric3 Anime Downloader Script | lolcat
            fi
            """)

    def buildURL(self):
        pass

    def animeDL(self):
        n = self.n
        db = self.db
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


# Downloader = Downloader(font="small")
