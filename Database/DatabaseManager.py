import csv
import json
import pathlib
import subprocess

from prettytable import PrettyTable


class DatabaseManager:
    def __init__(self, db='downloader', animedbFile='Anime_Database.json'):
        self.curPath = pathlib.Path(__file__).parent.absolute()
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
                    'Audio': '(SUB)',
                    'Air_Day': 'Sunday'
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
            self.normalPrint("Creating New Database File(JSON) :)\n"
                             "Looking like this")
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
                self.normalPrint(f"Insert Element({len(adbn)})")
                self.normalPrint("Anime Name: ", end='\c')
                aname = input()
                self.normalPrint("Date Aired: ", end='\c')
                releasedate = input()
                self.normalPrint("Airing Status: ", end='\c')
                astatus = input()
                self.normalPrint("Watching Status: ", end='\c')
                wstatus = input()
                self.normalPrint("Genres(comma seprated): ", end='\c')
                genres = input().split(",")
                self.normalPrint("Seasons(if any): ", end='\c')
                seasons = input()
                self.normalPrint("Last Episode(if with season than total): ", end='\c')
                ep = input()
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
                self.normalPrint(f"Insert Element({len(adbn)})")
                self.normalPrint("Provider Name: ", end='\c')
                provider = input()
                self.normalPrint("Anime Name: ", end='\c')
                aname = input()
                self.normalPrint("Season Number(if any): ", end='\c')
                season = input()
                self.normalPrint("Episode Number: ", end='\c')
                ep = input()
                self.normalPrint("Quality: ", end='\c')
                quality = input()
                self.normalPrint("Audio(SUB/DUB): ", end='\c')
                audio = input()
                self.normalPrint("Air_Day: ", end='\c')
                aday = input()
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
        self.normalPrint(f"Committed rows:{j}")

    def show(self):
        i = 1
        rows = self.animedb[self.mainkey]
        if len(rows) != 0:
            table = PrettyTable(padding_width=1)
            header = ["S_No."]
            header.extend(list(rows[0].keys()))
            table.field_names = header
            table.align = 'l'
            for row in rows:
                row = list(row.values())
                row.insert(0, i)
                table.add_row(row)
                i += 1

            if self.mainkey == 'List':
                self.normalPrint(table.get_string())
            elif self.mainkey == 'Downloader':
                header = ["S_No.", "Anime_Name", "EP", "Audio", "Air_Day"]
                self.normalPrint(table.get_string(fields=header))

    def normalPrint(self, text, end=''):
        try:
            subprocess.run(f'echo "{text} {end}" | lolcat', shell=True, check=True)
        except:
            if end == '\c':
                print(text, end='')
            else:
                print(text)

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
        self.normalPrint(f"Created CSV File with Name Anime_{self.mainkey}.csv")
        animedb.close()
