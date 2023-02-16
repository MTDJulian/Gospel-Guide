import os
from src import KjvBibleSql

PARENT_DIR = os.getcwd()

KJV_SQLITE_PATH = os.path.join(PARENT_DIR, 'bible', 'kjv', 'sql', 'bible.db')

Bible = KjvBibleSql(KJV_SQLITE_PATH)

Bible.chapter_verses("psalms", 91)