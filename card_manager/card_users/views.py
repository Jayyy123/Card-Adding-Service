from django.shortcuts import redirect, render

def account(request):
    return render(request, 'card_users/account.html')

def edit_account(request):
    return render(request, 'card_users/edit_account.html')

def login_user(request):
    return render(request, 'card_users/login_page.html')

def logout_user(request):
    return redirect('login')

def signup_user(request):
    return render(request, 'card_users/signup_page.html')
