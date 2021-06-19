import csv
import json
import pathlib
from os import system

from prettytable import PrettyTable


class DatabaseManager:
    def __init__(self, db='downloader', animedbFile='Anime_Database.json'):
        self.curPath = pathlib.Path(__file__).parent.absolute()
        self.cacheFile = str(self.curPath) + "/cache.json"
        self.animedbFile = animedbFile
        self.animedbFilePath = str(self.curPath) + "/" + self.animedbFile
        demo = {}
        if db == 'downloader':
            self.mainkey = "Downloader"
            demo = {self.mainkey: [
                "This is a Demo File.",
                "Please Insert Data on your Own.",
                "using the instructions",
                {
                    'Provider': '[SubsPlease]',
                    'Anime_Name': 'One Piece',
                    'Season': 'N/A',
                    'EP': 978,
                    'Quality': '(1080p)',
                    'Audio': '(SUB)'
                }]}
        elif db == "default":
            self.mainkey = "Default"
            demo = {self.mainkey: [
                "This is a Demo File.",
                "Please Insert Data on your Own.",
                "using the instructions",
                {
                    'Anime Name': 'One Piece',
                    'Release Date': '1999-Ongoing',
                    'Airing Status': 'Complete',
                    'Watching Status': 'Watching',
                    'Genres': ['Shounen'],
                    'Seasons': 'N/A',
                    'Episodes': 979
                }]}

        try:
            with open(self.animedbFilePath, 'r') as animedbFile:
                self.animedb = json.load(animedbFile)
        except:
            system('echo "Creating New Database File(JSON) :)" | lolcat')
            print("Looking like this")
            jo = json.dumps(demo, indent=4)
            print(jo)
            with open(self.animedbFilePath, "w") as outfile:
                outfile.write(jo)
            self.animedb = {self.mainkey: []}

        self.animedbEdited = self.animedb

    def insert(self, rows=None):
        adbn = self.animedbEdited[self.mainkey]
        if self.mainkey == 'Default':
            if rows is not None:
                rows = rows.split(",")
                rows = {
                    "Anime Name": rows[0],
                    "Release Date": rows[1],
                    "Airing Status": rows[2],
                    "Watching Status": rows[3],
                    "Genres": [rows[4]],
                    "Seasons": rows[5],
                    "Episodes": rows[6],
                    'Commit': True
                }
            else:
                print(f"Insert Element({len(adbn)})")
                aname = input("Anime Name: ")
                releasedate = input("Date Aired: ")
                astatus = input("Airing Status: ")
                wstatus = input("Watching Status: ")
                genres = input("Genres: ").split(",")
                seasons = input("Seasons(if any): ")
                ep = input("Last Episode(if with season than total): ")
                rows = {
                    "Anime Name": aname,
                    "Release Date": releasedate,
                    "Airing Status": astatus,
                    "Watching Status": wstatus,
                    "Genres": genres,
                    "Seasons": seasons,
                    "Episodes": ep,
                    'Commit': True
                }
        elif self.mainkey == 'Downloader':
            if rows is not None:
                rows = rows.split(",")
                rows = {
                    "Provider": rows[0],
                    "Anime_Name": rows[1],
                    "Season": rows[2],
                    "EP": rows[6],
                    "Quality": rows[3],
                    "Audio": rows[4],
                    "Air_Day": rows[5],
                    "Commit": True
                }
            else:
                print(f"Insert Element({len(adbn)})")
                provider = input("Provider Name: ")
                aname = input("Anime Name: ")
                season = input("Season Number(if any): ")
                ep = input("Episode Number: ")
                quality = input("Quality: ")
                audio = input("Audio(SUB/DUB): ")
                aday = input("Air_Day: ")
                rows = {
                    "Provider": provider,
                    "Anime_Name": aname,
                    "Season": season,
                    "EP": ep,
                    "Quality": quality,
                    "Audio": audio,
                    "Air_Day": aday,
                    "Commit": True
                }

        adbn.append(rows)

    def delete(self, rowNo):
        adbn = self.animedbEdited[self.mainkey]
        adbn.pop(rowNo)
        adbn[rowNo].update({'Commit': True})

    def update(self, rowNo, column, value):
        adbn = self.animedbEdited[self.mainkey]
        adbn[rowNo].update({column: value})
        adbn[rowNo].update({'Commit': True})

    def commit(self):
        j = 0
        adbn = self.animedbEdited[self.mainkey]
        adb = self.animedb[self.mainkey]
        for i in range(len(adbn)):
            try:
                if adbn[i]['Commit']:
                    adbn[i].pop('Commit')
                    try:
                        adb[i] = adbn[i]
                    except:
                        adb.append(adbn[i])
                    j += 1
            except:
                pass

        jo = json.dumps(self.animedb, indent=4)
        with open(self.animedbFilePath, "w") as outfile:
            outfile.write(jo)
        print(f"Committed rows({j})")

    def show(self):
        i = 1
        rows = self.animedb[self.mainkey]
        if len(rows) != 0:
            x = PrettyTable(padding_width=1)
            header = ["S_No."]
            header.extend(list(rows[0].keys()))
            x.field_names = header
            x.align = 'l'
            for row in rows:
                row = list(row.values())
                row.insert(0, i)
                x.add_row(row)
                i += 1

            if self.mainkey == 'List':
                system(f'echo "{x.get_string()}" | lolcat')
            elif self.mainkey == 'Downloader':
                header = ["S_No.", "Anime_Name", "EP", "Audio", "Air_Day"]
                system(f'echo "{x.get_string(fields=header)}" | lolcat')

    def jsonToCSV(self):
        rows = self.animedb[self.mainkey]
        animedb = open(f'Anime_{self.mainkey}.csv', 'w')
        csv_writer = csv.writer(animedb)
        header, i = True, 1
        for row in rows:
            if header:
                head = list(row.keys())
                head.insert(0, 'SNo.')
                csv_writer.writerow(head)
                header = False
            row = list(row.values())
            row.insert(0, i)
            csv_writer.writerow(row)
            i += 1
        animedb.close()
