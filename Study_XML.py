from xml.etree import ElementTree


def F(root, colours, level):
    if root.attrib['color'] == 'red':
        colours['red'] += level
        
    if root.attrib['color'] == 'blue':
        colours['blue'] += level
        
    if root.attrib['color'] == 'green':
        colours['green'] += level
        
    level += 1
    for child in root:
        colours = F(child, colours, level)
        
    return colours
    
    
colours = {'red':0, 'green':0, 'blue':0}
root = ElementTree.fromstring(input())
level = 1
colours = F(root, colours, level)
for key in colours:
    print(colours[key], end=' ')
