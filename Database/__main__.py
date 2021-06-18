from DatabaseManager import DatabaseManager as dbm


db = dbm()
db.show()
# db.insert()
db.insert("[SubsPlease],Boku No Hero Academia,S2,02,(1080p),(SUB)")
# db.update(0, "EP", 2)
db.commit()
db.show()
# db.jsonToCSV()
