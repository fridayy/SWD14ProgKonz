#!/usr/bin/env python3
# Benjamin "krennben14" Krenn [1410418084]
# ProgKonz  -  Exercise 05

import time
from random import randint
from threading import Thread

# file
name = 'krennben14'
exercise = 'ex05'
f = open('{0}_{1}.out'.format(exercise, name), 'w')


class Downloader(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self._url = url

    def run(self):
        print('Download started: {}'.format(self._url))
        time.sleep(randint(1, 3))
        print('Download stopped {}'.format(self._url))

    def getBytes(self):
        t = self._url.split('/')
        return len(t[len(t) - 1])

    def getFilename(self):
        t = self._url.split('/')
        return t[len(t) - 1]


urls = ['http://myserver.com/flower.gif',
        'https://fake.org/img/tree.bmp',
        'cifs://fake.org/img/flowers.zip',
        'afp://www.flowerpower.tv/green.gif',
        'ftps://ftp.fake.org/img/logo.gif',
        'http://www2.fake.org/images/small/grass.svg',
        'https://fake.org/thumbs/logo.jpg'
        ]

threads = []
size = 0
count = 1
for _ in urls:
    thread = Downloader(_)
    threads.append(thread)
    thread.start()
    print('Started download {} : {}'.format(count, thread.getFilename()))
    size += thread.getBytes()
    count += 1
    print('Added len: {}'.format(thread.getBytes()))

f.write('1: We started the download of {} files.\n'.format(len(threads)))

for _ in threads:
    _.join()

f.write('2: The overall bytes reported by the downloaded files is {}.\n'.format(size))
f.write('3: {} files downloaded. Done!\n'.format(len(threads)))
f.close()
