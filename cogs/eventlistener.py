import interactions
from interactions import Extension
from interactions.ext.tasks import IntervalTrigger, create_task


class EventListener(Extension):
	def __init__(self, client):
		self.client = client
		self.ready = False

		self.update_daily_verse.start(self)
	
	@interactions.extension_listener()
	async def on_ready(self) -> None:
		if self.ready: 
			return

		self.ready = True
		await self.client.get_daily_verse()

	@create_task(IntervalTrigger(3600))
	async def update_daily_verse(self):
		await self.client.get_daily_verse()

	# Logger will automatically capture error
	@interactions.extension_listener()
	async def on_command_error(self, ctx, error):
		await ctx.send(
				"⚠️ Unexpected command error, if this persist please contact the owner", 
				ephemeral = True)

def setup(client):
	EventListener(client)