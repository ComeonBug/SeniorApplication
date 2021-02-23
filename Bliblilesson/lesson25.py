# csv文件读取
import csv

rf = open('../tmp/test.csv', 'r')
wf = open('../tmp/test2.csv', 'w')
reader = csv.reader(rf)
print(reader)
for i in reader:
    print(i)
    print(reader.line_num)
    if reader.line_num>1 and int(i[1])>3:
        wf.write(','.join(i))