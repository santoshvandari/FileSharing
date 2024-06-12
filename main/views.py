from django.shortcuts import render,HttpResponse,redirect
from main.models import SharedFiles
from main.slugGenerator import slug_generator,fileid

# Create your views here.
def home(request):
    if request.method=='POST':
        file=request.FILES['file']
        filename=file.name
        slug=slug_generator(filename)
        fileid=fileid()
        print(slug,fileid)
        SharedFiles.objects.create(file=file,filename=filename,slug=slug,fileid=fileid)
        return render(request,'index.html',{'slug':slug})
    return render(request,'index.html')



def download(request):
    return render(request,'download.html')



def custom404(request):
    return render(request,'404.html')

def fileDownload(request,slug):
    if not slug:
        return redriect("/404")
    if slug:
        file=SharedFiles.objects.filter(sulg=slug)[0]
        if not file:
            return redirect("/404")
        else:
            return HttpResponse("File Found Successfully.")
    return redirect('/404')