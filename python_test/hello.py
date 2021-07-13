#coding:utf-8

for i in range(5):
	print("hello,world")

list_my=[3,1,2,5,4,9,7,3]
dict_my={}

def select_list():
    for i in list_my:
        if i not in dict_my.keys():
            dict_my[i] = 1
        else:
            print(dict_my)
            print("重复的数字是：",i)

select_list()