from textnode import TextNode, TextType
from copy_static import get_path_files, get_static_files, copy_files, make_public
import os

def main():
	make_public()
	if os.path.exists("static/"):
		path_files = get_path_files("static/")
	else:
		raise Exception("static directory does not exist")
	static_files = get_static_files(path_files, "static")
	copy_files(static_files, "public")
 
 
main()
