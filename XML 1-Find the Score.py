import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    tot = 0  # your code goes here
    #print(len(node))
    tot += len(node.attrib)
    if len(node)>0:
        for ele in node:
            tot += (get_attr_number(ele))
    return (tot)
    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
