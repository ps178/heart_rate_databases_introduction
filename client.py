import requests


R1 = requests.post("http://vcm-3584.vm.duke.edu:5000/api/heart_rate", json = {"user_email": "ps178@duke.edu", "user_age": 22, "heart_rate": 90})


R2 = requests.get("http://vcm-3584.vm.duke.edu:5000/api/heart_rate/ps178@duke.edu")
#name = R2.json()

R3 = requests.get("http://vcm-3584.vm.duke.edu:5000/api/heart_rate/average/ps178@duke.edu")
#hello = R3.json()

#R4 = requests.post("http://vcm-3584.vm.duke.edu:5000/api/heart_rate/interval_average", json={"user_email": "", "heart_rate_average_since": ""})

#print(name, hello)


