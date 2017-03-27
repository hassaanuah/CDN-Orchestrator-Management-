#from libcloud.compute.types import Provider
#from libcloud.compute.providers import get_driver


security_group_name = 'default'
security_group_exists = False


class Node:
	def __init__(self, connection):

		self.connection = connection
		self.Nodes = {}
		#1for node in self.connection.list_nodes():		
		#1	self.Nodes[node.name] = node		



	def getNodeNames(self):

		return self.Nodes.keys()



	def createNode(self, node_name, image_name, flavor_name, net, image, flavor):

		all_in_one_security_group = self.connection.ex_list_security_groups()[0]
		vm = image.getImageFromName(image_name)	
		flv = flavor.getFlavorFromName(flavor_name)
		#print vm, image_name
		#print flv, flavor_name
		node = self.connection.create_node(name=node_name, image=vm, size=flv, networks=[net], ex_security_groups=[all_in_one_security_group])
		self.connection.wait_until_running([node])
		"""for floating_ip in self.connection.ex_list_floating_ips():
			if not floating_ip.node_id:
				unused_floating_ip = floating_ip
				break

			if not unused_floating_ip and len(self.connection.ex_list_floating_ip_pools())>0:
				pool = self.connection.ex_list_floating_ip_pools()[0]
				floating_ip = pool.create_floating_ip()
				self.connection.ex_attach_floating_ip_to_node(node, floating_ip)"""

		print node
		print node.id
		return node.id


	def destroyNode(self, nodeId):
		for node in self.connection.list_nodes():
			if node.id == nodeId:
				print nodeId, node
				self.connection.destroy_node(node)
				break


	def createNodes(self, node_names, image_names, flavor_names, net, image, flavor):

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

		return

