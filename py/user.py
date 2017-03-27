class USER:
	def __init__(self, connection):

		self.connection = connection
		self.Nodes = {}
		#for node in self.connection.list_nodes():		
		#	self.Nodes[node.name] = node		



	def getNodeNames(self):

		return self.Nodes.keys()


	def createNode(self, node_names, image_names, flavor_names, net, image, flavor):

		namesNode = node_names.split(",")
		namesImage = image_names.split(",")
		namesFlavor = flavor_names.split(",")
		i = 0
		all_in_one_security_group = self.connection.ex_list_security_groups()[0]
		while i < len(namesNode):
			vm = image.getImageFromName(namesImage[i])		
			flv = flavor.getFlavorFromName(namesFlavor[i])
	    		#node = self.connection.create_node(name=namesNode[i], image=vm, size=flv, networks=[net], ex_security_groups=[all_in_one_security_group])
			#self.connection.wait_until_running([node])
			i += 1

		return 0
