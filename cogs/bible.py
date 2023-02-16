import random 
import discord
import interactions
from interactions import (Extension, 
						Embed, Button, Color)

from src import Range, InvalidRange

from .errors import (InvalidBookName, 
					InvalidChapter, InvalidVerse)

# Make the first letter of the string capital
fupper = lambda s: s[0].isdigit() and s[0] + " " + s[2].upper() + s[3:] or s[0].upper() + s[1:]

class Bible(Extension):
	def __init__(self, client):
		bible = client.bible
		
		books = bible.fetch_books()

		self.bible = bible
		self.books = books

		self._client = client

	


	@interactions.extension_command(
		name = "randomverse",
		description = "Get random verse from the bible"
	)
	async def randomverse(self, ctx) -> None:
		book = random.choice(self.books)
		bible = self.bible

		chapter = random.randint(1, book.chapters)
		
		chapter_length = bible.chapter_verses(book.name, chapter)
				
		start = random.randint(1, chapter_length)

		
		await self.preach(ctx, book.name, chapter, start, 0)

	@interactions.extension_command(
		name = "dailyverse",
		description = "Daily verse from the KJV Bible"
	)
	async def dailyverse(self, ctx) -> None:
		verse = self.client.daily_verse

		book = self.client.daily_verse.split(":")[0][:-2]
		chapter, start = verse[len(book):].strip().split(":")

		await self.preach(ctx, book.lower(), int(chapter), int(start), 0)



	@interactions.extension_command(
		name = "preach",
		description = "Get verses from the KJV Bible",
		options = [
	   		interactions.Option(
	            name = "book",
	            description = "Name of Book in the Bible",
	            type = interactions.OptionType.STRING,
	            required = True,
	            autocomplete = True
        	),

        	interactions.Option(
	            name="chapter",
	            description = "Chapter in the Book",
	            type = interactions.OptionType.INTEGER,
	            required = True,
        	),

        	interactions.Option(
	            name = "start",
	            description = "What verse to start reading from",
	            type = interactions.OptionType.INTEGER,
	            required = True,
        	),

        	interactions.Option(
	            name = "end",
	            description = "What verse do you want to end on",
	            type = interactions.OptionType.INTEGER,
	            required = False,
        	),
        	
    	],
    )
	async def preach(self, ctx, book: str, chapter: int, start: int, end: int = 0) -> None: 
		bible = self.bible

		books = list(filter(lambda b: b.name == book, self.books))

		if not books: 
			raise InvalidBookName("**%s** is NOT a valid book in the KJV Bible" % book)

		book = books[0]
		
		if chapter > book.chapters: 
			raise InvalidChapter("**%s** only has **%d** chapters, **%d** is not valid" 
				% (fupper(book.name), book.chapters, chapter))
		
		if (start > book.verses or end > book.verses): 
			raise InvalidVerse(
				"**%s** chapter **%d** only has **%d** verses" % 
				(fupper(book.name), chapter, bible.chapter_verses(book.name, chapter) ))

		# Create an instance of the Embed class
		embed = Embed(title = None, description = None, color = 16777215)

		verses = bible.fetch_verses(book.name, chapter, [Range(start, end)])

		for verse in verses:
			embed.add_field(
				name = "%s %d:%d" % (fupper(verse.book), verse.chapter, verse.verse), 
				value = verse.text, 
				inline = False
			)
			print(verse.text)
 		
		await ctx.send(embeds = [embed], content="**%s %d:%d:%d - King James Version**" % (fupper(book.name), chapter, start, end))

	
	@preach.error
	async def preach_error(self, ctx, error):
		if isinstance(error, InvalidBookName):
			message = error.message
			await ctx.send("%s 📖" % message, ephemeral = True)

		if isinstance(error, InvalidChapter):
			message = error.message 
			await ctx.send("%s ✏️" % message, ephemeral = True)

		if isinstance(error, InvalidVerse):
			message = error.message 
			await ctx.send("%s 🔍" % message, ephemeral = True)

		if isinstance(error, InvalidRange):
			message = error.message 
			await ctx.send("%s 🔢" % message, ephemeral = True)
		print(error)

	@interactions.extension_autocomplete(command="preach", name="book")
	async def book_autocomplete(self, ctx, book_name: str = ""):
		choices = [interactions.Choice(name=fupper(book.name), value=book.name) 
				   for book in self.books if book_name.lower() in book.name.lower()]

		await ctx.populate(choices[:min(25, len(choices))])




def setup(client):
	Bible(client)