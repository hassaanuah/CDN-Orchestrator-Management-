from DBManager import DBManager



dbManager = DBManager("127.0.0.1","root","t00r","cdn_db")
dbManager.connect()
#dbManager.insertUser("Miloud", "Bagaa", "bagmoul", "CORSO")
idMachines = dbManager.startService()
print "___________________"
print idMachines
print "___________________"
idMachines = dbManager.destroyCDNs()
print "_________00000__________"
print idMachines
print "_________00000__________"
dbManager.deconnect()

