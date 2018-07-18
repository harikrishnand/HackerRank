from html.parser import HTMLParser

class Myparser(HTMLParser):
    """
    """

    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            print(*['-> {0} > {1}'.format(a,v) for a,v in attrs], sep='\n')
        
        
        
inp = ''
for i in range(int(input())):
    inp += input() + '\n'
parse = Myparser()
#print(inp)
parse.feed(inp)
parse.close()
