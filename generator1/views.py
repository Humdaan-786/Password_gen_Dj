from random import random
from django.shortcuts import render
import random
# Create your views here.
# views can be used to send infomation like dictionary to html pages that value can bea accesed 
#like {{password}}
def home(request):
    return render(request,'generator1/home.html')
def about(request):
    return render(request,'generator1/about.html')



def password(request):
    thepassword=''
    characters=list('abcdefghijklmnopqrsuvwxyz')
    length=int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('speacial'):
        characters.extend(list('!@#$%^&*_:;'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
        
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator1/password.html',{'password':thepassword})