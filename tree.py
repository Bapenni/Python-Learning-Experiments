import sympy as sym

class Expr:
    pass

class Times (Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        
    def __str__(self):
        return "[" + str(self.l) + "*" + str(self.r) + "]"
    
    def eval(self,env):
        return self.l.eval(env) * self.r.eval(env)
        

class Plus (Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        
    def __str__(self):
        return "[" + str(self.l) + "+" + str(self.r) + "]"
    
    def eval(self,env):
        return self.l.eval(env) + self.r.eval(env)


class Const(Expr):
    def __init__(self,val):
        self.val = val
        
    def __str__(self):
        return str(self.val)
    
    def eval(self, env):
             return self.val


class Var (Expr):
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return str(self.name)
    
    def eval(self,env):
        return env[self.name]


e1 = Times(Const(3), Plus(Var("y"), Var("x")))
# print(e1)
e2 = Plus(Times(Const(3), Var("y")),Var("x"))
# print(e2)
env = {"x" : 2, "y" : 4}

#print(e1.eval(env))
#print(e2.eval(env))


x = sym.Symbol("x")

eq = (x**2 + 1) * sym.cos(x)
print(sym.diff(eq))

a, b = sym.symbols("a, b")
eq2 = x**2*y
print(sym.diff(eq2, x))