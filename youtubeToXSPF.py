from ast import Pass
import os
import sys
from selenium.webdriver.common.by import By
from easySelenium import easySelenium

def getingYtubevid(url):
   chrome= easySelenium(True)
   chrome.open(url)
   chrome.scroll()
   youtubeHyperlinks:list=[]
   i:int = 1
   while True:
      pass
      try:
         link = str(chrome.browser.find_element(By.XPATH,'//*[@id="items"]/ytd-grid-video-renderer['+str(i)+']//*[@id="video-title"]').get_attribute('href'))
         youtubeHyperlinks.append(link)
         i += 1
      except:
         break
   chrome.free()
   return youtubeHyperlinks
def xspfWriter(fileName,location = []):
   #annotation = title
   #var
   numbTrack = len(location)
   path =fileName + '.xspf'
   docIntro = '<?xml version="1.0" encoding="UTF-8"?>\n<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\n	<title>Playlist</title>\n	<trackList>\n'
   #create file
   file = open(os.path.join(sys.path[0], path),'w')
   file.write(docIntro)
   file.close()   
   #create tracks
   count = 0
   while count < numbTrack:
      r =''
      for i in location[count]:
         if i == '&':
            location[count]=r
            break
         r += i

      #write
      trackConstruct ='		<track>\n			<location>'+ location[count] + '</location>\n			<extension application="http://www.videolan.org/vlc/playlist/0">\n				<vlc:id>'+ str(count) +'</vlc:id>\n			</extension>\n		</track>\n'
      file = open(os.path.join(sys.path[0], path),'a')
      file.write(trackConstruct)
      file.close()
      count += 1   
   playlistClose = '	</trackList>\n</playlist>\n'
   file = open(os.path.join(sys.path[0], path),'a')
   file.write(playlistClose)
   file.close()


   #print
   print('\nTotal Videos present:'+ str(numbTrack))



#user_specific
driverpath = 'F://applications//active//chromedriver_win32//chromedriver.exe'
print('DO NOT try on youtube home page and video play pages(.com/watch?...) --Due to the infinite nature')
print('MADE for playlists(.com/playlist?list=...) and Channel Pages')
url = input('Youtube url:') or 'https://www.youtube.com/channel/UCX0CsAlmdzNBPcUR2hwgMAA'
filename = input('Name your output file:') or 'try'
list = getingYtubevid(url)
xspfWriter(filename,list)