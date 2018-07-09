no_of_inps,inp = input(),list(map(str,input().split()))                
print(all([any(v == v[::-1] for v in inp), all(int(x)>0 for x in inp)]))
