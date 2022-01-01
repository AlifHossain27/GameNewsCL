import requests
from simple_term_menu import TerminalMenu
import webbrowser

def GameNews():
  # Getting the game news data
  data=[]

  # Getting Options
  options=['Quit']

  resp=requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=15&maxlength=300&format=json")

  articles=resp.json()["appnews"]["newsitems"]

  # Getting the game news title and url in json and appending to the data list
  for article in articles:
    title=article["title"]
    url=article["url"]
    json_data={
      title:url
    }
    data.append(json_data)
    
    # Adding Options
    options.append(title)
  
  mainMenu=TerminalMenu(options)
  quitting=False

  # Functionality of the Options
  while quitting ==False:
    optionsIndex=mainMenu.show()
    optionsChoice=options[optionsIndex]
    if optionsChoice=='Quit':
      quitting=True
    for option in data:
      key, value = list(option.items())[0]
      if key == optionsChoice:
        print(value)
        webbrowser.open(value, new=0, autoraise=True)
        quitting =True
      else:
        pass


# Executing the Function
if __name__=="__main__":
    GameNews()
