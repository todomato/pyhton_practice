#list container

list = ['aaa', 'b', 7,  True, 0.3]
for index in range(0, len(list)):
    print(list[index])


# list.append(x): 把變數x塞到list的最後面
# list.insert(i, x): 把變數x塞到i這個位置上
# list.pop(): 把list的最後一格丟掉
# list.pop(i): 把list的第i格丟掉
# list.remove(x): 會把第一個出現的變數x拿掉
# list.clear(): 把list內的資料全部清光光

#slice
print(list[0:2])