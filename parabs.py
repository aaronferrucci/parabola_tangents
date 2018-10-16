from sympy import *
# init_printing(use_unicode=True)
x, x1, x2 = symbols('x x1 x2')
f = x**2 + 1
g = -x**2 - 2*x - 1
df = diff(f, x)
dg = diff(g, x)
x2s = solve(df.subs(x, x1) - dg.subs(x, x2), x2)
x1s = solve((f.subs(x, x1) - g.subs(x, x2s[0])) / (x1 - x2s[0]) - df.subs(x, x1), x1)
x2s[0].subs(x1, x1s[0])
x2s[0].subs(x1, x1s[1])

# print out x components of pts1 in R-evaluable syntax
print "pts1.x = c(" + str(x1s[0]), ", ", str(x2s[0].subs(x1, x1s[0])), ")"

m = df.subs(x, x1s[0])
delta = 3
