import clipboard
import requests
from bs4 import BeautifulSoup
from datetime import date
import time
from AnimeDatabase.AnimeDB import DatabaseManager as Animedb
from os import system


class Downloader:
    def __init__(self):
        # self.showHeader()
        self._db = Animedb()
        self.__url = "https://nyaa.iss.one/?f=0&c=0_0&q="

    def showHeader(self, font=None):
        if font is not None:
            system(f"figlet -w $(tput cols) -c -f {font} Anime Downloader Script | lolcat")
        else:
            system(f"""clear
            if [ $(tput cols)  -le  100 ]
                then
                  figlet -w $(tput cols) -c -f small Anime Downloader Script | lolcat
            else
                  figlet -w $(tput cols) -c -f isometric3 Anime Downloader Script | lolcat
            fi
            """)

    def downloadFromDB(self, n):
        db = self._db
        url = self.__url
        row = list(db.animedb['Downloader'][n - 1].values())
        ep = self.__updateEP(row[3])
        for j in range(6):
            if row[j] == 'N/A':
                continue
            elif j == 3:
                url += ep + "+"
            else:
                url += row[j] + "+"
        self.fancyPrint(f'{row[1]}\nEP-{row[3]} -> {ep}', digital)
        try:
            self.__downloader(url)
            db.update(n - 1, "EP", ep)
            self.fancyPrint("COPIED TO CLIPBOARD", 'digital')
            self.fancyPrint("UPDATED EPISODE COUNT", 'straight')
            return 40
        except:
            self.fancyPrint("NOT YET AVAILABLE", 'short')
            return 1

    def downloadFromInput(self, name, ep):
        url = self.__url
        ep = self.__updateEP(ep)
        for i in name:
            if i == " ":
                url += "+"
                continue
            url += i
        url += ep
        try:
            self.__downloader(url)
            self.fancyPrint(F"DOWNLOADING EP-{ep}", 'digital')
            return 30
        except:
            self.fancyPrint("NOT YET AVAILABLE", 'short')
            return 1

    def __downloader(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('td', class_='text-center')
        link = results[0].find_all('a')
        system(f'open -a "Free Download Manager" {link[1]["href"]}')
        self.copyToClipboard(link[1]["href"])
        return link

    def __updateEP(self, ep):
        ep = str(int(ep) + 1)
        if int(ep) < 10:
            ep = "0" + str(int(ep) + 1)
        return ep

    def commit(self):
        system('echo "Commit?? : \c" | lolcat')
        if input().upper() == 'Y':
            self._db.commit()
            self.fancyPrint("COMMITED UPDATES", 'short')

    def fancyPrint(self, text, font='digital'):
        system(f'figlet -w $(tput cols) -c -f {font} "{text}" | lolcat')

    def copyToClipboard(self, string):
        clipboard.copy(string)
