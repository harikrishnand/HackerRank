def fun(s):   # return True if s is a valid email, else return False
    import re
    #print(s)
    m = re.match(r'[\w-]+@[a-z¦0-9¦A-Z]+\.{1}[a-z¦0-9¦A-Z]{0,3}$',s)
    if m:
        return True
    else:
        return False
        
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
