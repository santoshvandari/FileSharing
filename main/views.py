from django.shortcuts import render,HttpResponse,redirect
from main.models import SharedFiles
from main.slugGenerator import slug_generator,fileid
import os
from core.settings import BASE_DIR
# Create your views here.
def home(request):
    if request.method=='POST':
        file=request.FILES['file']
        fullfilename=file.name
        if '.' in fullfilename:
            filename=fullfilename.split('.')[0]
        slug=slug_generator(filename)
        fileno=fileid()
        try:
            SharedFiles.objects.create(file=file,filename=fullfilename,slug=slug,fileid=fileno)
            successdata={
                'status':'success',
                'slug':'http://127.0.0.1:8000/d/'+slug,
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
        file=SharedFiles.objects.filter(slug=slug).first()
        if not file:
            return redirect("/404")
        elif file.is_expired():
            # remove from teh datbase and the file from the server
            file.delete()
            if os.path.exists(BASE_DIR+"/media/uploads/"+str(file.filename)):
                print(BASE_DIR+"/media/uploads/"+str(file.filename))
                os.remove(BASE_DIR+"/media/uploads/"+str(file.filename))
        else:
            file.file.open()
            response=HttpResponse(file.file, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename=%s' % file.filename
            return response
    else:
        return redirect("/404")


    return redirect('/404')