#!/usr/bin/env python3
# Benjamin "krennben14" Krenn [1410418084]
# ProgKonz  -  Exercise 03

import re

urls = ['python.org', 'www.google.com', 'www.microsoft.com',
        'www.linux.org', 'facebook.com', 'perl.org',
        'perl.com', 'python.com', 'www2.golang.com']

rxtext = """
The anatomy of a large-scale hypertextual Web search engine
Sergey Brin and Lawrence Page,
Computer Science Department, Stanford University, Stanford, CA 94305, USA
Available online 17 June 1999.
Abstract
In this paper, we present Google, a prototype of a large-scale search engine which makes heavy use of the structure present in hypertext. Google is designed to crawl and index the Web efficiently and produce much more satisfying search results than existing systems. The prototype with a full text and hyperlink database of at least 24 million pages is available at http://google.stanford.edu/
To engineer a search engine is a challenging task. Search engines index tens to hundreds of millions of Web pages involving a comparable number of distinct terms. They answer tens of millions of queries every day. Despite the importance of large-scale search engines on the Web, very little academic research has been done on them. Furthermore, due to rapid advance in technology and Web proliferation, creating a Web search engine today is very different from three years ago. This paper provides an in-depth description of our large-scale Web search engine - the first such detailed public description we know of to date.
Apart from the problems of scaling traditional search techniques to data of this magnitude, there are new technical challenges involved with using the additional information present in hypertext to produce better search results. This paper addresses this question of how to build a practical large-scale system which can exploit the additional information present in hypertext. Also we look at the problem of how to effectively deal with uncontrolled hypertext collections where anyone can publish anything they want.
Author Keywords: World Wide Web; Search engines; Information retrieval; PageRank; Google
(downloaded 15. Jan. 2010; http://www.sciencedirect.com/)
"""

#file
name = 'krennben14'
exercise = 'ex03'
f = open('{0}_{1}.out'.format(exercise, name), 'w')

# 1:
#map applies the function to all the elements of a list
#.strip to remove the www. and .org part.
orgurls = list(filter(lambda x: '.org' in x, urls))
hostnames = list(map(lambda x: x.strip('www.org').capitalize(), orgurls))
f.write('1: {}\n'.format(sorted(hostnames)))

#2:
def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n - 1)

f.write('2: {}\n'.format(factorial(7)))

#3:
f.write('3: {}\n'.format(re.findall(r'\d+', rxtext)))

#4:
f.write('4: {}\n'.format(re.findall('(\wage(?:\w+|))', rxtext)))

#5:
f.write('5: {}\n'.format(re.findall('search', rxtext, flags=re.IGNORECASE)))

#6:
#That regex.. ;)
f.write('6: {}\n'.format(re.findall("(\d{2}(?:\.)?(?:\s)(?:Jan(?:\.|uary)|Feb(?:\.|uary)|Mar(?:\.|ch)|Apr(?:\.|il)|May|Jun(?:\.|e)"
                 "|Jul(?:\.|y)|Aug(?:\.|ust)|Sep(?:\.|temper)|Oct(?:\.|ober)|Nov(?:\.|ember)|Dec(?:\.|ember))"
                 "\s(?:\d{4}))", rxtext, flags=re.IGNORECASE)))

#7:
f.write('7: {}\n'.format(re.findall('(?:http://)(\w+\.\w+\.\w+)', rxtext, flags=re.IGNORECASE)))

#8:
#Hack with join and split because I couldn't get it to work with regex alone.
keywords = re.findall('(?:Keywords:)(.*[^;])', rxtext)
keywords = ''.join(keywords)
f.write('8: {}\n'.format(keywords.strip().split('; ')))

#9:
def idGen(count):
    startid = 2001
    for x in range(startid,startid + count,1):
        yield x

studentids = idGen(7)

for x in studentids:
    f.write('9: {}\n'.format(x))


f.close()


