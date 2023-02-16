import interactions

from interactions import (Extension, 
						Embed, Button, Color)


class Utils(Extension):
	def __init__(self, client):
		self.client = client
		

	@interactions.extension_command(
	    name = "ping",
	    description = "Pong 🏓",
	    options = [
	    	interactions.Option(
	            name="message",
	            description="Say something or nothing",
	            type=interactions.OptionType.STRING,
	            required=False,
        	),
    	],
    )
	async def ping(self, ctx, message: str = None):
		output = "Pong 🏓"

		if message:
			output = output + ", " + message

		await ctx.send(output)

				
def setup(client):
	Utils(client)
