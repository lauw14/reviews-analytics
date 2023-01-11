#讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:#with會執行open，並且自動close
	for line in f:
		data.append(line.strip())#把陣列加上新的一行line資料，strip去掉換行\n與多的空格
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有 ', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #用for迴圈總合留言長度
	avg_len = sum_len / len(data)
print('每筆留言的平均長度為', avg_len)

new = [] #新的清單陣列
for d in data:
	if len(d) < 100:
		new.append(d)
print('小於100字的，有 ', len(new), '筆')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('談到good的留言，有 ', len(good), '筆')

#文字計數
wc = {} #word_count 字典
for d in data: #依次拆開不同人對話集
	words = d.split(' ') #用空格該人的對話拆開成陣列存的單字，建立一堆單字的words陣列
#但多個空格會生成多個空串字
#但其實split()括號裡是預設值為空白鍵，遇到連續空白，不會生成空字串。直接跳過
	for word in words: #把陣列的對話單字，一個個抓出單字
		if word in wc:
			wc[word] += 1 #第n次找到這個字，多一次
		else:
			wc[word] = 1 #第一次找到這個字, 增加第一次
			#新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:     #只印出超過100的字
		print(word, wc[word]) #列印出字典的key, value

print(len(wc)) #字典的長度
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('這個字沒有出現過')
print('感謝您的使用')


	