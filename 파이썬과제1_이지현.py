dic = {"이화여대 멋사 대표님":"현숙", "멋사 창립자":"두희","파이썬 세션 튜터":"세은","야옹":"마루"}

#for문으로 반복 / input()
print()

for key, value in dic.items() :
    print("다음은 누구에 대한 설명일까요? \n 1.현숙 2.세은 3. 두희 4.마루")
    print(key)
    
    value = dic[key]
    v = input()
    
    if value == v:
        print("정답입니다!")
    else :
        print("오답입니다!")