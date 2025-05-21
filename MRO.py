class A:
    def hablar(self):
        print("hola desde A")
        
class B(A):
    pass
        
class C(A):
    pass
        
class D(B,C):
    pass
        
d = D()

d.hablar()