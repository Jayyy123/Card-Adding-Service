from django.shortcuts import render

def base(request):
    return render(request, 'card_base/home.html')
