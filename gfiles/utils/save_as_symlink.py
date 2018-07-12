import os
import tempfile
from django.core.files import File
from django.conf import settings

def save_as_symlink(abs_pth, name, file_data_obj):
    tf = tempfile.NamedTemporaryFile(delete=False)

    # first create link to empty file
    file_data_obj.data_file.save(name, File(open(tf.name)))

    fpth = os.path.join(settings.MEDIA_ROOT, file_data_obj.data_file.name)
    os.remove(fpth)
    os.symlink(abs_pth, fpth)
    file_data_obj.save()
    tf.close()

    return file_data_obj