from pathlib import Path
import os
from core.settings import BASE_DIR
from main.models import SharedFiles


# Remove all the Expired Files 
def RemoveAllExpiredFiles():
    files=SharedFiles.objects.all()
    for file in files:
        if file.is_expired():
            if(RemoveFile(file.file)):
                # file.delete()
                print("FIle Deleted Succcessfully")
    return True

# Remove a file from the server
def RemoveFile(filename):
    print("File Name :" + str(filename))
    filelocation=BASE_DIR / "media/" / filename
    print(filelocation)
    if os.path.exists(filelocation):
        print(filelocation)
        try:
            os.remove(filelocation)
            return True
        except Exception as ex:
            print(ex)
            return False
    else:
        return True
    return True