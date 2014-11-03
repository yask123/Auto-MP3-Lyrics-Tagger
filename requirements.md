This is a web scrapper which scrappes the  Lyrics of music currently based on the file name.

Following things takes place

* Reads the name of all *.mp3 files , stores the name in a list
* Iterating through each song name , send a get request at `Google.com` with the query `song_name Lyrics`
* Looks if the Lyrics Page is available
    * If present , scrape the lyrics
    
