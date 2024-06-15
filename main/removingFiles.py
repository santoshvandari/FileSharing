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
                file.delete()
                pass
    return True

# Remove a file from the server
def RemoveFile(filename):
    filelocation=str(BASE_DIR) + "/media/" + str(filename)
    if os.path.exists(filelocation):
        try:
            os.remove(filelocation)
            return True
        except Exception as ex:
            print(ex)
            return False
    else:
        return True
    return True