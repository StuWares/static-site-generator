from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a HTML tag")
        
        if self.children is None:
            raise ValueError("Parent nodes must have at least one child node")
        
        children_string = ""
        parent_props = self.props_to_html()

        for c in self.children:
            children_string += c.to_html()

        return f"<{self.tag}{parent_props}>{children_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"