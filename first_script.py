#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

print("Output #1: I'm excited to learn Python.")

# 两个数值相加
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))

# 两个列表相加
a = [1, 2, 3, 4]
b = ['first', 'second', 'third', 'fourth']
c = a + b
print("Output #3: {0}, {1}, {2}.".format(a,b,c))

# 数值 - 整数
x = 9
print('Output #4: {0}'.format(x))
print('Output #5: {0}'.format(3**4))
print('Output #6: {0}'.format(int(8.3)/int(2.7)))

# 数值 - 浮点数
print('Output #7: {0:.3f}'.format(8.3/2.7))
y = 2.5 * 4.8
print('Output #8: {0:.1f}'.format(y))
r = 8/float(3)
print('Output #9: {0:.2f}'.format(r))
print('Output #10: {0:.4f}'.format(8.0/3))

# 数值 - math库基本函数演示
print('Output #11: {0:.4f}'.format(exp(3)))
print('Output #12: {0:.2f}'.format(log(4)))
print('Output #13: {0:.1f}'.format(sqrt(81)))

# 字符串
print('Output #14: {0:s}'.format('I\'m enjoying learning Python.'))
print('Output #15: {0:s}'.format('This is a long string. Without the backslash\
 it would run off of the page on the right in the text editor and be very\
 difficult to read and edit. By using the backslash you can split the long\
 string into smaller strings on separate lines so that the whole string is easy\
 to view in the text editor.'))
print('Output #16: {0:s}'.format('''You can use triple single quotes
for multi-line comment strings.'''))
print('Output #17: {0:s}'.format("""You can also use triple double quotes
for multi-line comment strings."""))

# 字符串 - 常用操作符和函数
string1 = 'This is a '
string2 = 'short string.'
sentence = string1 + string2
print('Output #18: {0:s}'.format(sentence))
print('Output #19: {0:s} {1:s}{2:s}'.format('She is', 'very '* 4, 'beautiful.'))
m = len(sentence)
print('Output #20: {0:d}'.format(m))

# 字符串 - split
string1 = 'My deliverable is due in May'
string1_list1 = string1.split()
string1_list2 = string1.split(' ', 2)
print('Output #21: {0}'.format(string1_list1))
print('Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}'\
      .format(string1_list2[0], string1_list2[1], string1_list2[2]))
string2 = 'Your,deliverable,is,due,in,June'
string2_list = string2.split(',')
print('Output #23: {0}'.format(string2_list))
print('Output #24: {0} {1} {2}'.format(string2_list[1], string2_list[5], string2_list[-1]))


# 字符串 - join
print('Output #25: {0}'.format(','.join(string2_list)))

# 字符串 - strip
string3 = ' Remove unwated characters    form this string.\t\t   \n'
print('Output #26: string3: {0:s}'.format(string3))
string3_lstrip = string3.lstrip()
print('Output #27: lstrip: {0:s}'.format(string3_lstrip))
string3_rstrip = string3.rstrip()
print('Output #28: rstrip: {0:s}'.format(string3_rstrip))
string3_strip = string3.strip()
print('Output #29: strip: {0:s}'.format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__---++"
print('Output #30: {0:s}'.format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print('Output #31: {0:s}'.format(string4_strip))

# 字符串 - replace
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(' ', '!@!')
print('Output #32 (with !@!): {0:s}'.format(string5_replace))
string5_replace = string5.replace(' ', ',')
print('Output #33 (with commas): {0:s}'.format(string5_replace))

# 字符串 - lower、upper、capitalize
string6 = "Here's WHAT Happens WHEN You Use lower."
print('Output #34: {0:s}'.format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print('Output #35: {0:s}'.format(string7.upper()))
string8 = "here's WHAT Happens WHEN you use Capitalize."
print('Output #36: {0:s}'.format(string8.capitalize()))
string8_list = string8.split()
print('Output #37 (on each word):')
for word in string8_list:
      print('{0:s}'.format(word.capitalize()))

# 正则表达式 - 计算字符串中模式出现的次数
string = 'The quick brown fox jumps over the lazy dog.'
string_list = string.split()
pattern = re.compile(r'The', re.I)
count = 0
for word in string_list:
      if pattern.search(word):
            count += 1
print('Output #38: {0:d}'.format(count))

# 正则表达式 - 在字符串中每次找到模式时将其打印出来
string = 'The quick brown fox jumps over the lazy dog.'
string_list = string.split()
pattern = re.compile(r'(?P<match_word>The)', re.I)
print('Output #39:')
for word in string_list:
      if pattern.search(word):
            print('{:s}'.format(pattern.search(word).group('match_word')))

# 正则表达式 - 使用字母'a'替换字符串中的单词'the'
string = 'The quick brown fox jumps over the lazy dog.'
string_to_find = r'The'
pattern = re.compile(string_to_find, re.I)
print('Output #40: {:s}'.format(pattern.sub('a', string)))

# 日期 - 打印出今天的日期形式，以及年、月、日
today = date.today()
print('Output #41: today: {0!s}'.format(today))
print('Output #42: {0!s}'.format(today.year))
print('Output #43: {0!s}'.format(today.month))
print('Output #44: {0!s}'.format(today.day))
current_datetime = datetime.today()
print('Output #45: {0!s}'.format(current_datetime))

# 日期 - 使用timedelta计算一个新日期
one_day = timedelta(days= -1)
yesterday = today + one_day
print('Output #46: yesterday: {0!s}'.format(yesterday))
eight_hours = timedelta(hours= -8)
print('Output #47: {0!s} {1!s}'.format(eight_hours.days, eight_hours.seconds))

# 日期 - 计算出两个日期之间的天数
date_diff = today - yesterday
print('Output #48: {0!s}'.format(date_diff))
print('Output #49: {0!s}'.format(str(date_diff).split()[0]))

# 日期 - 根据一个日期对象创建具有特定格式的字符串
print('Output #50: {:s}'.format(today.strftime('%m/%d/%Y')))
print('Output #51: {:s}'.format(today.strftime('%b %d, %Y')))
print('Output #52: {:s}'.format(today.strftime('%Y-%m-%d')))
print('Output #53: {:s}'.format(today.strftime('%B %d, %Y')))

# 日期 - 根据一个表示日期的字符串
# 创建一个带有特殊格式的datetime对象
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
# 基于4个具有不同日期格式的字符串
# 创建2个datetime对象和2个date对象
print('Output #54: {!s}'.format(datetime.strptime(date1, '%m/%d/%Y')))
print('Output #55: {!s}'.format(datetime.strptime(date2, '%b %d, %Y')))
# 仅显示日期部分
print('Output #56: {!s}'.format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print('Output #57: {!s}'.format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))

# 列表 - 创建列表
# 使用方括号创建一个列表
# 用len()计算列表中元素的数量
# 用max()和min()找出最大值和最小值
# 用count()计算出列表中某个值出现的次数
a_list = [1, 2, 3]
print('Output #58: {}'.format(a_list))
print('Output #59: a_list has {} elements.'.format(len(a_list)))
print('Output #60: the maximum value in a_list is {}.'.format(max(a_list)))
print('Output #61: the minimum value in a_list is {}.'.format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print('Output #62: {}'.format(another_list))
print('Output #63: another_list also has {} elements.'.format(len(another_list)))
print('Output #64: 5 is in another_list {} time.'.format(another_list.count(5)))

# 列表 - 索引值
# 使用索引值访问列表中的特定元素
# [0]是第1个元素，[-1]是最后一个元素
print('Output #65: {}'.format(a_list[0]))
print('Output #66: {}'.format(a_list[1]))
print('Output #67: {}'.format(a_list[2]))
print('Output #68: {}'.format(a_list[-1]))
print('Output #69: {}'.format(a_list[-2]))
print('Output #70: {}'.format(a_list[-3]))
print('Output #71: {}'.format(another_list[2]))
print('Output #72: {}'.format(another_list[-1]))

# 列表 - 列表切片
# 使用列表切片访问列表元素的一个子集
# 从开头开始切片，可以省略第1个索引值
# 一直切片刀末尾，可以省略第2个索引值
print('Output #73: {}'.format(a_list[0:2]))
print('Output #74: {}'.format(another_list[:2]))
print('Output #75: {}'.format(a_list[1:3]))
print('Output #76: {}'.format(another_list[1:]))

# 列表 - 列表复制
# 使用[:]复制一个列表
a_new_list = a_list[:]
print('Output #77: {}'.format(a_new_list))

# 列表 - 列表链接
# 使用+将两个或更多个列表链接起来
a_longer_list = a_list + another_list
print('Output #78: {}'.format(a_longer_list))

# 列表 - 使用in和not in
# 使用in和not in来检查列表中是否有特定元素
a = 2 in a_list
print('Output #79: {}'.format(a))
if 2 in a_list:
      print('Output #80: 2 is in {}'.format(a_list))
b = 6 not in a_list
print('Output #81: {}'.format(b))
if 6 not in a_list:
      print('Output #82: 6 is not in {}'.format(a_list))

# 列表 - 追加、删除和弹出元素
# 使用append()向列表末尾追加一个新元素
# 使用remove()从列表中删除一个特定元素
# 使用pop()从列表末尾删除一个元素
a_list.append(4)
a_list.append(5)
a_list.append(6)
print('Output #83: {}'.format(a_list))
a_list.remove(5)
print('Output #84: {}'.format(a_list))
a_list.pop()
a_list.pop()
print('Output #85: {}'.format(a_list))

# 列表 - 列表反转
# 使用reverse()原地反转一个列表会修改原列表
# 要想反转列表同时又不修改原列表，可以先复制列表
a_list.reverse()
print('Output #86: {}'.format(a_list))
a_list.reverse()
print('Output #87: {}'.format(a_list))

# 列表 - 列表排序
# 使用sort()对列表进行原地排序会修改原列表
# 要想对列表进行排序同时又不修改原列表，可以先复制列表
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print('Output #88: {}'.format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print('Output #89: {}'.format(list_copy))
print('Output #90: {}'.format(unordered_list))

# 列表 - sorted排序函数
# 使用sorted()对一个列表集合按照列表中某个位置的元素进行排序
my_lists = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 4, 1, 3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value:index_value[3])
print('Output #91: {}'.format(my_lists_sorted_by_index_3))
# 使用itemgetter()对一个列表集合按照两个索引位置来排序
my_lists = [[123, 2, 2, 444], [22, 6, 6, 444], [354, 4, 4, 678], [236, 5, 5, 678], [578, 1, 1, 290], [461, 1, 1, 290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3, 0))
print('Output #92: {}'.format(my_lists_sorted_by_index_3_and_0))

# 元组 - 创建元组
# 使用圆括号创建元组
my_tuple = ('x', 'y', 'z')
print('Output #93: {}'.format(my_tuple))
print('Output #94: my_tuple has {} elements'.format(len(my_tuple)))
print('Output #95: {}'.format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print('Output #96: {}'.format(longer_tuple))

# 元组 - 元组解包
one, two, three = my_tuple
print('Output #97: {0} {1} {2}'.format(one, two, three))
var1 = 'red'
var2 = 'robin'
print('Output #98: {} {}'.format(var1, var2))
# 在变量之间交换彼此的值
var1, var2 = var2, var1
print('Output #99: {} {}'.format(var1, var2))

# 元组 - 元组转换成列表（及列表转换成元组）
# 将元组转换成列表，列表转换成元组
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print('Output #100: {}'.format(tuple(my_list)))
print('Output #101: {}'.format(list(my_tuple)))

# 字典 - 创建字典
# 使用花括号创建字典
# 用冒号分隔键-值对
# 用len()计算出字典中键-值对的数量
empty_dict = {}
a_dict = {'one':1, 'two':2, 'three':3}
print('Output #102: {}'.format(a_dict))
print('Output #103: a_dict has {!s} elements'.format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', '9']}
print('Output #104: {}'.format(another_dict))
print('Output #105: another_dict also has {!s} elements'.format(len(another_dict)))

# 字典 - 引用字典中的值
# 使用键来引用字典中特定的值
print('Output #106: {}'.format(a_dict['two']))
print('Output #107: {}'.format(another_dict['z']))

# 字典 - 复制
# 使用copy()复制一个字典
a_new_dict = a_dict.copy()
print('Output #108: {}'.format(a_new_dict))

# 字典 - 键、值和项目
# 使用keys()、values()和items()分别引用字典中的键、值和键-值对
print('Output #109: {}'.format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print('Output #110: {}'.format(a_dict_keys))
print('Output #111: {}'.format(a_dict.values()))
print('Output #112: {}'.format(a_dict.items()))

# 字典 - 使用in、not in和get
if 'y' in another_dict:
      print('Output #114: y is a key in another_dict: {}.'.format(another_dict.keys()))
if 'c' not in another_dict:
      print('Output #115: c is not a key in another_dict: {}.'.format(another_dict.keys()))
print('Output #116: {!s}'.format(a_dict.get('three')))
print('Output #117: {!s}'.format(a_dict.get('four')))
print('Output #118: {!s}'.format(a_dict.get('four', 'Not in dict')))

# 字典 - 排序
# 使用sorted()对字典进行排序
# 要想对字典排序的同时不修改原字典
# 先复制字典
print('Output #119: {}'.format(a_dict))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print('Output #120: (order by keys): {}'.format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print('Output #121: (order by values): {}'.format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print('Output #122: (order by values, descending): {}'.format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print('Output #123: (order by values, ascending): {}'.format(ordered_dict4))

# 控制流 - if-else语句
x = 5
if x > 4 or x != 9:
      print('Output #124: {}'.format(x))
else:
      print('Output #124: x is not greater than 4')

# 控制流 - if-elif-else语句
if x > 6:
      print('Output #125: x is greater than six')
elif x > 4 and x == 5:
      print('Output #125: {}'.format(x*x))
else:
      print('Output #125: x is not greater than 4')

# 控制流 - for循环
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', 'Holly', 'Isabel', 'Jenny']
print('Output #126:')
for month in y:
      print('{!s}'.format(month))
print('Output #127: (index value: name in list)')
for i in range(len(z)):
      print('{0!s}: {1:s}'.format(i, z[i]))
print("Output #128: (access elements in y with z's index values)")
for j in range(len(z)):
      if y[j].startswith('J'):
            print('{!s}'.format(y[j]))
print('Output #129:')
for key, value in another_dict.items():
      print('{0:s}, {1}'.format(key, value))

# 控制流 - 简化for循环：列表、集合与字典生成式
# 使用列表生成式选择特定的行
my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print('Output #130: (list comprehension): {}'.format(rows_to_keep))
# 使用集合生成式在列表中选择出一组唯一的元组
my_data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9)]
set_of_tuples1 = {x for x in my_data}
print('Output #131: (set comprehension): {}'.format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print('Output #132: (set function): {}'.format(set_of_tuples2))
# 使用字典生成式选择特定的键-值对
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value >10}
print('Output #133: (dictionary comprehension): {}'.format(my_results))

# 控制流 - while循环
print('Output #134:')
x = 0
while x < 11:
      print('{!s}'.format(x))
      x += 1

# 控制流 - 函数
# 计算一系列数值的均值：
def getMean(numericValues):
      return sum(numericValues)/len(numericValues) if len(numericValues) > 0 else float('nan')
my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print('Output #135 (mean): {!s}'.format(getMean(my_list)))

# 控制流 - try-except
# 计算一系列数值的均值
def getMean2(numericValues):
      return sum(numericValues)/len(numericValues)
my_list2 = []
try:
      print('Output #138 {}'.format(getMean2(my_list2)))
except ZeroDivisionError as detail:
      print('Output #138 (Error): {}'.format(float('nan')))
      print('Output #138 (Error): {}'.format(detail))

# 控制流 - try-except-else-finally
# 完整形式
try:
      result = getMean2(my_list2)
except ZeroDivisionError as detail:
      print('Output #142 (Error): {}'.format(float('nan')))
      print('Output #142 (Error): {}'.format(detail))
else:
      print('Output #142 (The mean is ): {}'.format(result))
finally:
      print('Output #142 (Finally): The finally block is executed every time')

# 读取文件
# 读取单个文本文件
#input_file = sys.argv[1]
#print('Output #143:')
#filereader = open(input_file, 'r')
#for row in filereader:
#      print(row.strip())
#filereader.close()
# 读取文件的新型语法
#input_file = sys.argv[1]
#print('Output #144:')
#with open(input_file, 'r') as filereader:
#      for row in filereader:
#            print('{}'.format(row.strip()))

# 读取多个文本文件
#print('Output #145:')
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
#      with open(input_file, 'r') as filereader:
#            for row in filereader:
#                  print('{}'.format(row.strip()))

# 写入文件
# 写入一个文本文件
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(max_index):
      if index_value < (max_index - 1):
            filewriter.write(my_letters[index_value]+'\t')
      else:
            filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print('Output #146: Output written to file')

# 写入CSV文件
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(max_index):
      if index_value < (max_index - 1):
            filewriter.write(str(my_numbers[index_value])+',')
      else:
            filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print('Output #147: Output appended to file')
