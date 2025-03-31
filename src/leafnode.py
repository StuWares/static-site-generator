from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        leaf_node = ""
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        
        if self.tag == None:
            return self.value
        
        if self.props == None:
            leaf_node = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            leaf_node = F"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return leaf_node

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"