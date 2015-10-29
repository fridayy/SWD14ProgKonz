#!/usr/bin/env python3
# Benjamin "krennben14" Krenn [1410418084]
# ProgKonz  -  Exercise 02

import math

#functions
def getfilename(url):
    l = url.split("/")
    return l[len(l) - 1]

def getservername(url):
    l = url.split(".")
    if not l[0].startswith("www"):
        return l[0]
    else:
        return l[1]

#exercise
name = "krennben14"
urls = "http://www.python.org/images/python-logo.gif,http://www.fh-joanneum.at/favicon.png, https://elearning.fh-joanneum.at/logo.jpg"
f = open('ex02_krennben14.out', 'w')
#1
f.write("1: '{0}' has {1} characters.\n".format(name,len(name)))
#2
f.write("2: '{}'\n".format(name.upper()))
#3
f.write("3: '{}'\n".format(name[-3:]))
#4
f.write("4: 'Example{:03d}'\n".format(len(name)))
#5
surls = urls.split(",")
filenames = []
for i in surls:
    filenames.append(getfilename(i))
f.write("5: ' {} '\n".format(" ".join(filenames)))


#6
f.write("6: Pi is approx '{:.9f}'.\n".format(math.pi))

#7
ulist = ['python.org', 'www.google.com','www.microsoft.com',
        'www.linux.org','facebook.com','perl.org',
        'perl.com','python.com','www2.golang.com']
f.write('7: ')
f.write(str(sorted(ulist, key=lambda url: len(url))))
f.write('\n')
#8
hostnames = []
for i in ulist:
    hostnames.append(getservername(i))
f.write('8: ')
f.write(str(sorted(hostnames, reverse=True)))
f.write('\n')

#9
f.write('9: \'')
f.write(";".join(sorted(set(hostnames))))
f.write('\'\n')

#10
ma = dict()
ma['age'] = 4
ma['name'] = 'maria'
ma['father'] = 'georg'
f.write('10: \'')
f.write(";".join(sorted(ma.keys())))
f.write('\'\n')

#11
ge = dict()
ge['age'] = 40
ge['name'] = 'georg'
ge['father'] = 'joseph'

f.write('11: \'')
f.write(";".join("{0}".format(v) for k,v in sorted(ma.items())))
f.write('\'\n')

#12
f.write('12: \'')
f.write(";".join("{0}".format(v) for k,v in sorted(ge.items())))
f.write('\'\n')
#bye
f.close()