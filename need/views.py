from django.shortcuts import render

# Create your views here.
def nindex(request):
    return render(request,'nindex.html')