#from libcloud.compute.types import Provider
#from libcloud.compute.providers import get_driver


class Image:
	def __init__(self, connection):

		self.connection = connection
		self.Images = {}
		#for image in self.connection.list_images():		
		#	self.Images[image.name] = image		


	def getImageFromName(self, name):
		
		#if name in self.Images.keys():
		#	return self.Images[name]
		
		return ["StreamingServer","CONTENT-DB", "V-CONTENT-DB"]		


	def getImageNames(self):

		return  ["StreamingServer","CONTENT-DB", "V-CONTENT-DB"]	#self.Images.keys()	

