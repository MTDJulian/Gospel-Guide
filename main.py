import os
import asyncio

from src import (GospelGuide, 
				KjvBibleSql, Range)

from dotenv import load_dotenv

load_dotenv()

PARENT_DIR = os.getcwd()
KJV_SQLITE_PATH = os.path.join(PARENT_DIR, 'bible', 'kjv', 'sql', 'bible.db')

Bible = KjvBibleSql(KJV_SQLITE_PATH)


blacklist = ['errors']

def main() -> None:
	bot = GospelGuide(Bible)

	# list of files in the cogs dir
	files = os.listdir('cogs')

	# filter only python files
	files = list(filter(lambda f: f.endswith('.py') and f[:-3] not in blacklist, files))

	# load extensions
	for file in files:
		bot.load('cogs.%s' % file[:-3])
	
	# command helper
	bot.load("interactions.ext.help")
	
	bot.start()

if __name__ == '__main__':
	main()
