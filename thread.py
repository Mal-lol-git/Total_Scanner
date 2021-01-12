# -*- coding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

def Tasker(f, number, *args):
        with ThreadPoolExecutor(max_workers=number) as executor:
                executor.map(f, *args)

        return True
