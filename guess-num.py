# 產生一個隨機整數1-100(不要印出來)
# 讓使用者重複輸入去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要告訴他比答案大/小

import random
start = input('請輸入隨機數字範圍開始值： ')
end = input('請輸入隨機數字範圍結束值： ')
start = int(start)
end = int(end)
ans = random.randint(start, end)
count = 0
while True:
	guess = input('請猜一個數字： ')
	guess = int(guess)
	count += 1 # count = count + 1
	if ans == guess:
		print('你猜中了')
		print('這是你猜的第', count, '次')
		break
	elif ans > guess:
		print('比答案小')
	else:
		print('比答案大')
	print('這是你猜的第', count, '次')	