# 如何调整字符串中文本的格式？
import re

log = open('../tmp/log.txt').read()
# new_log = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', log)
new_log = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)
print(new_log)
