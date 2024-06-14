from pathlib import Path
import os
from core.settings import BASE_DIR
from main.models import SharedFiles


# Remove all the Expired Files 
def RemoveAllExpiredFiles():
    files=SharedFiles.objects.all()
    for file in files:
        if file.is_expired():
            file.delete()
            RemoveFile(file.filename)
    return True

# Remove a file from the server
def RemoveFile(filename):
    filelocation=BASE_DIR / "media/uploads/" / filename
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