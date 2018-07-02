no_of_students = int(input())
header = list(input().split())
from collections import namedtuple
marksheet = namedtuple('marksheet',header)
total_mark = 0
for i in range(no_of_students):
    student = marksheet(*list(input().split()))
    total_mark += int(student.MARKS)
    print(student)
print('%.2f' %(total_mark/no_of_students))
    
