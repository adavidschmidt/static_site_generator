import os
import shutil


def make_public():
	if os.path.exists("public"):
		shutil.rmtree("public")
	os.mkdir("public")

def get_path_files(path):
	return os.listdir(path)

def get_static_files(path_files, current_path):
	file_paths = []
	for item in path_files:
		item_path = os.path.join(current_path, item)
		if os.path.isfile(item_path):
			file_paths.append(item_path)
		else:
			file_paths.extend(get_static_files(get_path_files(item_path), item_path))
	return file_paths
		
def copy_files(files, target):
    for item in files:
        target_path = os.path.join(target, item.removeprefix('static/'))
        dir_names = os.path.dirname(target_path)
        if os.path.exists(dir_names):
            shutil.copy(item, target_path)
        else:
            os.makedirs(dir_names)
            shutil.copy(item, target_path)
