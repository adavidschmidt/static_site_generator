from textnode import TextNode, TextType
import os
import shutil

def copy_static():
	pass
def get_static_files(current_filetree, current_path):
	file_paths = []
	for dir, content in current_filetree.items():
		new_path = f"{current_path}/{dir}"
		if content is None:
			file_paths.extend(new_path)
		else:
			file_paths.extend(get_static_files(content, new_path))
	return file_paths

def main():
	if not os.path.exists("public/"):
		os.mkdir("public")
	else:
		print("exists")
	#to run at the end of the function to copy the items from the directory.
	#shutil.rmtree("static/")

main()
