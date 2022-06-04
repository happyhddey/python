s='가위'
r='바위'
h='보'
while True:
    print('시작할까요? (네/나가기):', end=" ")
    start = input()
    if start =='네':
        while True:
            print('USER A:', end=" ")
            a = input()
            if a==s or a==r or a==h:
                print('A는',a,'를 선택하였습니다.')
                break
            else:
                continue
        while True:
            print('USER B:', end=" ")
            b = input()
            if b==s or b==r or b==h:
                print('B는',b,'를 선택하였습니다.')
                if a==b:
                    print('draw')
                else:
                    if a == s:
                        if b == r:
                            print('B win')
                        else:
                            print('A win')
                    else:
                        if a == r:
                            if b == s:
                                print('A win')
                            else:
                                print('B win')
                        else:
                            if a==h:
                                if b==s:
                                    print('B win')
                                else:
                                    print('A win')
                            else:
                                pass
                break
            else:
                continue
    else:
        if start =='나가기':
            break
        else:
            continue