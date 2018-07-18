from html.parser import HTMLParser
#import re

class customparser(HTMLParser):
    """ Custom parser for formating change"""
    def handle_comment(self,data): pass
        #print(data)

    def handle_starttag(self, tag, attrs):
        print('Start : ' + tag)
        if attrs:
            print(*['-> {0} > {1}'.format(a,v) for a,v in attrs], sep='\n')
    
    def handle_endtag(self, tag):
        print('End   : ' + tag)
    
    def handle_startendtag(self, tag, attrs):
        print('Empty : ' + tag)
        if attrs:
            print(*['-> {0} > {1}'.format(a,v) for a,v in attrs], sep='\n')


no_of_lines = int(input())
htmlinst = customparser()
inp = ''
for i in range(no_of_lines):
    inp += input()+ '\n'     
    
#print(inp)    
htmlinst.feed(inp)
