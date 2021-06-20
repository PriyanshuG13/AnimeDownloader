import os
import subprocess
import webbrowser

import clipboard
import requests
from bs4 import BeautifulSoup
from pyfiglet import Figlet

from Database.DatabaseManager import DatabaseManager as Animedb


class Downloader(Animedb):
    def __init__(self, delay=60):
        self._COLS = os.get_terminal_size().columns
        self.showHeader()
        super().__init__()
        self.__URL = "https://nyaa.iss.one/?f=0&c=0_0&q="
        self.__delay = delay

    def showHeader(self, font=None):
        os.system('clear||cls')
        cols = self._COLS
        self.drawline(cols)
        if font is not None:
            self.fancyPrint("Anime Downloader Script", font)
        else:
            if cols <= 125:
                self.fancyPrint("Anime Downloader Script", 'small')
            else:
                self.fancyPrint("Anime Downloader Script", 'isometric3')
        self.drawline(cols)

    def downloadFromDB(self, n):
        url = self.__URL
        row = list(self.animedb['Downloader'][n].values())
        ep = self.__incrementEP(row[3])
        for j in range(6):
            if row[j] == 'N/A':
                continue
            elif j == 3:
                url += ep + "+"
            else:
                url += row[j] + "+"
        self.fancyPrint(f'{row[1]}\nEP-{row[3]} -> {ep}', 'digital')
        try:
            self.__downloader(url)
            self.fancyPrint("COPIED TO CLIPBOARD", 'digital')
            self.fancyPrint("UPDATED EPISODE IN DATABASE", 'straight')
            self.update(n - 1, "EP", ep)
            return self.__delay
        except:
            self.fancyPrint("NOT YET AVAILABLE", 'short')
            return 1

    def downloadFromInput(self, name, ep):
        url = self.__URL
        ep = self.__incrementEP(ep)
        url += f"{name} {ep}"
        try:
            self.__downloader(url)
            self.fancyPrint(f"DOWNLOADING EP-{ep}", 'digital')
            return self.__delay
        except:
            self.fancyPrint("NOT YET AVAILABLE", 'short')
            return 1

    def __downloader(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('td', class_='text-center')
        link = results[0].find_all('a')
        self.__openClient(link)
        clipboard.copy(link[1]["href"])
        return link

    def __openClient(self, link):
        try:
            subprocess.run(f'open -a "Free Download Manager" {link[1]["href"]}', shell=True, check=True)
        except:
            self.fancyPrint("Try Installing Free Download Manager", 'mini')
            print("It also Backs Up as a Torrent Client")
            download = "https://nyaa.iss.one/" + link[0]["href"]
            webbrowser.open(download, new=2)

    def __incrementEP(self, ep):
        ep = str(int(ep) + 1)
        if int(ep) < 10:
            ep = "0" + ep
        return ep

    def drawline(self, cols):
        print(end='\nX')
        for col in range(cols - 2):
            print(end='~')
        print('X\n')

    def commitToDb(self):
        self.normalPrint("Commit?? : ", end='\c')
        if input().upper() == 'Y':
            self.commit()
            self.fancyPrint("COMMITED UPDATES", 'short')

        self.drawline(self._COLS)

    def fancyPrint(self, text, font='digital'):
        try:
            subprocess.run(f'figlet -w $(tput cols) -c -f {font} "{text}" | lolcat', shell=True, check=True)
        except:
            f = Figlet(font=font)
            print(f.renderText(text))
