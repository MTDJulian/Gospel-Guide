class YError(Exception): 
	def __init__(self, message: str) -> None:
		self.message = message
		super().__init__(message)

class InvalidRange(YError):
	pass

class Range:
	def __init__(self, start: int, end: int = 0) -> None: 
		if start > end and end != 0: 
			raise InvalidRange("verse start **(%d)** larger than end **(%d)**" % (start, end))

		self.start = start
		self.end = end
