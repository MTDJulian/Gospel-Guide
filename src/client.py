import os
import discord
import interactions

from interactions import Client, Intents
from dotenv import load_dotenv


class Yahmen(Client):
	def __init__(self, bible) -> None:
		intents = (Intents.DEFAULT | Intents.GUILD_MEMBERS |
			Intents.GUILD_MESSAGES | interactions.Intents.GUILD_MESSAGE_CONTENT)
		
		super().__init__(token = os.environ.get('TOKEN'), intents = intents)

		self.bible = bible





