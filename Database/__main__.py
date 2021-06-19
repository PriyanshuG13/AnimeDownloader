from sys import argv
from DatabaseManager import DatabaseManager, insert

if len(argv) > 1:
    dbm = DatabaseManager(argv[1])
    if argv[2] == 'insert':
        if argv[3] == 'multiple':
            insert(dbm)
        else:
            dbm.insert(argv[3])
            dbm.commit()
    elif argv[2] == 'update':
        dbm.update(argv[3], argv[4], argv[5])
        dbm.commit()
    elif argv[2] == 'delete':
        dbm.delete(argv[3])
        dbm.commit()
    elif argv[2] == 'show':
        dbm.show()
