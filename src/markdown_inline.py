from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        temp_split = old_node.text.split(delimiter)
        if len(temp_split) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(len(temp_split)):
            if temp_split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(temp_split[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(temp_split[i], text_type))
        new_nodes.extend(split_nodes)
            

    return new_nodes
