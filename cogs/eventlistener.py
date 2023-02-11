import interactions
from interactions import Extension


class EventListener(Extension):
	def __init__(self, client):
		self.client = client
		self.ready = False

	@interactions.extension_listener()
	async def on_ready(self) -> None:
		if not self.ready:
			print("Client is online")
			self.ready = True


	@interactions.extension_listener()
	async def on_message_create(self, message):
		pass

	@interactions.extension_listener()
	async def on_guild_join(self, guild):
		pass


def setup(client):
	EventListener(client)