import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_props(self):
        node = LeafNode("h1", "Title", {"class": "section-heading"})
        self.assertEqual(node.to_html(), '<h1 class="section-heading">Title</h1>')

    def test_leaf_to_html_multi_props(self):
        node = LeafNode("h1", "Title", {"class": "section-heading","id": "main-heading"})
        self.assertEqual(node.to_html(), '<h1 class="section-heading" id="main-heading">Title</h1>')

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )