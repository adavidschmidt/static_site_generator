
class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		if not self.props:
			return ""
		attrib_string = ""
		for key, value in self.props.items():
			attrib_string += f' {key}="{value}"'
		return attrib_string

	def __repr__(self):
		return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if not self.value:
			raise ValueError("invalid HTML: missing value")
		if not self.tag:
			return self.value
		return f"<{self.tag}>{self.value}</{self.tag}>"

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        html = ""
        if not self.tag:
            raise ValueError("invalid HTML: missing tag")
        if not self.children:
            raise ValueError("invalid HTML: no children")
        for node in self.children:
            html += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
