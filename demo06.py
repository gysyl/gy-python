"""
    函数参数
        实际参数
"""


def fun01(a, b, c):
    print(a)
    print(b)
    print(c)


# 1. 位置实参：根据位置，将实参传递给形参。
fun01(1, 2, 3)

# 2.序列实参：使用星号将序列拆分后，与形参进行对应。
list01 = [4, 5, 6]
fun01(*list01)

# 3.关键字:根据名称，将实参传递给形参。
fun01(a=1, c=3, b=2)

# 4. 字典实参：使用双星号将字典拆分后，与形参进行对应。
dict01 = {"c": 3, "b": 2, "a": 1}
fun01(**dict01)

# 第一个python文件
print("hello world") 

# 交换两个变量的值
a = 1
b = 2
a,b = b,a
print("a=",a,"b=",b)
age = 18
print("age=",age)
print(f'我今年{age}岁了')
# 数组的增删改查
# 数组的增加
# append 向数组中添加元素
list01 = []
list01.append(1)
list01.append(2)
list01.append(3)
print(list01)
# insert 向数组中指定位置添加元素
list01.insert(1, 4)
print(list01)
# extend 向数组中添加多个元素
list01.extend([5, 6, 7])
print(list01)
# 数组的删除
# remove 删除指定元素
list01.remove(2)
print(list01)
# pop 删除指定位置的元素
list01.pop(1)
print(list01)
# clear 清空数组
list01.clear()
print(list01)
# 数组的修改
# 修改指定位置的元素
list01[0] = 1
print(list01)
# 数组的查询
# index 查询指定元素的位置
print(list01.index(1))
# count 查询指定元素的个数
print(list01.count(1))
# len 查询数组的长度
print(len(list01))
# 数组的排序
# sort 升序排序
list01.sort()
