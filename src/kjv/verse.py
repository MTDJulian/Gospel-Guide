class Verse:
	def __init__(self, book: str, chapter: int, verse: int, text: str) -> None:
		self.book = book
		self.chapter: int = chapter
		self.verse: int = verse 
		self.text: str = text

	def __str__(self) -> str: 
		return self.text