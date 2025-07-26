from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'birthday_app/home.html')

def vuvu_note(request):
    return render(request, 'birthday_app/vuvu.html')

def chhawi_note(request):
    return render(request, 'birthday_app/chhawi.html')

def vandu_note(request):
    return render(request, 'birthday_app/vandu.html')

def gifts(request):
    return render(request, 'birthday_app/gifts.html')

