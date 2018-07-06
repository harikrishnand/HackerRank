import re
no_of_tries = int(input())
test = 'test'
for i in range(no_of_tries):
    try:
        re.match(input(),test)
    except Exception as e:
        print('False')
        #print('False',e,dir(e),e.msg,e.args)
    else:
        print('True')
