# 如何构建xml文件：把其他类型的文件转为xml文件
# 即如何构建一个 element tree
from xml.etree.ElementTree import ElementTree,Element,tostring


e = Element('Data')
print(e.tag)
e.set('name','abc')
print(tostring(e))
e.text='123'
print(tostring(e))
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.88'
e2.append(e3)
print(tostring(e2))
e.text=None
e.append(e2)
print(tostring(e))
et = ElementTree(e)
et.write(open('../tmp/demo.xml', 'wb'))