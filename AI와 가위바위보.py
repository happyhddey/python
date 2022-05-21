s = '가위'
r = '바위'
h = '보'
you=0
AI=0
tie=0
while True:
    import random
    a = random.choice(['가위', '바위', '보'])
    if you==0 and AI==0 and tie==0:
        print('가위바위보를 시작할까요? 네/나가기')
    else:
        print('가위바위보를 다시 시작할까요? 네/나가기')
    start= input()
    if start=='네':
        print('현재', you, '승,', AI, '패,', tie, '무 입니다')
        while True:
            print('가위, 바위, 보 중에서 하나를 선택하세요')
            b= input()
            if b==s or b==r or b==h:
                if a==b:
                    print('AI와 비겼습니다!')
                    tie=tie+1
                    break
                else:
                    if a == s:
                        if b == r:
                            print('당신이 AI를 이겼습니다.')
                            you=you+1
                            break
                        else:
                            print('AI가 이겼습니다')
                            AI=AI+1
                            break
                    else:
                        if a == r:
                            if b == s:
                                print('AI가 이겼습니다')
                                AI = AI + 1
                                break
                            else:
                                print('당신이 AI를 이겼습니다.')
                                you = you + 1
                                break
                        else:
                            if a==h:
                                if b==s:
                                    print('당신이 AI를 이겼습니다.')
                                    you = you + 1
                                    break
                                else:
                                    print('AI가 이겼습니다')
                                    AI = AI + 1
                                    break
                            else:
                                pass
            else:
                continue
    else:
        if start=='나가기':
            if you==0 and AI==0 and tie==0:
                break
            else:
                print('총 결과입니다.', you, '승,', AI, '패,', tie,'무 입니다.')
                if you>AI:
                    print('당신이 AI를 이겼습니다! 축하합니다!')
                else:
                    if you<AI:
                        print('당신은 AI에게 패배했습니다.')
                    else:
                        print('AI와 당신은 비겼습니다.')
                break
        else:
            continue