#from libcloud.compute.types import Provider
#from libcloud.compute.providers import get_driver


class Connection:
	def __init__(self, auth_url, auth_username, auth_password, project_name, region_name):

		self.auth_url = auth_url
		self.auth_username = auth_username
		self.auth_password = auth_password
		self.project_name = project_name
		self.region_name = region_name


	def connect(self):
		provider = get_driver(Provider.OPENSTACK)
		self.conn = provider(self.auth_username, self.auth_password, ex_force_auth_url=self.auth_url, ex_force_auth_version='2.0_password', ex_tenant_name=self.project_name, ex_force_service_region=self.region_name)		
		return self.conn
