"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class HostExt:
	"""
	HostExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# Initialize internal variables
		self.roomId = str(self.ownerComp.par.Roomid)
		self.socketIoDat = ipar.Host.Socketiodat
		self.id = None
		self.hostConnected = False

		
		
		return

	def OnId(self, data):
		self.id = data

		print("id: " + self.id)
		return

	def Connect(self):
		data = { 'name': 'host', 'roomId': self.roomId }
		self.socketIoDat.eval().emit('join', data=data)

		return
	
	def SetRoomId(self, data):
		self.roomId = data
		return

	def OnHostConnect(self, data):
		print("Host connected to server.")
		self.hostConnected = True
		
		if (not self.roomId):
			self.roomId = data.roomId
		return

	def OnClientConnect(self, data):
		print("Client connected to server.")
		return
	
	def OnClientDisconnect(self, data):
		print("Client disconnected to server.")
		return
	
	def OnReceiveData(self, data):
		print(data)
		return