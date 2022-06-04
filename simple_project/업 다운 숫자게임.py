import random
a=random.randint(1,1000)
count=1
while True:
    print(count, '번쨰 시도입니다')
    print('숫자를 맞춰보세요')
    b = input()
    if b=='싫어' or b=='싫어요' or b=='왜' or b=='왜?' or b=='하기 싫어' or b=='안할래' or b=='어쩌라고':
        print('그럼 하지마.')
        break
    else:
        b = int(b)
        if b == a:
            print('축하합니다! 정답을 맞추셨습니다!')
            print(count,'번 만에 정답을 맞추셨습니다')
            break
        else:
            count=count+1
            if b>a:
                print('다운!')
            else:
                print('업!')
                continue
