from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("#"):
            line_split = line.split(" ", 1)
            if len(line_split[0]) == 1:
                return line_split[1]
            else:
                continue
    raise ValueError("title does not exist")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md = f.read()
    html = markdown_to_html_node(md).to_html()
    with open(template_path) as t:
        template = t.read()
        
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(template)
        
def generate_page_recursive(source_path, template_path, destination_path, basepath):
    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        to_path = os.path.join(destination_path, filename)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, to_path.replace(".md", ".html"), basepath)
        else:
            generate_page_recursive(from_path, template_path, to_path, basepath)