import mysql.connector
import uuid
import time
import datetime



class DBManager:

	def __init__(self, host, user, password, dataBase):

		self.host = host
		self.password = password
		self.user = user
		self.dataBase = dataBase		

	def connect(self):

		self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.dataBase)
		return self.cnx
		#cnx.close()


	def deconnect(self):
		self.cnx.close()


############################################################################################################################


	def insertUser(self, firstName, lastName, user, password, secretquestion, secretanswer):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM user WHERE UserName = '%s'"%(user)
		cursor.execute(get_user)
		if len(cursor.fetchall()) > 0:
			return False	
		add_user = "INSERT INTO user (FirstName, LastName, UserName, Password, SecurityQuestion, SecurityAnswer) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(firstName, lastName, user, password, secretquestion, secretanswer)
		cursor.execute(add_user)
		return True





############################################################################################################################


	def insertCloud(self, cloudname, cloudlocation, longitude, latitude, url, cloudprovider, providerusername, providerpassword, availablememory, availablecpu, availablestorage, availablenetwork, totalmemory, totalcpu, totalstorage, totalnetwork, country, city, continent):

		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM cloud WHERE CloudName = '%s'"%(cloudname)
		cursor.execute(get_user)
		if len(cursor.fetchall()) > 0:
			return False	
		add_cloud = "INSERT INTO cloud (CloudName, CloudLocation, Longitude, Latitude, URL, ProviderUserName, ProviderPassword, AvailableMemory, AvailableCPU, AvailableStorage, AvailableNetwork, TotalMemory, TotalCPU, TotalStorage, TotalNetwork, Country, City, Continent, CloudProvider) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(cloudname, cloudlocation, longitude, latitude, url, providerusername, providerpassword, availablememory, availablecpu, availablestorage, availablenetwork, totalmemory, totalcpu, totalstorage, totalnetwork, country, city, continent, cloudprovider)

		cursor.execute(add_cloud)
		return True


############################################################################################################################


	def insertUser_admin(self, firstName, lastName, user, password, secretquestion, secretanswer, secretkey):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM adminuser WHERE UserName = '%s'"%(user)
		cursor.execute(get_user)
		if len(cursor.fetchall()) > 0:
			return False	
		if secretkey=='admincdn':
			add_user = "INSERT INTO adminuser (FirstName, LastName, UserName, Password, SecurityQuestion, SecurityAnswer) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(firstName, lastName, user, password, secretquestion, secretanswer)
			cursor.execute(add_user)
			return True
		return False



############################################################################################################################


	def authUser(self, user, password):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM user WHERE UserName = '%s' and Password = '%s'"%(user, password)
		S = cursor.execute(get_user)
		rows = []
		try:
			if len(cursor.fetchall()) > 0:
				return S
			else:
				return False
		except:
			return False

	def authUser_admin(self, user, password):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM adminuser WHERE UserName = '%s' and Password = '%s'"%(user, password)
		S = cursor.execute(get_user)
		rows = []
		try:
			if len(cursor.fetchall()) > 0:
				return True
			else:
				return False
		except:
			return False


	def forgotpassword(self, user):
		cursor = self.cnx.cursor()
		get_user = "SELECT SecurityQuestion FROM user WHERE UserName = '%s'"%(user)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		secretquestion = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False	


	def forgotpassword_admin(self, user):
		cursor = self.cnx.cursor()
		get_user = "SELECT SecurityQuestion FROM adminuser WHERE UserName = '%s'"%(user)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		secretquestion = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False



	def verifyanswer(self, user, pwd):
		cursor = self.cnx.cursor()
		get_user = "SELECT Password FROM user WHERE UserName = '%s' and SecurityAnswer = '%s'"%(user,pwd)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False



	def verifyanswer_admin(self, user, pwd):
		cursor = self.cnx.cursor()
		get_user = "SELECT Password FROM adminuser WHERE UserName = '%s' and SecurityAnswer = '%s'"%(user,pwd)
		S = cursor.execute(get_user)
		rows=0
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return (rows)
			else:
				return False
		except:
			return False


############################################################################################################################



	def check_cdnname(self, cdn_name):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM cdn WHERE CDNName = '%s'"%(cdn_name)
		S = cursor.execute(get_user)
		rows = []
		try:
			if len(cursor.fetchall()) > 0:
				return False
			else:
				return True
		except:
			return True



	def check_cdnname_modify(self, cdn_name, cdnid):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM cdn WHERE CDNName = '%s'"%(cdn_name)
		S = cursor.execute(get_user)
		rows = []
		received_data=cursor.fetchall()
		try:
			if len(received_data) > 0:
				cursor = self.cnx.cursor()
				get_user = "SELECT CDNName FROM cdn WHERE IDCDN = %d"%(int(cdnid))
				S = cursor.execute(get_user)
				rows = []
				rows = cursor.fetchall()
				for row in rows:
					if (row[0]==cdn_name):
						return True
					else:
						return False
			else:
				True
		except:
			return True



	def insertLocation(self, location, longitude, latitude):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM servicearea WHERE cdnlocation = '%s'"%(location)
		cursor.execute(get_user)
		if len(cursor.fetchall()) > 0:
			return False		
		add_user = "INSERT INTO servicearea (cdnlocation,longitude,latitude) VALUES ('%s', '%s', '%s')" %(location,longitude,latitude)
		cursor.execute(add_user)
		return True





	def removeCDN(self, idCDN):
		cursor = self.cnx.cursor()
		rm_cdn = "delete from cdn WHERE IDCDN=%s"%(idCDN)
		cursor.execute(rm_cdn)
		req = "SELECT * FROM machines WHERE IDCDN = %s"%(idCDN)
		S = cursor.execute(req)
		rows = []
		try:
			rows = cursor.fetchall()
			for row in rows:
				rm_VM = "UPDATE machines set Deleted = 1 WHERE  IDCDN='%s'"%(idCDN)
				cursor.execute(rm_VM)
		except:
			return False
		return True



	def delete_machine(self, idCDN, machineID):
		cursor = self.cnx.cursor()
		req = "update machines set Deleted=1 WHERE IDCDN = %s and MachineID = '%s'"%(idCDN, machineID)
		try:
			S = cursor.execute(req)
			return True
		except:
			return False



	def getRegionInfo(self, nameRegion):
		req = get_user = "SELECT * FROM servicearea WHERE regionservice = '%s'"%(nameRegion)
		cursor = self.cnx.cursor()
	 	cursor.execute(req)
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				return rows[0]
		except:
			return False	



	def get_region_flavors(self, location):
		get_idcloud = "SELECT IDCloud FROM cloud WHERE CloudLocation = '%s'"%(location)
		cursor = self.cnx.cursor()
	 	cursor.execute(get_idcloud)
		flavors=[]
		rows = []
#	try:
		rows = cursor.fetchall()
		if len(rows) > 0:
			for row in rows:
				idcloud=rows[0]
				get_flavors = "SELECT FlavorName FROM flavors WHERE IDCloud = %d"%(idcloud[0])
				cursor = self.cnx.cursor()
			 	cursor.execute(get_flavors)
				try:
					rows = cursor.fetchall()
					for row in rows:
						flavors.append(row)
					return (True,flavors)
				except:
					return (False,[])
			
			return (False,[])
#	except:
		return (False,[])	



	def clear_database(self):
		cursor = self.cnx.cursor()
		get_user = "delete from user"
		S = cursor.execute(get_user)
		return True	




	def getCdn(self, user, password):
		cursor = self.cnx.cursor()
		get_user = "SELECT * FROM user WHERE UserName = '%s' and Password = '%s'"%(user, password)
		S = cursor.execute(get_user)
		rows = []
		idcdn = []
		namecdn = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				iduser = rows[0][0];
				get_cdn = "SELECT IDCDN, CDNName FROM cdn WHERE IDUser = %d"%(iduser)
				S = cursor.execute(get_cdn)
				try:
					rows = cursor.fetchall()
					for row in rows:
						idcdn.append(row[0])
						namecdn.append(row[1]) 
					return (True, idcdn, namecdn)
				except:
					return (False, idcdn, namecdn)

			else:
				return (False, [], [])
			
		except:
			return (False, [], [])


	def load_cdn_details(self, cdnID):
		cursor = self.cnx.cursor()
		machine_names = []
		machine_public_ip = []
		machine_private_ip = []
		machine_creation_date = []
		machine_flavor = []
		machine_type = []
                started = []
		rows =[]
		rows1 =[]
		rows2 =[]
		get_machines = "SELECT MachineName, MachinePublic_IP, MachinePrivate_IP, MachineCreatedOn, Started, MachineFlavorID, MachineImageID FROM machines WHERE IDCDN = %d and Deleted=0"%(int(cdnID))
		S = cursor.execute(get_machines)
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				try:
					for row in rows:
						machine_names.append(row[0])
						machine_public_ip.append(row[1])
						machine_private_ip.append(row[2])
						machine_creation_date.append(row[3])
						started.append(row[4])
						cursor = self.cnx.cursor()
						get_flavors = "SELECT FlavorName FROM flavors WHERE FlavorID = '%s'"%(row[5])
						S = cursor.execute(get_flavors)
						rows1 = cursor.fetchall()
						for row1 in rows1:
							machine_flavor.append(row1[0])
						cursor = self.cnx.cursor()
						get_types = "SELECT TypeName FROM machinetype WHERE MachineImageID = '%s'"%(row[6])
						S = cursor.execute(get_types)
						rows2 = cursor.fetchall()
						for row2 in rows2:
							machine_type.append(row2[0])
					return (True, machine_names, machine_public_ip, machine_private_ip, machine_creation_date, started, machine_flavor, machine_type)
				except:
					return (False, [], [], [], [], [], [], [])

			else:
				return (False, [], [], [], [], [], [], [])
			
		except:
			return (False, [], [], [], [], [], [], [])



	def cdn_modify_details(self, cdnID):
		cdn_name = []
		vm_machine_names = []
		vm_machine_IDs = []
		rows =[]
		rows1 =[]
		cursor = self.cnx.cursor()
		get_cdn_name = "SELECT CDNName FROM cdn WHERE IDCDN = %d"%(int(cdnID))
		S = cursor.execute(get_cdn_name)
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				try:
					for row in rows:
						cdn_name.append(row[0])
						cursor = self.cnx.cursor()
						get_machine_names = "SELECT MachineName,MachineID FROM machines WHERE IDCDN = %d and Deleted=0"%(int(cdnID))
						S = cursor.execute(get_machine_names)
						rows1 = cursor.fetchall()
						for row1 in rows1:
							vm_machine_names.append(row1[0])
							vm_machine_IDs.append(row1[1])

					return (True, cdn_name, vm_machine_names, vm_machine_IDs)
				except:
					return (False, [], [], [])

			else:
				return (False, [], [], [])
			
		except:
			return (False, [], [], [])



	def modify_cdn(self, cdnID, cdnname, machinenames):
		cursor = self.cnx.cursor()
		vm_ids = []
		rows =[]
		rows1 =[]
		get_machine_ids = "SELECT MachineID FROM machines WHERE IDCDN = %d"%(int(cdnID))
		S = cursor.execute(get_machine_ids)
		try:
			rows = cursor.fetchall()
			for row in rows:
				vm_ids.append(row[0])
		except:
			false

		cursor = self.cnx.cursor()
		get_cdn_name = "update cdn set CDNName='%s' where IDCDN=%d;"%(cdnname, int(cdnID))
		S = cursor.execute(get_cdn_name)
		try:
			#rows = cursor.fetchall()
			try:
				for i in range (0, len(machinenames)):
					cursor = self.cnx.cursor()
					try:
						get_machine_names = "update machines set MachineName='%s' where IDCDN=%d and MachineID = '%s'"%(machinenames[i], int(cdnID), vm_ids[i])
						S = cursor.execute(get_machine_names)
						rows1 = cursor.fetchall()
					except:
						pass
				return (True)
			except:
				return (False)


		except:
			return (False)






	def get_machinetypes(self):
		cursor = self.cnx.cursor()
		get_machine = "SELECT MachineImageID,TypeName FROM machinetype"
		S = cursor.execute(get_machine)
		rows = []
		IDType = []
		TypeName = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				try:
					for row in rows:
						IDType.append(row[0])
						TypeName.append(row[1]) 
					return (True, IDType, TypeName)
				except:
					return (False, IDType, TypeName)

			else:
				return (False, [], [])
			
		except:
			return (False, [], [])




	def get_flavors(self):
		cursor = self.cnx.cursor()
		get_machine = "SELECT FlavorID,FlavorName FROM flavors"
		S = cursor.execute(get_machine)
		rows = []
		IDFlavor = []
		FlavorName = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				try:
					for row in rows:
						IDFlavor.append(row[0])
						FlavorName.append(row[1])
					return (IDFlavor, FlavorName)
				except:
					return (False, [])

			else:
				return (False, [])
			
		except:
			return (False, [])




	
	def getRegions(self):
		cursor = self.cnx.cursor()
		get_services = "SELECT IDCloud,CloudLocation,Longitude,Latitude FROM cloud"
		S = cursor.execute(get_services)
		rows = []
		CloudLocation = []
		Longitude = []
		Latitude = []
		try:
			rows = cursor.fetchall()
			for row in rows:
				CloudLocation.append(row[1])
				Longitude.append(row[2]) 
				Latitude.append(row[3])
			return (True, CloudLocation, Longitude, Latitude)			
		except:
			return (False, ["BBB"], ["CCC"],["DDD"])


	def addCDN(self, login, namecdn, qoe, timestart, timeend, validatetime):
		
		cursor = self.cnx.cursor()
		get_userID = "SELECT * FROM user WHERE UserName = %s"%(login)
		S = cursor.execute(get_userID)
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				IDUser = rows[0][0]				
			else:
				return (False, 0)			
		except:
			return (False, 0)

		timestartmonth=timestart[2:3]
		timestartdate=timestart[4:7]
		timestartyear=timestart[7:12]
		timestart= timestartyear + '-' + timestartmonth + '-' + timestartdate


		timeendmonth=timeend[2:3]
		timeenddate=timeend[4:7]
		timeendyear=timeend[7:12]
		timeend= timeendyear + '-' + timeendmonth + '-' + timeenddate
                if (timestart == '--' or timeend=='--'):
                    timestart= '1111-11-11'
                    timeend= '1111-11-11'
		add_cdn = "INSERT INTO cdn (IDUser, CDNName, QoE, StartTime, StopTime, Permanent) VALUES (%d, %s, %s, '%s', '%s', %s)"%(IDUser, namecdn, qoe, timestart, timeend, validatetime)
		cursor.execute(add_cdn)
		get_cdnID = "SELECT * FROM cdn WHERE CDNName = %s"%(namecdn)
		S = cursor.execute(get_cdnID)
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				idCDN = rows[0][0]	
				return (True, idCDN)			
			else:
				return (False, 0)			
		except:
			return (False, 0)




	def addMachines(self, idcdn, vnfs, flavors, types, regions):

		i = 0
		idservice = 7 # This is the id of AALTO, we should change it later when we disucss...
		machineList = []
		cursor = self.cnx.cursor()
		while i < len(flavors):
			idMachine = str(uuid.uuid4())
			machineList.append(idMachine)
			nameMachine = vnfs[i]
			flavor_ = flavors[i]
			type_ = types[i]
			regions_ = regions[i]
			cursor = self.cnx.cursor()
			get_userID = "SELECT * FROM machinetype WHERE TypeName = '%s'"%(type_)
			S = cursor.execute(get_userID)
			rows = []
			try:
				rows = cursor.fetchall()
				if len(rows) > 0:
					type_id = rows[0][0]				
				else:
					return (False, 0)			
			except:
				return (False, 0)

			cursor = self.cnx.cursor()
			get_userID = "SELECT * FROM flavors WHERE FlavorName = '%s'"%(flavor_)
			S = cursor.execute(get_userID)
			rows = []

			try:
				rows = cursor.fetchall()
				if len(rows) > 0:
					flavor_id = rows[0][0]				
				else:
					return (False, 0)			
			except:
				return (False, 0)


			cursor = self.cnx.cursor()
			get_userID = "SELECT * FROM cloud WHERE CloudLocation = '%s'"%(regions_)
			S = cursor.execute(get_userID)
			rows = []

			try:
				rows = cursor.fetchall()
				if len(rows) > 0:
					cloud_id = rows[0][0]				
				else:
					return (False, 0)			
			except:
				return (False, 0)

			add_Machine = "INSERT INTO machines (Started, Deleted, MachineUUID, MachineName, IDCDN, MachineFlavorID, MachineImageID, IDCloud, MachineID) VALUES ('0', '0', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(idMachine, nameMachine, idcdn, flavor_id, type_id, cloud_id, idMachine)
			cursor.execute(add_Machine)
			i = i + 1
		return (True, machineList)


	def addMachines_existingcdn(self, cdnname, vnfs, flavors, types, regions):

		i = 0
		idservice = 7 # This is the id of AALTO, we should change it later when we disucss...
		machineList = []
		cursor = self.cnx.cursor()
		get_userID = "SELECT IDCDN FROM cdn WHERE CDNName = '%s'"%(cdnname)
		S = cursor.execute(get_userID)
		rows = []
		try:
			rows = cursor.fetchall()
			if len(rows) > 0:
				idcdn = rows[0][0]				
			else:
				return (False, 0)			
		except:
			return (False, 0)

		while i < len(flavors):
			idMachine = str(uuid.uuid4())
			machineList.append(idMachine)
			nameMachine = vnfs[i]
			flavor_ = flavors[i]
			type_ = types[i]
			regions_ = regions[i]
			cursor = self.cnx.cursor()
			get_userID = "SELECT * FROM machinetype WHERE TypeName = '%s'"%(type_)
			S = cursor.execute(get_userID)
			rows = []
			try:
				rows = cursor.fetchall()
				if len(rows) > 0:
					type_id = rows[0][0]				
				else:
					return (False, 0)			
			except:
				return (False, 0)

			cursor = self.cnx.cursor()
			get_userID = "SELECT * FROM flavors WHERE FlavorName = '%s'"%(flavor_)
			S = cursor.execute(get_userID)
			rows = []

			try:
				rows = cursor.fetchall()
				if len(rows) > 0:
					flavor_id = rows[0][0]				
				else:
					return (False, 0)			
			except:
				return (False, 0)


			cursor = self.cnx.cursor()
			get_userID = "SELECT * FROM cloud WHERE CloudLocation = '%s'"%(regions_)
			S = cursor.execute(get_userID)
			rows = []

			try:
				rows = cursor.fetchall()
				if len(rows) > 0:
					cloud_id = rows[0][0]				
				else:
					return (False, 0)			
			except:
				return (False, 0)

			add_Machine = "INSERT INTO machines (Started, Deleted, MachineUUID, MachineName, IDCDN, MachineFlavorID, MachineImageID, IDCloud, MachineID) VALUES ('0', '0', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(idMachine, nameMachine, idcdn, flavor_id, type_id, cloud_id, idMachine)
			cursor.execute(add_Machine)
			i = i + 1
		return (True, machineList)



	def assignMachinesCDN(self, idCDN, machineList):

		cursor = self.cnx.cursor()
		for idMachine in  machineList:
			req = "INSERT INTO cdnmachine VALUES ('%s', '%s')"%(idCDN, idMachine)
			cursor.execute(req)
		return True		


	def getMachineCDN(self, idcdn):
		cursor = self.cnx.cursor()
		get_cdnmachine = "SELECT * FROM cdnmachine  WHERE idcdn= %d "%(idcdn)
		S = cursor.execute(get_cdnmachine)
		rows = []
		myidmachinetostart=[]
		try:
			rows = cursor.fetchall()
			for row in rows:
				myidmachinetostart.append(row[1])
			return myidmachinetostart
		except:
			return False 
                        

                
	def startService(self):
		mytime = time.strftime('%Y-%m-%d %H:%M:%S')
		mytime = datetime.datetime.strptime(mytime,'%Y-%m-%d %H:%M:%S')
		cursor = self.cnx.cursor()
		get_cdn = "SELECT * FROM cdn WHERE started = 0"
		S = cursor.execute(get_cdn)
		rows = []	
		idmachinetoputstart=[]
		try:
			rows = cursor.fetchall()
			for row in rows:
				if (mytime >= row[4]) or row[6] == 1:
					cursor1 = self.cnx.cursor()
					update_cdn = "update cdn set started=1 where idcdn=%d "%(row[0])
					S1 = cursor.execute(update_cdn)
					for  m in self.getMachineCDN(row[0]):
						idmachinetoputstart.append(m);
                                                                                                           
			return idmachinetoputstart                                     

		except:
			return False


	 ##############			



        def destroyRemovedCDNs(self):
		cursor = self.cnx.cursor()
		
		req = "SELECT * FROM cdn WHERE destroy = 1"
		S = cursor.execute(req)
		rows = []
		destroyedMachine = set()	               
		try:
			rows = cursor.fetchall()
			for row in rows:
				idremove = row[0]
				print "CDN should be removed %d"%(idremove)
				req = "DELETE FROM cdn WHERE idcdn = %d"%(idremove)
				cursor.execute(req)				  
				req ="select * from cdnmachine where idcdn = %d "%(idremove)
				S1 = cursor.execute(req)
				rows1 = cursor.fetchall()
				for row1 in rows1:
					print "______________"
					destroyedMachine.add(row1[1])
					print destroyedMachine
					req="delete from machine where idmachine = '%s' "%(row1[1])
					S1 = cursor.execute(req)	
					req="delete from cdnmachine where idmachine = '%s' "%(row1[1])
					S1 = cursor.execute(req)
				
			return destroyedMachine

		except:
			return set()

                
        def destroyOverdatedCDNs(self):

		mytime=time.strftime('%Y-%m-%d %H:%M:%S')
		mytime = datetime.datetime.strptime(mytime,'%Y-%m-%d %H:%M:%S')
		cursor = self.cnx.cursor()
		get_cdn = "SELECT * FROM cdn WHERE started = 1 and validatetime = 0"
		S = cursor.execute(get_cdn)
		rows = []	
		destroyedMachine = set()
	       
		try:
			rows = cursor.fetchall()
			for row in rows:
				if mytime >= row[5]:
					cursor1 = self.cnx.cursor()

					machineToDestroy = set(self.getMachineCDN(row[0]))

					delete_cdn="delete from cdn where idcdn = %d "%(row[0])
					S1 = cursor.execute(delete_cdn)

					delete_cdn="delete from cdnmachine where idcdn = %d "%(row[0])
					S1 = cursor.execute(delete_cdn)

					destroyedMachine = destroyedMachine | machineToDestroy
					for mId in machineToDestroy:
						delete_cdn="delete from machine where idmachine = '%s' "%(mId)
						S1 = cursor.execute(delete_cdn)

	
			return destroyedMachine                                    
		except:
			return set()


        def destroyCDNs(self): 
		return self.destroyRemovedCDNs() | self.destroyOverdatedCDNs()  



	def getInfoImage(self, imageId):
		cursor = self.cnx.cursor()
		get_cdn = "SELECT * FROM machine WHERE idmachine = '%s'"%(imageId)
		S = cursor.execute(get_cdn)
		rows = []	
		try:
			rows = cursor.fetchall()
			row = rows[0]
			return (row[1], row[2], row[3])

		except:
			return False

		             



	def updateImageID(self, idOld, idNew):
		cursor = self.cnx.cursor()
		req = "UPDATE machine set idmachine = '%s' where idmachine = '%s'"%(idNew, idOld)
		S = cursor.execute(req)			

		cursor = self.cnx.cursor()
		req = "UPDATE cdnmachine set idmachine = '%s' where idmachine = '%s'"%(idNew, idOld)
		S = cursor.execute(req)			

