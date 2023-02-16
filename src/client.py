import os
import discord
import aiohttp
import logging
import interactions
from bs4 import BeautifulSoup
from interactions import Client, Intents
from dotenv import load_dotenv


VERSE_OF_THE_DAY = "https://www.biblegateway.com/reading-plans/verse-of-the-day/today?version=KJV"

logger = logging.basicConfig(filename = 'guide.log', encoding = 'utf-8', level = logging.ERROR)

class GospelGuide(Client):
	def __init__(self, bible) -> None:
		intents = (Intents.DEFAULT | Intents.GUILD_MEMBERS |
			Intents.GUILD_MESSAGES | interactions.Intents.GUILD_MESSAGE_CONTENT)
		
		super().__init__(token = os.environ.get('TOKEN'), intents = intents, logging = logger)

		self.bible = bible
		self.daily_verse = None

	async def get_daily_verse(self) -> None: 
		session = aiohttp.ClientSession()
		resp = await session.get(VERSE_OF_THE_DAY, raise_for_status = False)

		if resp.status != 200:
			return

		PAGE = await resp.text()
		
		PAGE = BeautifulSoup(PAGE, "html.parser")

		verse = PAGE.find("div", { "class": "rp-passage-display" })

		self.daily_verse = verse.text
		
		return await session.close()

