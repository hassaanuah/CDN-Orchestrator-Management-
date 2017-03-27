#from libcloud.compute.types import Provider
#from libcloud.compute.providers import get_driver

class Flavor:
	def __init__(self, connection):

		self.connection = connection
		self.Flavors = {}
		#for flavor in self.connection.list_sizes():		
		#	self.Flavors[flavor.name] = flavor


	def getFlavorFromName(self, name):

		#if name in self.Flavors.keys():
		#	return self.Flavors[name]
		
		return ["m1.tiny","m1.small","m1.medium","m1.large","m1.xlarge"]		

	def getFlavorNames(self):

		return ["m1.tiny","m1.small","m1.medium","m1.large","m1.xlarge"]#self.Flavors.keys()

