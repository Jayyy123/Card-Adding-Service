from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_overview(request):
    
    links = {
        'api_overview':'/account/',
    }
    return Response(links)