from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'post_list.html', {})

def laura(request):
    texto = {'domingo': 'infelizmente hoje é domingo'}
    return render(request, 'laura.html', texto)

