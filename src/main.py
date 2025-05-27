from textnode import TextNode, TextType
from copy_static import copy_files_recursive, make_public
import os
from page_generator import generate_page_recursive
import sys

def main():
    basepath = sys.argv[0]
    make_public()
    copy_files_recursive("static", "public")
    generate_page_recursive("content", "template.html", basepath)

main()
