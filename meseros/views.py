from django.shortcuts import render

# Create your views here.
def meseros(request):

    return render(request, 'meseros/meseros.html')