# 如何去掉字符串中不需要的字符
# 方法1：strip
# s = '...abc....'
# print(s.strip('.'))
# print(s.rstrip('.'))
# 方法2：replace
# s = '...abc....'
# print(s.replace('.', ''))
# s2 = '\tab\tc\t'
# print(s2.replace('\t',''))
# 方法3：正则
# import re
# s = '...abc....'
# print(re.sub('[.]', '', s))
# s2 = '\tab\tc\t'
# print(re.sub('[\t]', '', s2))
# 方法四：unicode.translate()原始目的：映射表,好像python3的unicode编码不一样了？
# u = 'nǐ hǎo'
# print(u.translate({0x0301:None}))


