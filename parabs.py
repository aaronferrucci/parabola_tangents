from sympy import *
# init_printing(use_unicode=True)
x, x1, x2 = symbols('x x1 x2')
f = x**2 + 1
g = -x**2 - 2*x - 1
df = diff(f, x)
dg = diff(g, x)
x2s = solve(df.subs(x, x1) - dg.subs(x, x2), x2)
x1s = solve((f.subs(x, x1) - g.subs(x, x2s[0])) / (x1 - x2s[0]) - df.subs(x, x1), x1)

delta = 4
# print pts1, line1 in R-evaluable syntax
x1_val = x1s[0]
x2_val = x2s[0].subs(x1, x1_val)
x1_val, x2_val = min(x1_val, x2_val), max(x1_val, x2_val)

y1_val = f.subs(x, x1_val)
y2_val = g.subs(x, x2_val)
print "pts1 <- data.frame(x=c(%s, %s), y=c(%s, %s))" % (str(x1_val), str(x2_val), str(y1_val), str(y2_val))
print "# pts1.x: " + str([N(x_tmp) for x_tmp in (x1_val, x2_val)])
print "# pts1.y: " + str([N(y_tmp) for y_tmp in (y1_val, y2_val)])

m = df.subs(x, x1_val)
print "line1 <- data.frame(x = c(%s, %s), y = c(%s, %s))" % (str(x2_val - delta), str(x1_val + delta), str(y2_val - m * delta), str(y1_val + m * delta))
print "# line1.x: " + str([N(x_tmp) for x_tmp in (x2_val - delta, x1_val + delta)])
print "# line1.y: " + str([N(y_tmp) for y_tmp in (y2_val - m * delta, y1_val + m * delta)])

# print pts2, line2 in R-evaluable syntax
x1_val = x1s[1]
x2_val = x2s[0].subs(x1, x1_val)
x1_val, x2_val = min(x1_val, x2_val), max(x1_val, x2_val)
y1_val = g.subs(x, x1_val)
y2_val = f.subs(x, x2_val)
print "# pts2.x: " + str([N(x_tmp) for x_tmp in (x1_val, x2_val)])
print "# pts2.y: " + str([N(y_tmp) for y_tmp in (y1_val, y2_val)])

print "pts2 <- data.frame(x=c(%s, %s), y=c(%s, %s))" % (str(x1_val), str(x2_val), str(y1_val), str(y2_val))
m = df.subs(x, x2_val)
print "line2 <- data.frame(x = c(%s, %s), y = c(%s, %s))" % (str(x2_val - delta), str(x1_val + delta), str(y2_val - m * delta), str(y1_val + m * delta))
