import os
import tempfile
from django.core.files import File
from django.conf import settings

def save_as_symlink(abs_pth, name, generic_file_obj, data_file_field_name='data_file'):
    """ Takes a :class:`gfiles.models.GenericFiles` object and saves a symlink of the file to the absolute path
     (abs_pth).

     Can also work with any model class that has FileField named with the data_file_field_name variable

    :param abs_pth: path to the file to symlink to
    :param name: Name to save to the file as
    :param generic_file_obj: :class:`gfiles.models.GenericFiles` object

    :returns: updated :class:`gfiles.models.GenericFiles` object with symlink

    """
    tf = tempfile.NamedTemporaryFile(delete=False)

    # first create link to empty file
    getattr(generic_file_obj, data_file_field_name).save(name, File(open(tf.name)))

    fpth = os.path.join(settings.MEDIA_ROOT, getattr(generic_file_obj, data_file_field_name).name)
    os.remove(fpth)
    os.symlink(abs_pth, fpth)
    generic_file_obj.save()
    tf.close()

    return generic_file_obj

