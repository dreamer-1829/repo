from django.shortcuts import render
# Create your views here.

# homepage landing page
def homepage(request):
    return render(request,'home.html')

# another page
def secondpage(request):
    return render(request,'second.html')