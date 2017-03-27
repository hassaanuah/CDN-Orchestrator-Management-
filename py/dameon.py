from DBManager import DBManager
from connection import Connection
from image import Image
from flavor import Flavor
from network import Network
from node import Node
import mysql.connector
import time

def main():


	
	dbManager = DBManager("127.0.0.1","root","t00r","cdn_db")
	dbManager.connect()
	
	row = dbManager.getRegionInfo("AALTO")
	if row == False:
		return

	auth_url = 'http://controller:5000'	
	auth_username = row[3]
	auth_password = row[4]
	project_name = row[5]
	region_name = row[6]
	#print auth_username, auth_password, project_name, region_name
	conntion = Connection(auth_url, auth_username, auth_password, project_name, region_name)
	conn = conntion.connect()
	flavor = Flavor(conn)
	image = Image(conn)
	node = Node(conn)
	network = Network(conn)
	net = network.getNetFromName("demo-net")
	dbManager.deconnect()
	while True:
		dbManager = DBManager("127.0.0.1","root","t00r","cdn_db")
		dbManager.connect()
		idMachines = dbManager.startService()
		for idOld in idMachines:
			(node_name, image_name, flavor_name) = dbManager.getInfoImage(idOld)
			idNew = node.createNode(node_name, image_name, flavor_name, net, image, flavor)
			print idOld, idNew
			dbManager.updateImageID(idOld, idNew)

		#return
		idMachines = dbManager.destroyCDNs()
		print idMachines
		for idNode in idMachines:
			print idNode
			node.destroyNode(idNode)

		dbManager.deconnect()	

		time.sleep(30)
		print "!!!!!! New round !!!!!!"

main()
