#讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:#with會執行open，並且自動close
	for line in f:
		data.append(line.strip())#把陣列加上新的一行line資料，strip去掉換行\n與多的空格
		count += 1
		if count % 1000 == 0:
			print(len(data))
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #用for迴圈總合留言長度
print('全部留言的總長度為', sum_len)
avg_len = sum_len / len(data)
print('每筆留言的平均長度為', avg_len)

new = [] #新的清單陣列
for d in data:
	if len(d) < 100:
		new.append(d)
print('小於100字的，有 ', len(new), '筆')
print(new[0])
print(new[1])

	