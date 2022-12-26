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


