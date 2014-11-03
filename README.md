Auto-MP3-Lyrics-Tagger
======================

This program will automatically search for the **Lyrics** of the song online then download the lyrics for the song and add then embed *Lyrics* to the *mp3* file via *eyed3* Tagger. All songs lyrics fetched in one go!

### Instructions
* If You have `pip` installed 
  * Type `pip install -r requirements.txt` to install all the dependecies
* If you don't have `pip` installed [`manual way`]  
  * The file requires *eyed3* and *BeautifulSoup* modules to work , so first install those dependencies
    *  `$ sudo pip install eyed3`
    *  `$ sudo pip install BeautifulSoup`
* Download the archive and extract the `.py` file wherever you have your song collections.
* Open the terminal in that directory
* Type `$ python auto_lyrics_tagger.py` 
* Wait for it to complete

### Youtube Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=xlfLY868YSo
" target="_blank"><img src="http://img.youtube.com/vi/xlfLY868YSo/0.jpg" 
alt="Demo" width="240" height="180" border="10" /></a>

####Side Note:
1. It currently works with English Songs only 
2. Requires *Python 2.7.8* with the module dependecies installed
3. May not work for all song files due to `Encoding` issues [working on it]
4. It currently searches for songs lyrics based on the song name.[Will work by scanning current ID3 tags soon]


### Basic Introduction for people interested in improving this scraper.

This is a web scrapper which scrappes the  Lyrics of music currently based on the file name.

Following things takes place

* Reads the name of all *.mp3 files , stores the name in a list
* Iterating through each song name , send a get request at `Google.com` with the query `song_name Lyrics`
* Looks if the Lyrics Page is available
    * If present , scrape the lyrics
   
### To Contribute 

Anyone with basic Python and Scrapping knowledge can help improving this scrapper.
To get started install the following modules 
* BeatifulSoup
* eyed3
And run the programe.
