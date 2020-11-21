ps = 'a123456'
x =3
while x > 0:
	ps1 = input('請輸入密碼(你有三次機會):')
	if ps1 != ps:
		print('密碼錯誤','還有', x-1, '次機會')
	x = x-1
	if ps1 == ps:
		print('登入成功')
		break
		