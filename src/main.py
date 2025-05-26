from textnode import TextNode, TextType
import os
import shutil


def make_public():
	if not os.path.exists("public"):
		os.mkdir("public")

def get_path_files(path):
	return os.listdir(path)

def get_static_files(path_files, current_path):
	file_paths = []
	for item in path_files:
		item_path = f"{current_path}/{item}"
		if os.path.isfile(item_path):
			file_paths.append(item_path)
		else:
			file_paths.append(item_path)
			file_paths.extend(get_static_files(os.listdir(item_path), item_path))
	return file_paths

def copy_files(source_items, target_directory):
	for item in source_items:
		if os.path.isfile(item):
			shutil.copy(item, target_directory)
		else:
			directory = item.strip("static")
			os.mkdir(f"{target_directory}/{directory}")

def main():
	make_public()
	if os.path.exists("static/"):
		path_files = get_path_files("static/")
	else:
		raise Exception("static directory does not exist")
	static_files = get_static_files(path_files, "static")
	copy_files(static_files, "public/")
	#to run at the end of the function to copy the items from the directory.
	#shutil.rmtree("static/")

main()
