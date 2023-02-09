import interactions
from interactions import Extension


class Bible(Extension):
	def __init__(self, client):
		self.client = client
		self.bible = client.bible

def setup(client):
	Bible(client)