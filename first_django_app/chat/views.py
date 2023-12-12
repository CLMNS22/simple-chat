from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render #render is imported to generate an HTML file using a template and data
from .models import Chat, Message

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print('received data' + request.POST['messageText'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['messageText'], chat=myChat, author=request.user, receiver=request.user)
    
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {"messages": chatMessages})

def userLogin(request):
    redirect = request.POST.get('next')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect(redirect)
        else:
            return render(request, 'chat/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'chat/login.html', {'redirect': redirect})