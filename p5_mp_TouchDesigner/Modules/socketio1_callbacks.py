# me - This DAT
# dat - The connected SocketIO DAT
# rowIndex - The row number the message was placed into
# message - An arbitrarily structured message from the server. Depending on the event spec the message could be a dictionary, a list, a string etc.
# event - The name of the event. This name will correspond to an event name in the Event input DAT.
# failure - Whether the connection was closed because of a failure

def onReceiveEvent(dat, rowIndex, message, event):
	if (event == 'id'):
		parent.Host.OnId(message)
	elif (event == 'hostConnect'):
		parent.Host.OnHostConnect(message)
	elif (event == 'clientConnect'):
		parent.Host.OnClientConnect(message)
	elif (event == 'clientDisconnect'):
		parent.Host.OnClientDisconnect(message)
	elif (event == 'receiveData'):
		parent.Host.OnReceiveData(message)
	return

def onOpen(dat):
	return

def onClose(dat, failure):
	return
	