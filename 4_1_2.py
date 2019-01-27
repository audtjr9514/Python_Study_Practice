def sum_avg(x=[]):
    sum = 0
    for i in x:
        sum += int(i)
    avg = sum / len(x)
    print("입력받은 평균의 값은 %s" %avg)

a = input("숫자를 입력하세요 : ").split(" ")
sum_avg(a)