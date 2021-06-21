from django.shortcuts import render
from covid_india import states
# Create your views here.

def covidstate(request,state):
    data = states.getdata(state.title())
    data['Total'] = int(data['Active']) + int(data['Cured']) + int(data['Death'])
    return render(request,
        'covid.html' ,
        {
            'title' : 'COVID' + state.upper(),
            'data' : data

        }
    
    )
