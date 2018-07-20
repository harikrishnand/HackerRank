import xml.etree.ElementTree as etree


maxdepth = 0
def depth(elem, level):
    global maxdepth
    
    if len(elem)>0:
        if maxdepth == level+1:
            maxdepth += 1
            
        for e in elem:
            depth(e,level+1)
    #print(len(elem),level,maxdepth)
    # your code goes here
    
    
    if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
