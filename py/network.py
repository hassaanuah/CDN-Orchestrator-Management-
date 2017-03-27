#from libcloud.compute.types import Provider
#from libcloud.compute.providers import get_driver


class Network:
	def __init__(self, connection):

		self.connection = connection
		self.Networs = {}
		#for net in self.connection.ex_list_networks():		
		#	self.Networs[net.name] = net		

		#1self.networks = self.connection.ex_list_networks()

	def getNetFromName(self, name):
		
		#if name in self.Networs.keys():
		#	return self.Networs[name]

		return -1

