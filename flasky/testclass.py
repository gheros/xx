#1
def get_no_of_instances(cls_obj):
    return cls_obj.no_inst
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
ik1 = Kls()
ik2 = Kls()
print(get_no_of_instances(ik2))
print(get_no_of_instances(ik1))
print(get_no_of_instances(Kls))
print(get_no_of_instances(Kls))



#2
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst
ik1 = Kls()
ik2 = Kls()
print (ik1.get_no_of_instance())
print (Kls.get_no_of_instance())

class test1(object):
    a=0
    b=0
    num=0
    @staticmethod
    def add(a,b):
        return a+b


    def addlist(self,i1,i2):
        self.a=i1
        self.b=i2
        test1.num=test1.num+1
        print(self.a,self.b)
t1=test1()
# t1.add()
print(t1.a,t1.b)
t1.addlist(3,3)
print(t1.a,t1.b,t1.num)
t2=test1()
print(t2.a,t2.b,t2.num)
t2.addlist(2,2)
print(t2.a,t2.b,t2.num)
print(t1.a,t1.b,t1.num)



