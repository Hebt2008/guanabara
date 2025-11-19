# v = r * a
# a = v/r
# r = v/a
a = float(input('sua corrente  '))
v = float(input('sua tensao  '))
r = float(input('sua resistencia  '))

if a == 0:
    res_a1 = v / r
    print('sua corrente e ',res_a1)
elif v == 0 :
    res_v1 = r * a
    print('sua tensao e',res_v1)
elif r == 0 :
    res_r1 = v / a
    print('sua resistencia e',res_r1)
else :
    print('ok')

