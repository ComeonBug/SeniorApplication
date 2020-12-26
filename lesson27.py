# 解析xml文件
from xml.etree.ElementTree import parse

f = open('./tmp/test.xml', 'r')
et = parse(f)
print(et)
root = et.getroot()
print(root)
print(root.tag)
print(root.attrib)
# python3中使用elementtree.iter()来代替getiterator,使用list()来代替getChildren()
# print(list(et.iter()))
# for child in et.iter():
#     print(child.tag)
# for i in et.iterfind('country'):
#     print(i.get('name'))
# for i in et.findall('country'):
#     print(i.get('name'))
#     for j in i.findall('neighbor'):
#         print(j.get('name'))
# for i in list(root.iter('neighbor')):
#     print(i)
# for i in list(root.iter('country/*')): # 迭代对象里为空,root.iter('标签名')：这里不支持xpath
#     print(i)
# a = list(root.findall('country/*')) # root.findall('表达式')：这里支持xpath，xpath：*任意元素
# # print(a)
# b = list(root.findall('.//neighbor')) # xpath:.//任意位置
# print(b)
# c = list(root.findall('.//neighbor[1]')) # xpath:.//任意位置
# print(c)
# d = list(root.findall('.//neighbor[last()]')) # xpath:.//任意位置
# print(d)
# f = list(root.findall('.//country[@name="beijin"]'))
# print(f)
g = list(root.findall('country[rank]')) # 找到含有rank这个标签的所有的country标签
print(g)
h = list(root.findall('country[rank="3"]')) # 找到含有rank,且值为3的这个标签的所有的country标签
print(h)
