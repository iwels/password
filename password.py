ps = 'a123456'
x =3
while x > 0:
	x = x-1
	ps1 = input('請輸入密碼(你有三次機會):')
	if ps1 != ps:
		print('密碼錯誤!')
		if x > 0:
			print('還有',x,'次機會!')
		else:
			print('沒有機會了！')
	
	if ps1 == ps:
		print('登入成功')
		break
		