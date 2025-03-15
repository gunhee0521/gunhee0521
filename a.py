# STEP1 : 모듈 import
import random



def update_hint(goard,idiom,clue):

    print("goard",goard)
    print("idiom",idiom)
    print("hint",hint)
    for i in range(len(idiom)) :
        if goard == idiom[i]:
            hint[i]=goard





live=9
heart=" h "
hint=["?","?","?","?"]
result=False
words=["일석이조","호시탐탐","자업자득","금상첨화","동문서답","유유자적"]
idiom = random.choice(words)
while live >0 :
    print(hint)
    print("남은 생명 "+heart*live)
    guess=input("사자성어를 맞춰 보세요(한글자or네글자):")
    if guess ==idiom:
        result=True
        break
    else :  
        print("땡.생명이 줄어 들었습니다.")
        live-=1

    
    for gword in guess :
        if gword in idiom:
            print("idiom",idiom)
            update_hint(gword,idiom,hint)
if result :
    print("성공!")
else:
    print("실패 당신이 맞추지 못한 사자성어는"+idiom+"입니다.")