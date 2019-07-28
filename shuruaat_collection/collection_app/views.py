from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'collection_app/index.html')
