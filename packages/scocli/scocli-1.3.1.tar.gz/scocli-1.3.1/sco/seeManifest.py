#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def print_manifest_tree(manifest_path, indent=0):
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    print_element(root, indent, [])

def print_element(element, indent, ancestors):
    tag = element.tag.split("}")[1] if "}" in element.tag else element.tag
    value = element.text.strip() if element.text else None

    if tag == "organization":
        identifier = element.attrib.get("identifier", "")
        print(" " * indent + f"organization {identifier}")
    elif tag == "title" and ancestors and ancestors[-1].tag.split("}")[1] == "organization":
        print(" " * indent + f"title: {value}")
    elif tag == "item":
        identifier = element.attrib.get("identifier", "")
        identifierref = element.attrib.get("identifierref", "")
        print(" " * indent + f"item {identifier}")
        for child in element:
            if child.tag.split("}")[1] == "title":
                title = child.text.strip() if child.text else ""
                print(" " * (indent + 2) + f"title: {title}")
        print(" " * (indent + 2) + f"linked resource identifier: {identifierref}")
    elif tag == "resource":
        identifier = element.attrib.get("identifier", "")
        href = element.attrib.get("href", "")
        print(" " * indent + f"resource identifier: {identifier}")
        print(" " * (indent + 2) + f"Main file: {href.split('/')[-1]}")

    for child in element:
        print_element(child, indent + 2, ancestors + [element])

def main():
    manifest_path = "imsmanifest.xml"  # Change this to the path of your imsmanifest.xml file
    print_manifest_tree(manifest_path)

if __name__ == "__main__":
    main()
