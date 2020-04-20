from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import os
chromedriverpath = os.path.dirname(os.path.abspath(__file__))+'/chromedriver'

options = Options()
options.headless=True


def linkgrabber(url):
	browser = webdriver.Chrome(options=options,executable_path=chromedriverpath)
	browser.get(url)
	a=browser.find_element_by_xpath('''/html/body/div[3]/div/div[9]/center/div/a[2]''')
	return(a.get_attribute('href'))
	browser.close()
	browser.quit()

def episodecounter(url):
	browser = webdriver.Chrome(options=options,executable_path=chromedriverpath)
	browser.get(url)
	a=browser.find_element_by_xpath('''/html/body/select/option[1]''')
	ok=a.get_attribute('value')
	epno=re.findall('\d+',ok)
	return(epno[-1])
	browser.close()
	browser.quit()






url=input("Enter chia-anime url of anime\nEg: http://www.chia-anime.me/episode/blade/\nEg: https://m.chia-anime.me/show/blade/\n:")

start=int(input("Enter starting episode no:"))
end=int(input("Enter ending episode no:"))
asktosaveinfile=input("Do you want to save links in a file?\nEnter Y or N:")
if asktosaveinfile == 'Y':
	filename=input("Enter filename:")






if 'www.' in url:
	animenamere=re.findall('episode\/(.*)',url)
	animename=animenamere[0]
	if animename[-1] == '/':
		animename=animename.replace('/','')

elif 'm.' in url:
	animenamere=re.findall('show\/(.*)',url)
	animename=animenamere[0]
	if animename[-1] == '/':
		animename=animename.replace('/','')

epcheckurl='https://m.chia-anime.me/show/'+animename
totaleps=int(episodecounter(epcheckurl))
if end > totaleps:
	print("Sorry your ending episode number exceeds the total number of episodes")
	quit()

eplist=[]
print("\n")
for i in range(start,(end+1)):
	episodeurl='https://m.chia-anime.me/view/'+animename+'-episode-'+str(i)
	link=linkgrabber(episodeurl)
	print('\033[31m')
	print(link)
	eplist.append(link)

if asktosaveinfile == 'Y':
	eps='\n'.join(eplist)
	f=open(filename,'w+')
	f.write(eps)
	f.close()








