class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"



class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

 

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            p1_repr = "(" + repr(self.p1) + ")"
        else:
            p1_repr = repr(self.p1)
        
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_repr = "(" + repr(self.p2) + ")"
        else:
            p2_repr = repr(self.p2)
        
        return f"{p1_repr} * {p2_repr}"




class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return "(" + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"




poly_div = Div(Add(Int(10), Mul(X(), Int(2))), Int(2))
poly_sub = Sub(Add(Int(5), X()), Mul(Int(2), X()))
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))

print(poly)
print(poly_div)
print(poly_sub)

# Test case 1: Division and Subtraction in a larger expression
larger_expr = Add(
    Div(Mul(Int(5), X()), Int(2)),
    Sub(Add(Int(3), X()), Mul(X(), Int(4)))
)
print("Result for larger_expr",larger_expr)

# Test case 2: Complex expression involving all operations
complex_expr = Add(
    Mul(Int(2), X()),
    Sub(
        Div(Add(Int(8), X()), Int(2)),
        Mul(Int(3), X())
    )
)
print("Result for complex_expr",complex_expr)

# Test case 3: Expression with nested operations
nested_expr = Add(
    Mul(Int(2), Div(Add(X(), Int(3)), Int(2))),
    Sub(
        Add(Int(5), Mul(X(), Int(2))),
        Mul(X(), Div(Int(4), X()))
    )
)
print("Result for nested_expr", nested_expr)
