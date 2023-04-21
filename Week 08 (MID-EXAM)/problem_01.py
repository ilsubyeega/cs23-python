height = input('키(cm)? ')
weight = input('몸무게(kg)? ')

def isUnsignedReal(n):
    flagdigit = n.isdigit()
    flagdigitperiod = n.replace('.', '', 1).isdigit()
    return flagdigit or flagdigitperiod

if not isUnsignedReal(height) or not isUnsignedReal(weight):
    print('입력 오류')
else:
    bmi = float(weight) / (float(height) / 100) ** 2
    print(bmi)

"""
Point: (12/12)
"""