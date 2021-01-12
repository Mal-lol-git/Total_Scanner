from settings import *

def hash_save():
    with open(HASH_SAVE_PATH, 'w') as f:
        for row in list(set(MD5)):
            f.write('%s\n' % row)


