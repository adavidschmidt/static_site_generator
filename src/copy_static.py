import os
import shutil


def make_public(dest_target):
	if os.path.exists(dest_target):
		shutil.rmtree(dest_target)
	os.mkdir(dest_target)

def copy_files_recursive(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    
    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        to_path = os.path.join(destination_path, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)