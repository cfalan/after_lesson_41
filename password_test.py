


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


'''
true_password 放左 loop 外運算會較簡潔
思考，chance 減少，應在哪個行動後發生
chance 減少，應在輸入錯誤後發生，不是在每次輸入後發生。這確保輸入正確後，不會減少chance。

每次輸入password後，最先要驗證的，應該是password是否正確
之後才到其他行動

chance 每次減少，最先驗證的，應該是chance 是否已到0， 到0要有相應行動。
未到0， 就給回應，再行loop。

'''

true_password = 'alan'

chance = 2

print('你有 ', chance, ' 次輸入密碼機會')

while chance >= 0:

	password = input('請輸入密碼：  ')
	

	if true_password == password:
		print('密碼正確')
		break

	else:
		chance = chance - 1
		if chance == 0:
			print('還是錯誤了，goodbye~~~~~')
			break
		else:
			print('不正確，請重試')
			print('你尚有 ', chance, ' 次機會')

	

'''
#執行用
python3 password_test.py

#更新版本用
git add password_test.py
git commit -m "4"
git push origin main
'''



