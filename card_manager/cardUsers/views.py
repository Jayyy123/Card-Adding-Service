from django.shortcuts import render

def authentication(request):
    return render(request, 'cardUsers/authentication.html')

def login_page(request):
    return render(request, 'cardUsers/login.html')

def signup_page(request):
    return render(request, 'cardUsers/signup.html')

def account(request):
    return render(request, 'cardUsers/account.html')

