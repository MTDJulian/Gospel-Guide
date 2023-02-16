import os
import sqlite3 

# Utils

from .verse import Verse
from .range import Range 
from .book import Book


class KjvBibleSql:

	# path: str to sqlite3 database

	def __init__(self, path: str):
		self.conn = sqlite3.connect(path)
		self.cursor = self.conn.cursor()

	def chapter_verses(self, book, chapter) -> int:
		query = '''
				SELECT max(verse) as largest_verse 
				FROM Bible
				WHERE book = ? AND chapter = ?
				'''

		self.cursor.execute(query, (book, chapter))

		return self.cursor.fetchall()[0][0]

	def fetch_books(self) -> list[str]: 
		payload: list[Book] = []

		query = '''
				SELECT book, chapter, MAX(verse) AS largest_verse
				FROM Bible
				GROUP BY book
				ORDER BY MAX(id);
				'''

		self.cursor.execute(query)

		payload = [Book(*data) for data in self.cursor.fetchall()]

		return payload

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