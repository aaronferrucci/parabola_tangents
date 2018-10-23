from sympy import *
# init_printing(use_unicode=True)

x, x1, x2 = symbols('x x1 x2')
a0, b0, c0, a1, b1, c1 = symbols('a0 b0 c0 a1 b1 c1')

f = a0*x**2 + b0*x + c0
g = a1*x**2 + b1*x + c1
df = diff(f, x)
dg = diff(g, x)

x2s = solve(df.subs(x, x1) - dg.subs(x, x2), x2)
x1s = solve((f.subs(x, x1) - g.subs(x, x2s[0])) / (x1 - x2s[0]) - df.subs(x, x1), x1)
print('$' + latex(x1s) + '$')

