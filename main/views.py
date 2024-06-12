from django.shortcuts import render,HttpResponse,redirect
from main.models import SharedFiles
from main.slugGenerator import slug_generator,fileid

# Create your views here.
def home(request):
    if request.method=='POST':
        file=request.FILES['file']
        filename=file.name
        if '.' in filename:
            filename=filename.split('.')[0]
        slug=slug_generator(filename)
        fileno=fileid()
        print(slug,fileno)
        print(filename)
        try:
            SharedFiles.objects.create(file=file,filename=filename,slug=slug,fileid=fileno)
            successdata={
                'status':'success',
                'slug':slug,
                'fileid':fileno
            }
            print(successdata)
            return render(request,'index.html',successdata)
        except Exception as ex:
            print(ex)
            successdata={
                'status':'error',
                'message':'Something went wrong.'
            }
            print(successdata)
            return render(request,'index.html',successdata)
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