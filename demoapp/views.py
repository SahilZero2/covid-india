from django.shortcuts import render
from covid_india import states
# Create your views here.
# def home(request):
#     return render(
#           request ,
#          'home.html'
#           {
#               'title':'Home page'
#           }
#     ) 


def home(request):
    data = states.getdata('Total')
    data['Total'] = int(data['Active']) + int(data['Cured']) + int(data['Death'])
    return render(request,'home.html',{'data':data})