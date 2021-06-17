import csv
import json
import pathlib
from prettytable import PrettyTable
from os import system
# from art import *

path = pathlib.Path(__file__).parent.absolute()


class AnimeDB:
    def __init__(self, animeDBFile='AnimeDB.json'):
        self.animeDBFile = str(path) + "/" + animeDBFile
        try:
            with open(self.animeDBFile, 'r') as openfile:
                self.animeDB = json.load(openfile)
        except:
            print("Creating New Database File(JSON):")
            print("{\n"
                  " \t'Anime Name': 'One Piece',\n"
                  " \t'Release Date': '1999-Ongoing',\n"
                  " \t'Airing Status': 'Complete',\n"
                  " \t'Watching Status': 'Watching',\n"
                  " \t'Genres': ['Shounen'],\n"
                  " \t'Seasons': 'N/A',\n"
                  " \t'Episodes': 979\n"
                  "}")
            self.animeDB = {"Anime_List": []}

        self.animeDBNew = self.animeDB

    def insert(self, rows=None):
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
            print(f"Insert Element({len(self.animeDBNew['Anime_List'])})")
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

        self.animeDBNew['Anime_List'].append(rows)

    def delete(self, rowNo):
        self.animeDBNew['Anime_List'].pop(rowNo)
        self.animeDBNew['Anime_List'][rowNo].update({'Commit': True})

    def update(self, rowNo, column, value):
        self.animeDBNew['Anime_List'][rowNo].update({column: value})
        self.animeDBNew['Anime_List'][rowNo].update({'Commit': True})

    def commit(self):
        j = 0
        for i in range(len(self.animeDBNew['Anime_List'])):
            try:
                if self.animeDBNew['Anime_List'][i]['Commit']:
                    self.animeDBNew['Anime_List'][i].pop('Commit')
                    try:
                        self.animeDB['Anime_List'][i] = self.animeDBNew['Anime_List'][i]
                    except:
                        self.animeDB['Anime_List'].append(self.animeDBNew['Anime_List'][i])
                    j += 1
            except:
                pass

        jo = json.dumps(self.animeDB, indent=4)
        with open(self.animeDBFile, "w") as outfile:
            outfile.write(jo)
        print(f"Committed rows({j})")

    def show(self):
        i = 1
        rows = self.animeDB['Anime_List']
        x = PrettyTable(align='l', padding_width=1)
        header = ["Sno."]
        header.extend(list(rows[0].keys()))
        x.field_names = header
        x.align = 'l'
        for row in rows:
            row = list(row.values())
            row.insert(0, i)
            x.add_row(row)
            i += 1
        system(f'echo "{x.get_string()}" | lolcat')

    def jsonToCSV(self):
        rows = self.animeDB['Anime_List']
        animeDB = open('AnimeDB.csv', 'w')
        csv_writer = csv.writer(animeDB)
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
        animeDB.close()

# tprint("""
# Anime
# Database
# Script
# """, "rnd-small")

# db = AnimeDB()
# db.insert()
# db.insert("One Piece,1999-Ongoing,Watching,Shounen,N/A,979")
# db.update(0, "EP", 2)
# db.commit()
# db.show()
# db.jsonToCSV()


class DownloadAnimeDB:
    def __init__(self, animeDBFile='AnimeDB.json'):
        self.animeDBFile = str(path) + "/" + animeDBFile
        try:
            with open(self.animeDBFile, 'r') as openfile:
                self.animeDB = json.load(openfile)
        except:
            print("Creating New Database File(JSON):")
            print("{'Provider': '[SubsPlease]',"
                  " 'Anime_Name': 'Boku No Hero Academia',"
                  " 'Season': S2,"
                  " 'EP': 2,"
                  " 'Quality': '(1080p)',"
                  " 'Audio': '(SUB)'}")
            self.animeDB = {"Download_Anime_List": []}

        self.animeDBNew = self.animeDB

    def insert(self, rows=None):
        if rows is not None:
            rows = rows.split(",")
            rows = {
                "Provider": rows[0],
                "Anime_Name": rows[1],
                "Season": rows[2],
                "EP": rows[3],
                "Quality": rows[4],
                "Audio": rows[5],
                "Commit": True
            }
        else:
            print(f"Insert Element({len(self.animeDBNew['Download_Anime_List'])})")
            provider = input("Provider Name: ")
            aname = input("Anime Name: ")
            season = input("Season Number(if any): ")
            ep = input("Episode Number: ")
            quality = input("Quality: ")
            audio = input("Audio(SUB/DUB): ")
            rows = {
                "Provider": provider,
                "Anime_Name": aname,
                "Season": season,
                "EP": ep,
                "Quality": quality,
                "Audio": audio,
                "Commit": True
            }

        self.animeDBNew['Download_Anime_List'].append(rows)

    def delete(self, rowNo):
        self.animeDBNew['Download_Anime_List'].pop(rowNo)
        self.animeDBNew['Download_Anime_List'][rowNo].update({'Commit': True})

    def update(self, rowNo, column, value):
        self.animeDBNew['Download_Anime_List'][rowNo].update({column: value})
        self.animeDBNew['Download_Anime_List'][rowNo].update({'Commit': True})

    def commit(self):
        j = 0
        for i in range(len(self.animeDBNew['Download_Anime_List'])):
            try:
                if self.animeDBNew['Download_Anime_List'][i]['Commit']:
                    self.animeDBNew['Download_Anime_List'][i].pop('Commit')
                    try:
                        self.animeDB['Download_Anime_List'][i] = self.animeDBNew['Download_Anime_List'][i]
                    except:
                        self.animeDB['Download_Anime_List'].append(self.animeDBNew['Download_Anime_List'][i])
                    j += 1
            except:
                pass

        jo = json.dumps(self.animeDB, indent=4)
        with open(self.animeDBFile, "w") as outfile:
            outfile.write(jo)
        print(f"Committed rows({j})")

    def show(self):
        # i = 0
        # rows = self.animeDB['rows']
        # for row in rows:
        #     i += 1
        #     print(f"{i}.)", end=" ")
        #     row = list(row.values())
        #     for j in range(len(row)):
        #         if j == 3:
        #             print(f"EP-{row[j]}", end=" ")
        #         elif j != 0 and j != 4 and row[j] != 'N/A':
        #             print(row[j], end=" ")
        #     print()
        i = 1
        rows = self.animeDB['Download_Anime_List']
        x = PrettyTable(padding_width=1)
        header = ["Sno."]
        header.extend(list(rows[0].keys()))
        x.field_names = header
        for row in rows:
            row = list(row.values())
            row.insert(0, i)
            x.add_row(row)
            i += 1
        x.align = 'l'
        header = ["Sno.", "Anime_Name", "EP", "Audio"]
        system(f'echo "{x.get_string(fields=header)}" | lolcat')

    def jsonToCSV(self):
        rows = self.animeDB['Download_Anime_List']
        animeDB = open('DownloadAnimeDB.csv', 'w')
        csv_writer = csv.writer(animeDB)
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
        animeDB.close()

# db = DownloadAnimeDB()
# db.insert()
# db.insert("[SubsPlease],Boku No Hero Academia,S2,2,(1080p),(SUB)")
# db.update(0, "EP", 2)
# db.commit()
# db.show()
# db.jsonToCSV()
