import re


# str1 = "hello,world"
#
# pattern = re.compile(r"(\w+),(\w+),(\w+)(?P<sign>.*)")  #���ԭ���ַ�
# result1 = re.match(pattern,str1) #ƥ����ʲô��ͷ
# print(result1.string)
# print( result1.re )
# print(result1.pos)
# print(result1.endpos)
# print(result1,lastindex)

str1 = 'summer hot ~~'
pattern3 = re.compile(r"(\w+) (\w+)")
str1 = re.sub(pattern3,r"\2 \1",str1)
str1 = re.sub(pattern3,r"hello",str1)
print(str1)

def fun(m):
    return m.group(1).title() + '' + m.group(2).title
print(re.sub(pattern3,fun,s))