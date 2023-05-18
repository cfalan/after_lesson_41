


# using while function.

'''
while True:
	
	name = input('請輸入你的名字：  ')

	if name == 'q':
		print ('you can leave now')
		break
	else:
		print ('you cannot leave')

python3 password_test.py
'''

chance = 3

print('你有3次輸入密碼機會')

while chance >= 0:
	true_password = 'a123456'

	password = input('請輸入密碼：  ')

	chance = chance - 1

	if chance == 0:
		print('goodbye~~~~~')
		break	
		
	if true_password == password:
		print('密碼正確')
		break
	else:
		print('不正確，請重試')
		print('你尚有 ', chance, ' 次機會')
	





