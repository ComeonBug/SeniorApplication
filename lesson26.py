# 读写json
import json

l = [
    {
        "key": "elementId",
        "value": "878472a4-0bc2-4e6b-b069-2b0bcc38f160",
        "name": "elementId"
    }]
# # dumps()把json转为str
# j = json.dumps(l)
# print(j)
# j2 = json.dumps(l,separators=(',',':'))
# print(j2)
# j3 = json.dumps(l, sort_keys=True)
# print(j3)
# # loads():把str转为list或dict
# s = '[{"key":"elementId","value":"878472a4-0bc2-4e6b-b069-2b0bcc38f160","name":"elementId"}]'
# sj = json.loads(s)
# print(type(sj))
# print(sj)
# s2 = '{"key":"elementId","value":"878472a4-0bc2-4e6b-b069-2b0bcc38f160","name":"elementId"}'
# sj2 = json.loads(s2)
# print(type(sj2))
# print(sj2)
# 读取json文件内容，读取后的对象类型为str
jf = json.load(open('./tmp/2.json','r'))
print(type(jf))
print(jf)
# 把str写入文件
with open('./tmp/test2.json','w') as f:
    json.dump(jf, f)


