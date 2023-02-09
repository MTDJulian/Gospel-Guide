import os
import sqlite3 

# Utils

from .verse import Verse
from .range import Range 

class KjvBibleSql:

	# path: str to sqlite3 database

	def __init__(self, path: str):
		self.conn = sqlite3.connect(path)
		self.cursor = self.conn.cursor()


	def fetch_verses(self, book: str, chapter: int, verses: list[Range]) -> list[Verse]:
		payload: list[Verse] = []

		for verse in verses:
			if not verse.end:
				query = '''
						SELECT text FROM Bible
						WHERE book = ? AND chapter = ? AND verse = ?
						'''

				self.cursor.execute(query, (book, chapter, verse.start))
			else:
				query = '''
						SELECT text FROM Bible
						WHERE book = ? AND chapter = ? AND verse BETWEEN ? AND ?
						'''

				self.cursor.execute(query, (book, chapter, verse.start, verse.end))



			payload = [Verse(book, chapter, verse.start + index, text[0]) for index, text in enumerate(self.cursor.fetchall())]


		return payload
	def __del__(self) -> None:
		self.conn.close()