import os
import random
import string
import base64

def get_random_string(length=8):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def get_available_filepath(filepath):
	dir_name, file_name = os.path.split(filepath)
	file_root, file_ext = os.path.splitext(file_name)
	while os.path.exists(filepath):
		filepath = os.path.join(dir_name, "%s_%s%s" % (file_root, get_random_string(7), file_ext))
	return filepath


def get_tmp_dir():
    curr_dir = os.getcwd()
    TMP_DIR = os.path.join(curr_dir, 'tmp')
    os.makedirs(TMP_DIR, exist_ok=True)
    return TMP_DIR


def file2base64(filepath):
    with open(filepath, 'rb') as file:
        base64_str = base64.b64encode(file.read())  # base64类型
        return base64_str.decode('utf-8')  # str
