import requests
import time
from pathlib import Path
import urllib.request
api_url = "https://script.google.com/macros/s/AKfycbwzXfRARanEuxoCskvrlvdpS6xLiDPwpBVfhRCMydUqCNaG5gsLhyD07oH4gHyeh0pS/exec"
while True:
    response = requests.get(api_url)
    config = response.json()
    print(config)
    imageUrlsList = config["imageURLs"]

    #Set up the images folder
    folderPath = Path("images")
    folderPath.mkdir(exist_ok=True)
    
    # Get local images
    localImageList = []
    for file in folderPath.iterdir():
        if file.is_file():
            localImageList.append(file.name)
    serverImageList = []
    #Download images that are not already stored localy
    for image in imageUrlsList:
        imageFileName = image[0]
        imageURL = image[1]
        serverImageList.append(imageFileName)
        if(imageFileName not in localImageList):
            print("fetching " + imageFileName)
            urllib.request.urlretrieve(imageURL, folderPath /  imageFileName)
    #cleanup local images that are no longer in the google drive
    for localImage in localImageList:
        if(localImage not in serverImageList):
            Path.unlink(folderPath / localImage)
        

    with open("WindTurbineConfig.txt", "w") as file:
        file.write(str(config))
    time.sleep(30)