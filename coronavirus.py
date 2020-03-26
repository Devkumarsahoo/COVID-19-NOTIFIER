from plyer import notification
from bs4 import BeautifulSoup
import requests
import time


def notifyme(title,message):
	notification.notify(title=title,
		message=message,
		app_icon="C:\\Users\\SEBIHO\\Desktop\\download.ico")

def getdata(url):
	r=requests.get(url)
	return r.text


if __name__ == '__main__':
	while True:
	#notifyme("dev","coronavirus Alert!!") 	
		myHtmldata=getdata('https://www.mohfw.gov.in/') #use url to scrap the data
		myDataStr=""
		soup = BeautifulSoup(myHtmldata, 'html.parser')
		
		
		for tr in soup.find_all('tbody')[7].find_all('tr'):
			myDataStr+=tr.get_text()
		myDataStr=myDataStr[1:]
		itemList=myDataStr.split("\n\n")

		states=['Kerala','Maharashtra'] #enter the the states u want to display.
		for item in itemList[0:26]:
			dataList=item.split('\n')
			if dataList[1] in states:
				ntitle="Cases of Covid-19"
				ntext=f"{dataList[1]}\nIndian:{dataList[2]}\nForeign:{dataList[3]}\nCured:{dataList[4]}    Death:{dataList[5]}"
				notifyme(ntitle,ntext)
				print(dataList)
		time.sleep(3600)#after 1 hour u wil be notified

	