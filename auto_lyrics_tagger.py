"""Written By Yask Srivastava  http://yask007.wordpress.com """

import glob
import eyed3
import urllib2
from bs4 import BeautifulSoup

song_name= glob.glob("*.mp3")

for name in song_name:
	try:

		print ((name))
		str = name
		str = unicode(str, errors='replace')
		name = str.encode('utf8')

		
		audiofile = eyed3.load((name))
		print('Test')
		name= name.replace('.mp3','')
		print('Applying to '+name)
		name = name +' lyrics'
		name  = name.replace(' ','+')

		url = 'http://www.google.com/search?q='+name
		
		req = urllib2.Request(url, headers={'User-Agent' : "foobar"})

		response = urllib2.urlopen(req)
		str = response.read()
		str = unicode(str, errors='replace')

		#print(str.encode('utf8'))

		result = str.encode('utf8')

		link_start=result.find('http://www.metrolyrics.com')
		link_end=result.find('html',link_start+1)
		#print(result[link_start:link_start+57])


		link = result[link_start:link_end+4]
		
		lyrics_html = urllib2.urlopen(link).read()
		soup = BeautifulSoup(lyrics_html)
		raw_lyrics= (soup.findAll('p', attrs={'class' : 'verse'}))
		paras=[]
		test1=unicode.join(u'\n',map(unicode,raw_lyrics))

		test1= (test1.replace('<p class="verse">','\n'))
		test1= (test1.replace('<br/>',' '))
		test1 = test1.replace('</p>',' ')
		print (test1)
		audiofile.tag.lyrics.set(u''+test1 )
		udiofile.tag.save()
		print('lyrics Added! ')

	except :
		print ('An error occured for '+name)		

