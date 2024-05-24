import os
import tempfile
import shutil


def create_temporary_copy(src_file_name, preserve_extension=False):
    """
    Copies the source file into a temporary file.
    Returns a _TemporaryFileWrapper, whose destructor deletes the temp file
    (i.e. the temp file is deleted when the object goes out of scope).
    """
    tf_suffix = ""
    if preserve_extension:
        _, tf_suffix = os.path.splitext(src_file_name)
    tf = tempfile.NamedTemporaryFile(suffix=tf_suffix)
    shutil.copy2(src_file_name, tf.name)
    return tf
