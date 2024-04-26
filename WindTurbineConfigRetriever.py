import requests
import time
api_url = "https://script.google.com/macros/s/AKfycbwzXfRARanEuxoCskvrlvdpS6xLiDPwpBVfhRCMydUqCNaG5gsLhyD07oH4gHyeh0pS/exec"
while True:
    response = requests.get(api_url)
    config = response.json()
    print(config)
    with open("WindTurbineConfig.txt", "w") as file:
        file.write(config)
    time.sleep(30)