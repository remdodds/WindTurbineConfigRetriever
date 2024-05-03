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
    

    for imageURL in imageUrlsList:
        urllib.request.urlretrieve(imageURL[1], folderPath /  imageURL[0])
    

    with open("WindTurbineConfig.txt", "w") as file:
        file.write(str(config))
    time.sleep(30)