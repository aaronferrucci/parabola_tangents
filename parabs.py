from sympy import *
import sys

try:
    (a0, b0, c0, a1, b1, c1) = [ float(arg) for arg in sys.argv[1:]]
except:
    print "Usage: %s <a0> <b0> <c0> <a1> <b1> <c1>" % sys.argv[0]
    sys.exit(1)

# init_printing(use_unicode=True)

x, x1, x2 = symbols('x x1 x2')
f = a0*x**2 + b0*x + c0
g = a1*x**2 + b1*x + c1
df = diff(f, x)
dg = diff(g, x)
x2s = solve(df.subs(x, x1) - dg.subs(x, x2), x2)
x1s = solve((f.subs(x, x1) - g.subs(x, x2s[0])) / (x1 - x2s[0]) - df.subs(x, x1), x1)

delta = 3
print "# produced by parabs.py, sympy"
print "# f: %s" % str(f)
print "# g: %s" % str(g)
for i in range(0, len(x1s)):
    # print pts<i>, line<i> in R-evaluable syntax
    x1_val = x1s[i]

    # x1 values were computed using their slope on f. For each x1, that slope
    # is the slope of the line.
    m = df.subs(x, x1_val)

    # solve for the other point, as a function of this x1
    x2_val = x2s[0].subs(x1, x1_val)

    # 'x1' is left-most
    x1_val, x2_val = min(x1_val, x2_val), max(x1_val, x2_val)

    # y values are on f or g, depending on slope
    if m < 0:
        y1_val = f.subs(x, x1_val)
        y2_val = g.subs(x, x2_val)
    else:
        y1_val = g.subs(x, x1_val)
        y2_val = f.subs(x, x2_val)

    print "pts%d <- data.frame(x=c(%s, %s), y=c(%s, %s))" % \
      (i + 1, str(x1_val), str(x2_val), str(y1_val), str(y2_val))

    print "line%d <- data.frame(x = c(%s, %s), y = c(%s, %s))" % \
      (i + 1, str(x1_val - delta), str(x2_val + delta), \
      str(y1_val - m * delta), str(y2_val + m * delta))

