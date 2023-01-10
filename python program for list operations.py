iList = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


print('iList: ',iList)

print('first element: ',iList[0]) 
 
print('fourth element: ',iList[3]) 

print('iList elements from 0 to 4 index:',iList[0: 5]) 

print('3rd or -7th element:',iList[-7]) 



iList.append(111)
print('iList after append():',iList)


print('index of \'800\': ',iList.index(800))


iList.sort()
print('after sorting: ', iList);


print('Popped elements is: ',iList.pop())
print('after pop(): ', iList);


iList.remove(800)
print('after removing \'800\': ',iList)

 
 
iList.insert(2, 1000)
print('after insert: ', iList)


print('number of occurences of \'100\': ', iList.count(100))


iList.extend([110, 220, 330])
print('after extending:', iList)

iList.reverse()
print('after reversing:',iList)


