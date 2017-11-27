from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def user_login(request):        
    if request.method == 'POST':            
        form = LoginForm(request.POST)            
        if form.is_valid():                
            cd = form.cleaned_data                
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:                    
                if user.is_active:                        
                    login(request, user)                        
#                    return HttpResponse('Authenticated successfully')
                    return HttpResponseRedirect('/cmdb/index/')
                else:                        
                    return HttpResponse('Disabled account')
        else:            
            return HttpResponse('Invalid login')        
    else:            
        form = LoginForm()        
        return render(request, 'login.html', {'form': form})
    

def index(request):
    return render(request, 'index.html')
