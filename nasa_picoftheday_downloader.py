import nasapy
import os
from datetime import datetime
import urllib.request
from IPython.display import Image, display

ky = "DEMO_KEY"
nasa = nasapy.Nasa(key = ky)
day = datetime.today().strftime('%Y-%m-%d')
picoftheday = nasa.picture_of_the_day(date = day, hd = True)

if(picoftheday["media_type"] == "image"):
	if("hdurl" in picoftheday.keys()):
		title = day + picoftheday["title"].replace(" ", "_").replace(":","_") + ".jpg"
		dir_img = "./APOD"
		dir_res = os.path.exists(dir_img)
		if (dir_res==False):
			os.makedirs(dir_img)
		else:
			print("Given directory exists!\n")
		urllib.request.urlretrieve(url = picoftheday["hdurl"], filename = os.path.join(dir_img,title))
		
		if("date" in picoftheday.keys()):
			print("The date the picture was posted: ", picoftheday["date"])	
		display(Image(os.path.join(dir_img,title)))	
else:
	print("Sorry, but given file type is not available.")		