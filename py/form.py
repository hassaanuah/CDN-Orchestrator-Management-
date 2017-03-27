import smtplib
from mod_python import apache, Session, util
import json
import cgi
from DBManager import DBManager
from connection import Connection
from image import Image
from flavor import Flavor
from network import Network
from node import Node
from accounting import Accounting
WEBMASTER = "webmaster"   # webmaster e-mail
SMTP_SERVER = "localhost" # your SMTP server


auth_username = 'muddesar'
auth_password = '***********'
auth_url = 'http://controller:5000'
project_name = 'admin'
region_name = 'RegionOne'

dbManager = DBManager("127.0.0.1","root","t00r","cdn_db")

connetion = Connection(auth_url, auth_username, auth_password, project_name, region_name)
#conn = connetion.connect()
conn = 8
flavor = Flavor(conn)
image = Image(conn)
node = Node(conn)
network = Network(conn)
accounting = Accounting()


def createCDN(req):
	info =req.form	
	dateStart = info['dateStart']
	dateEnd = info['dateEnd']
	qoe = info['qoe']
	validatetime = info['validatetime']
	cdnname = info['cdnname']
	nbSubscribers = info['nbSubscribers']
	nbVideos = info['nbVideos']
	login = info['login']
	flavors = json.loads(info['flavors'])
	types = json.loads(info['types'])
	regions = json.loads(info['regions'])
	vnfs = json.loads(info['vnfs'])
	result = {}
	dbManager.connect()
	(result['success'], idCDN) =  dbManager.addCDN(login, cdnname, qoe, dateStart, dateEnd, validatetime)
	machineList = []	
	if (result['success']==True):
		#cdnservice update will be later not now....
		(result['success'], machineList) = dbManager.addMachines(idCDN, vnfs, flavors, types, regions)

	#if (result['success']==True):
	#	dbManager.assignMachinesCDN(idCDN, machineList)
		
	dbManager.deconnect()
	return json.dumps(result,indent=1)



def create_machine(req):
	info =req.form	
	cdnname = info['cdnname']
	nbSubscribers = info['nbSubscribers']
	nbVideos = info['nbVideos']
	login = info['login']
	flavors = json.loads(info['flavors'])
	types = json.loads(info['types'])
	regions = json.loads(info['regions'])
	vnfs = json.loads(info['vnfs'])
	result = {}
	dbManager.connect()
	machineList = []	
	(result['success'], machineList) = dbManager.addMachines_existingcdn(cdnname, vnfs, flavors, types, regions)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def account(req):
	info =req.form
	vms = 0 #info['vms']
	types = 0 #info['types']
	flavors = 0 #info['flavors']
	regions = 0 #info['regions']		
	result = {}
	result['success'] = True
	result['account'] = accounting.account(flavors, types)
	return json.dumps(result,indent=1)	


def addUser(req):
	info =req.form
	firstName = info['firstName']
	lastName = info['lastName']
	user = info['user']
	password = info['password']
	secretquestion = info['secretquestion']		
	secretanswer = info['secretanswer']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.insertUser(firstName, lastName, user, password, secretquestion, secretanswer)
	dbManager.deconnect()
	return json.dumps(result,indent=1)



def addUser_admin(req):
	info =req.form
	firstName = info['firstName']
	lastName = info['lastName']
	user = info['user']
	password = info['password']
	secretquestion = info['secretquestion']		
	secretanswer = info['secretanswer']
	secretKey = info['secretKey']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.insertUser_admin(firstName, lastName, user, password, secretquestion, secretanswer, secretKey)
	dbManager.deconnect()
	return json.dumps(result,indent=1)




def addCloud(req):
	info =req.form
	cloudname = info['cloudname']
	cloudlocation = info['cloudlocation']
	longitude = info['longitude']
	latitude = info['latitude']
	url = info['url']		
	cloudprovider = info['cloudprovider']
	providerusername = info['providerusername']
	providerpassword = info['providerpassword']
	availablememory = info['availablememory']
	availablecpu = info['availablecpu']
	availablestorage = info['availablestorage']
	availablenetwork = info['availablenetwork']
	totalmemory = info['totalmemory']
	totalcpu = info['totalcpu']
	totalstorage = info['totalstorage']
	totalnetwork = info['totalnetwork']
	country = info['country']
	city = info['city']
	continent = info['continent']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.insertCloud(cloudname, cloudlocation, longitude, latitude, url, cloudprovider, providerusername, providerpassword, availablememory, availablecpu, availablestorage, availablenetwork, totalmemory, totalcpu, totalstorage, totalnetwork, country, city, continent)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def addLocation(req):
	info =req.form
	location = info['cdnlocation']
	longitude = info['longitude']
	latitude = info['latitude']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.insertLocation(location, longitude, latitude)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def authUser(req):
	info =req.form
	user = info['user']
	password = info['password']		
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.authUser(user, password)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def authUser_admin(req):
	info =req.form
	user = info['user_admin']
	password = info['password_admin']		
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.authUser_admin(user, password)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def forgetpassword(req):
	info =req.form
	user = info['user']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.forgotpassword(user)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def forgetpassword_admin(req):
	info =req.form
	user = info['user']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.forgotpassword_admin(user)
	dbManager.deconnect()
	return json.dumps(result,indent=1)



def verify_answer(req):
	info =req.form
	user = info['user']
	answer = info['password']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.verifyanswer(user,answer)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def verify_answer_admin(req):
	info =req.form
	user = info['user']
	answer = info['password']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.verifyanswer_admin(user,answer)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def clear_database(req):
	info =req.form
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.clear_database()
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def getCDN(req):
	info =req.form
	user = info['user']
	password = info['password']		
	result = {}
	dbManager.connect()
	(result['success'], result['idcdn'], result['namecdn']) =  dbManager.getCdn(user, password)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def cdn_details(req):
	info =req.form
	cdnID = info['cdnID']	
	result = {}
	dbManager.connect()
	(result['success'], result['machine_names'], result['machine_public_ip'], result['machine_private_ip'], result['machine_creation_date'], result['started'], result['machine_flavor'], result['machine_type']) =  dbManager.load_cdn_details(cdnID)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def cdn_modify_details(req):
	info =req.form
	cdnID = info['cdnID']	
	result = {}
	dbManager.connect()
	(result['success'], result['cdn_name'], result['vm_machine_names'], result['vm_machine_IDs']) =  dbManager.cdn_modify_details(cdnID)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def modify_cdn(req):
	info =req.form
	idCDN = info['idCDN']
	cdnname = info['cdnname']
	vm_machines_new_names = json.loads(info['machine_names'])
	result = {}
	dbManager.connect()
	(result['success']) =  dbManager.modify_cdn(idCDN, cdnname, vm_machines_new_names)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def deleteCDN(req):
	info =req.form
	idCDN = info['cdnID']
	result = {}
	dbManager.connect()
	result['success'] = dbManager.removeCDN(idCDN)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def getRegions(req):
	result = {}
	dbManager.connect()
	(result['success'], result['CloudLocation'], result['Longitude'], result['Latitude']) =  dbManager.getRegions()
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def computeVMs(req):
	result = {}
	result['success'] = True
	result['myFlavors'] = ["m1.medium", "m1.small", "m1.medium"]
	result['myTypes'] = ["CONTENT-DB", "STREAMING_SERVER", "STREAMING_SERVER"]
	result['myRegions'] = ["AALTO", "AALTO", "AALTO"]
	result['mynetwork'] = "demo-net"
	dbManager.connect()
	(result['IDFlavor'],result['flavors']) = dbManager.get_flavors()
	(result['status'],result['IDType'],result['types']) = dbManager.get_machinetypes() #image.getImageNames()
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def check_cdnname(req):
	info =req.form
	cdn_name = info['cdn_name']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.check_cdnname(cdn_name)
	dbManager.deconnect()
	return json.dumps(result,indent=1)

def get_region_flavors(req):
	info =req.form
	location = info['location']
	result = {}
	dbManager.connect()
	(result['success'], result['fl']) = dbManager.get_region_flavors(location)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def check_cdnname_modify(req):
	info =req.form
	cdn_name = info['cdn_name']
	idcdn = info['IDCDN']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.check_cdnname_modify(cdn_name, idcdn)
	dbManager.deconnect()
	return json.dumps(result,indent=1)


def delete_machine(req):
	info =req.form
	cdnID = info['cdnID']
	machineID = info['machineid']
	result = {}
	dbManager.connect()
	result['success'] =  dbManager.delete_machine(cdnID, machineID)
	dbManager.deconnect()
	return json.dumps(result,indent=1)





