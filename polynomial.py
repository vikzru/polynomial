class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return "(" + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"

    def evaluate(self, x):
        try:
            return self.p1.evaluate(x) / self.p2.evaluate(x)
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return float('nan')


poly_div = Div(Add(Int(10), Mul(X(), Int(2))), Int(2))
poly_sub = Sub(Add(Int(5), X()), Mul(Int(2), X()))
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))

print(poly, " at x=2 is ", poly.evaluate(2) )
print(poly_div, " at x=2 is ", poly_div.evaluate(2))
print(poly_sub, " at x=2 is ", poly_sub.evaluate(2))

# Test case 1: Division and Subtraction in a larger expression
larger_expr = Add(
    Div(Mul(Int(5), X()), Int(2)),
    Sub(Add(Int(3), X()), Mul(X(), Int(4)))
)
print("Result for larger_expr",larger_expr, " at x = 3 is: ", larger_expr.evaluate(3))

# Test case 2: Complex expression involving all operations
complex_expr = Add(
    Mul(Int(2), X()),
    Sub(
        Div(Add(Int(8), X()), Int(2)),
        Mul(Int(3), X())
    )
)
print("Result for complex_expr",complex_expr, " at x = 3 is: ", complex_expr.evaluate(3))

# Test case 3: Expression with nested operations
nested_expr = Add(
    Mul(Int(2), Div(Add(X(), Int(3)), Int(2))),
    Sub(
        Add(Int(5), Mul(X(), Int(2))),
        Mul(X(), Div(Int(4), X()))
    )
)
print("Result for nested_expr", nested_expr, " at x = 3 is: ",nested_expr.evaluate(3))
