#讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:#with會執行open，並且自動close
	for line in f:
		data.append(line.strip())#把陣列加上新的一行line資料，strip去掉換行\n與多的空格
		count += 1
		if count % 1000 == 0:
			print(len(data))
		#strip只能針對字串，append只能針對清單
print(data[0])
print('--------------------------')
print(data[1])
print('檔案讀取完了，總共有', len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #用for迴圈總合留言長度
print('全部留言的總長度為', sum_len)
avg_len = sum_len / len(data)
print('每筆留言的平均長度為', avg_len)