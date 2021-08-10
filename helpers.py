import os
import shutil
from datetime import datetime

def create_custom_folder(ppt_basename, basedir = "tmp"):
    # Get names
    timestamp_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # Create a name for the folder
    custom_path = "./" + basedir + "/" + timestamp_str + "-" + ppt_basename
    # Create the folders
    os.mkdir(custom_path)
    for subdir in ["/ppt","/ipynb","/zip","/ipynb/images"]:
        os.mkdir(custom_path + subdir)
    return custom_path

def make_archive(source, destination):
   base = os.path.basename(destination)
   name = base.split('.')[0]
   format = base.split('.')[1]
   archive_from = os.path.dirname(source)
   #archive_to = os.path.dirname(destination)
   #print(archive_to, "archive_to")
   archive_to = os.path.basename(source.strip(os.sep))
   print(source, destination, archive_from, archive_to)
   shutil.make_archive(name, format, archive_from, archive_to)
   shutil.move('%s.%s'%(name,format), destination)