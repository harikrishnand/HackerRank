def wrapper(f):
    def fun(l):
        nl = ['+91 '+v[-10:-5] + ' ' + v[-5:] for v in l]
        ret = f(nl)
        return ret        
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
