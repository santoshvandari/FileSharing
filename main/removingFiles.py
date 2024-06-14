from pathlib import Path
import os
from core.settings import BASE_DIR


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


# Remove all the Expired Files 
def RemoveAllExpiredFiles():
    pass
