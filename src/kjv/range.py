class InvalidRange(Exception):
	pass 


class Range:
	def __init__(self, start: int, end: int = 0) -> None: 
		if start > end and end != 0: 
			raise InvalidRange("Verse start larger than end")

		self.start = start
		self.end = end
