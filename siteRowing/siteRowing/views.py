from django.shortcuts import render
from .forms import NameForm
from . import logic
from django.http import HttpResponseRedirect

def index(request):
    dictionary = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            sportsmanName = form.cleaned_data['sportsmanName']
            sportsmanName = (sportsmanName.title()).strip()
            accuracy, _ = logic.sporsmen_data(sportsmanName)
            if accuracy:
                id = logic.nameID(sportsmanName)
                out = HttpResponseRedirect(f'find_name?sportsmanID={id}')
                return out
            else:
                dictionary['accuracy'] = True
    else:
        form = NameForm()
    dictionary['form'] = form
    return render(request, 'home.html', dictionary)
def race(request):
    idRace = request.GET.get('raceID')
    raceData = logic.race_data(idRace)
    return render(request, 'race.html', {'raceData': raceData})
def search_sportsman(request):
    sportsmanID = request.GET.get("sportsmanID")
    sportsmanName = logic.idName(sportsmanID)
    _, sportsmanList = logic.sporsmen_data(sportsmanName)
    list200 = []
    list500 = []
    list1000 = []
    for sportsman in sportsmanList:
        if sportsman[4] == '200':
            list200.append([sportsman[-2], sportsman[5]])
        elif sportsman[4] == '500':
            list500.append([sportsman[-2], sportsman[5]])
        else:
            list1000.append([sportsman[-2], sportsman[5]])
    minList200 = []
    for minList in list200:
        if minList[0] != 'не финишировал' and minList[0] != 'не стартовали' and minList[0] != 'дисквалифицирован':
            minList200.append(float(minList[0][:str(minList[0]).find(':')])*60 +
                               float(minList[0][str(minList[0]).find(':')+1:])
                               if str(minList[0]).find(':') != -1 else float(minList[0]))
    if len(minList200) == 0:
        min200 = "Недостаточно данных"
    else:
        min200 = str(int(min(minList200)//60)) + ':' \
                 + str(round(min(minList200)%60, 3)) \
            if min(minList200)%60 > 9 \
            else (str(int(min(minList200)//60)) + ':' + '0' +
                  str(round(min(minList200)%60, 3)))
        if min200[0] == '0':
            min200 = min200[2:]
    minList500 = []
    for minList in list500:
        if minList[0] != 'не финишировал' and minList[0] != 'не стартовали' and minList[0] != 'дисквалифицирован':
            minList500.append((float(minList[0][:str(minList[0]).find(':')])*60 +
                               float(minList[0][str(minList[0]).find(':')+1:]))
                              if str(minList[0]).find(':') != -1 else float(minList[0]))
    if len(minList500) == 0:
        min500 = "Недостаточно данных"
    else:
        min500 = (str(int(min(minList500)//60)) + ':' +
                  str(round(min(minList500)%60, 3))) \
            if min(minList500)%60 > 9 \
            else (str(int(min(minList500)//60)) + ':' +
                  '0' + str(round(min(minList500)%60, 3)))
    minList1000 = []
    for minList in list1000:
        if minList[0] != 'не финишировал' and minList[0] != 'не стартовали' and minList[0] != 'дисквалифицирован':
            minList1000.append((float(minList[0][:str(minList[0]).find(':')])*60 +
                               float(minList[0][str(minList[0]).find(':')+1:]))
                               if str(minList[0]).find(':') != -1 else float(minList[0]))
    if len(minList1000) == 0:
        min1000 = "Недостаточно данных"
    else:
        min1000 =str(int(min(minList1000)//60)) + ':' + \
                 str(round(min(minList1000)%60, 3)) \
            if min(minList1000)%60 > 9 \
            else (str(int(min(minList1000)//60)) + ':' +
                  '0' + str(round(min(minList1000)%60, 3)))
    return render(request, 'search_sportsman.html', {'twoHundredList': list200, 'fiveHundredList': list500,
                                                     'thousandList': list1000,
                                                     'sportsmanName': sportsmanName, 'min200': min200,
                                                     'min500': min500, 'min1000': min1000})
def listSportsman(request):
    idList = int(request.GET.get('idList'))
    listSportsman = logic.listSportsman(idList)
    return render(request, 'listSportsman.html', {'listSportsman': listSportsman})