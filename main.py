import requests
from bs4 import BeautifulSoup
import sqlite3
con = sqlite3.connect('rowing.db')
cur = con.cursor()
c = 1
cRace = 0
listPlaers = []
while True:
    if cRace >= 50:
        break
    link = f'https://results.imas-sport.com/russia/race.php?competition=wettkampf_518&race_id={c}'
    a = requests.get(link)
    soup = BeautifulSoup(a.text, 'lxml')
    if str(soup.text)[:4] == 'No i':
        cRace += 1
    else:
        help = str((soup.find("div", id="table_renn_header_raceclass")).text)
        raceClassHelp = help[:].lower()
        if raceClassHelp.find('k') == -1 and raceClassHelp.find('к') == -1:
            raceClassHelpNomber = raceClassHelp.find('c')
            if raceClassHelpNomber == -1:
                raceClassHelpNomber = raceClassHelp.find('с')
        else:
            raceClassHelpNomber = raceClassHelp.find('k')
            if raceClassHelpNomber == -1:
                raceClassHelpNomber = raceClassHelp.find('к')
        raceClass = raceClassHelp[raceClassHelpNomber:raceClassHelp.find(' ', raceClassHelpNomber+1)]
        raceClass = 'к'+raceClass[1:] if raceClass[0] == 'k' else 'c'+raceClass[1:]
        race = (soup.title).text
        raceDistance = raceClassHelp[raceClassHelp.find(' ', raceClassHelp.rfind('00')-5)+1:raceClassHelp.rfind('00')+2]
        if raceClass[-1] == '1' and raceDistance != '5000':
            competition = soup.find('div', id="table_regatta_header_name").text
            allDataStart = soup.find_all('tr')
            raceID = link[link.rfind('=') + 1:]
            dataRace = str(soup.find("div", id="table_renn_header_start"))[str(soup.find("div", id="table_renn_header_start")).find(',')+2:str(soup.find("div", id="table_renn_header_start")).find('-')-1]
            allDataStarts = []
            for date in allDataStart[1:]:
                if len(date) != 3:
                    allDataStarts.append(date)
            for DataStarts in allDataStarts:
                try:
                    Starts = DataStarts.find_all('td')
                    sportsman = str(Starts[3].find('td').text)
                    sportsmanID = sportsman[:sportsman.find('-') - 1]
                    if sportsman.find('(') == -1:
                        sportsmanName = sportsman[sportsman.find('-') + 2:]
                    else:
                        sportsmanName = sportsman[sportsman.find('-') + 2:sportsman.find('(') - 1]
                    coach = str(Starts[3].find('b').text)[2:]
                    rank = Starts[0].text
                    finish = Starts[-1].text
                    #print(f'{competition}\n{race}\n{raceClass}\n{raceID}\n{link}\n{sportsmanID}\n{sportsmanName}\n{coach}\n{rank}\n{finish}')
                    listPlaers.append((competition, race, raceClass, raceID, raceDistance, dataRace, link, sportsmanID, sportsmanName, coach, rank, finish))
                except:
                    print(1)
    c += 1
cur.executemany("INSERT INTO rowingFor1 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", listPlaers)
con.commit()