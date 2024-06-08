from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=='POST':
        pass
    return render(request,'index.html')





def custom404(request):
    return render(request,'404.html')

def fileDownload(request):
    pass