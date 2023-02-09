import os
import asyncio

from src import (Yahmen, 
				KjvBibleSql, Range)

from dotenv import load_dotenv

load_dotenv()

PARENT_DIR = os.getcwd()

KJV_SQLITE_PATH = os.path.join(PARENT_DIR, 'bible', 'kjv', 'sql', 'bible.db')

Bible = KjvBibleSql(KJV_SQLITE_PATH)


def main() -> None:
	bot = Yahmen(Bible)

	for file in os.listdir("cogs"):
		if file.endswith(".py"):
			bot.load(f'cogs.{file[:-3]}' )

	
	bot.start()
if __name__ == '__main__':
	main()
