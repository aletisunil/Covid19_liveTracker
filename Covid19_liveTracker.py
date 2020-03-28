import requests
import bs4

country_name=input("Enter the Country name: ")

def covid19(country):
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    data=soup.select('tr td')
    for i in range(len(data)):
        if data[i].text.lower()==country.lower():
            index=i
            break
    
    for i in range(7):
        if i == 0:
            print("Country name: "+str(data[i+index].text))
        elif i == 1:
            print("Total cases: "+str(data[i+index].text))
        elif i == 2:
            print("New cases: "+str(data[i+index].text))
        elif i == 3:
            print("Total deaths: "+str(data[i+index].text))
        elif i == 4:
            print("New deaths: "+str(data[i+index].text))
        elif i == 5:
            print("Total Recovered: "+str(data[i+index].text))
        elif i == 6:
            print("Active cases: "+str(data[i+index].text),end='\n\n')
covid19(country_name)
