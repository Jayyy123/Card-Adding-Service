from wsgiref.util import request_uri
from django.shortcuts import render


def base(request):

    return render(request, 'cardBase/home.html')


# def base(request):
