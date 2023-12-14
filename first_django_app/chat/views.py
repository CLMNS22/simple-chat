from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect #render is imported to generate an HTML file using a template and data
from .models import Chat, Message
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages

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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Use the 'next' parameter from the query string if available
            redirect_to = request.POST.get('redirect_to') or redirect_to

            # Redirect to the 'next' URL if it's provided
            if redirect_to:
                return redirect(redirect_to)
            else:
                # Redirect to a default URL if 'next' is not provided
                return redirect('chat')  # Change 'home' to the name of your home or dashboard view
        else:
            return render(request, 'chat/login.html', {'wrongPassword': True, 'redirect_to': redirect_to})

    return render(request, 'chat/login.html', {'redirect_to': redirect_to})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process form data and create a new user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                # Create a new user
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account created successfully. You can now log in.')
                return redirect('login')  # Redirect to the login page
            else:
                messages.error(request, 'Passwords do not match.')
    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'form': form})


def userLogout(request):
    logout(request)
    return redirect('login')