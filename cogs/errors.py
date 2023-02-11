class YError(Exception): 
	def __init__(self, message: str) -> None:
		self.message = message
		super().__init__(message)

class InvalidBookName(YError):
	pass 

class InvalidChapter(YError):
	pass

class InvalidVerse(YError):
	pass