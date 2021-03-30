class intro : 
    def __init__(self, name, age, sex):
        self.name=name
        self.age=age
        self.sex=sex
    
    def __str__(self) :
        return "{}는 {}세이고, {}입니다.".format(self.name, self.age, self.sex)

jj = intro("짱구",5,"남자")
dd = intro("도라에몽",14,"남자")
cc = intro("코난",8,"남자")
ss = intro("쇼콜라",15,"여자")
aa = intro("아무",12,"여자")
gg = intro("가영",16,"여자")
print(jj)
print(dd)
print(cc)
print(ss)
print(aa)
print(gg)