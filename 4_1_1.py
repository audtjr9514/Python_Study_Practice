def is_odd(x):
    if x%2 == 0:
        print("%d은 짝수입니다" %x)
    else:
        print("%d은 홀수입니다" %x)

a = int(input("숫자를 입력하세요 : "))
is_odd(a)
