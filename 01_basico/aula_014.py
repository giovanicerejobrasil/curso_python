a = 'AAAAAA'
b = 'BBBBBB'
c = 1.1
string = 'c={c_name:.2f}, a={0}, b={b_name}, a={0}, c={c_name:.2f}, b={b_name}'
formato = string.format(a, b_name=b, c_name=c)

print(formato)