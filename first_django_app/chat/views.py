from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect #render is imported to generate an HTML file using a template and data
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
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        redirect_to = request.POST.get('redirect_to')
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect(redirect_to)
        else:
            return render(request, 'chat/login.html', {'wrongPassword': True, 'redirect_to': redirect_to})
    return render(request, 'chat/login.html', {'redirect_to': redirect_to})

def registerUser(request):
    return()