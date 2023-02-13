from collections import namedtuple

info = namedtuple('Studnt','ID MARKS CLASS NAME')

n = int(input())
students = []

for i in range(n+1):
    line = input().split()
    students.append(info(*line))

for i in range(4):
    if students[0][i] == 'MARKS':
        dx = i


marks = []
for i in range(1,len(students)+1):
    marks.append(int(students[i][dx]))


if len(marks) == 0:
    print("No valid marks found.")
else:
    avg = sum(marks) / len(marks)
    print("{:.2f}".format(avg))


