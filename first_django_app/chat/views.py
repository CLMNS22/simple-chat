# from django.shortcuts import render
# from .models import Chat, Message

# # Create your views here.
# def index(request):
#     if request.method == 'POST':
#         print('received data' + request.POST['messageText'])
#         myChat = Chat.objects.get(id=1)
#         Message.objects.create(text=request.POST['messageText'], chat=myChat, author=request.user, receiver=request.user)
#         chatMessages = Message.objects.filter(chat__id=1)
#     return render(request, 'chat/index.html', {"message": chatMessages})

from django.shortcuts import render
from .models import Chat, Message

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('received data' + request.POST['messageText'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['messageText'], chat=myChat, author=request.user, receiver=request.user)
    
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {"messages": chatMessages})
