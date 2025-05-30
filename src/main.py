from textnode import TextNode, TextType
from copy_static import copy_files_recursive, make_public
import os
from page_generator import generate_page_recursive
import sys

content_path = "content/"
target_path = "docs/"
static_path = "static/"
template_path = "template.html"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(basepath)
    make_public(target_path)
    copy_files_recursive(static_path, target_path)
    generate_page_recursive(content_path, template_path, target_path, basepath)

main()
