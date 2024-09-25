import requests

def get_joke():
    request = "https://api.chucknorris.io/jokes/random"
    # need to pip install urllib3==1.26.6 to avoid error
    response = requests.get(request).json()
    return response["value"]

while True:
    user_input = input("Haluatko kuulla Chuck Norris -vitsin? [y/n] ")
    if user_input.lower()== "n":
        print("Selvä, lopetetaan")
        break
    print(get_joke())
