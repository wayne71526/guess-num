# 產生一個隨機整數1-100(不要印出來)
# 讓使用者重複輸入去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要告訴他比答案大/小

import random
ans = random.randint(1, 100)
while True:
	guess = input('請猜一個數字： ')
	guess = int(guess)
	if ans == guess:
		print('你猜中了')
		break
	elif ans > guess:
		print('比答案小')
	else:
		print('比答案大')