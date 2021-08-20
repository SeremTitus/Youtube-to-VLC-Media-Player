import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def getingYtubevid(url):
   options = Options()
   options.add_experimental_option("excludeSwitches", ["enable-automation"])
   options.add_experimental_option('useAutomationExtension', False)
   driver = webdriver.Chrome(driverpath, options=options)
   driver.get(url)
   time.sleep(5)
   height = driver.execute_script("return document.documentElement.scrollHeight")
   lastheight = 0
   while True:
      if lastheight == height:
         break
      lastheight = height
      driver.execute_script("window.scrollTo(0, " + str(height) + ");")
      time.sleep(10)
      height = driver.execute_script("return document.documentElement.scrollHeight")

   user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
   f =[]
   for i in user_data:
      link = (i.get_attribute('href'))
      f.append(str(link))
   driver.quit()
   return f
def xspfWriter(fileName,location = []):
   #annotation = title
   #var
   numbTrack = len(location)
   path =fileName + '.xspf'
   docIntro = '<?xml version="1.0" encoding="UTF-8"?>\n<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\n	<title>Playlist</title>\n	<trackList>\n'
   #create file
   file = open(path,'w')
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
      file = open(path,'a')
      file.write(trackConstruct)
      file.close()
      count += 1   
   playlistClose = '	</trackList>\n</playlist>\n'
   file = open(path,'a')
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