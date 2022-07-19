import math

def lcm(a, b):
    return int((a*b)//(math.gcd(a,b)))


def coeffAndSign(input):
        fractions = []
        curr = ""
        found = False
        a,b,c,d,op = 0,1,0,1,''
        for i in input:
                if i == '/' and not found:
                        curr += i
                        found = True
                        continue

                if i in ['+', '-', '*', '/']:
                        if found:
                                fractions.append(curr)
                                curr = ""
                                op = i
                                found = False
                                continue

                curr += i
        if curr[0] in ['*', '/']:
                print("invalid entry! try again")
                return 0,1,0,1,'I'
        fractions.append(curr)
        frac = []
        #splits the fractions array's elements into string that'll be converted to int
        #fractions array currently contains : ["a/b", "c/d"]
        for f in fractions:
                curr_frac = f.split('/')
                frac.append(int(curr_frac[0]))
                frac.append(int(curr_frac[1]))
        #frac array contains : [a,b,c,d]
        a,b,c,d = frac
        return a,b,c,d,op

#calculate the lcm of denominators and add/subtract as we do with hands
def addSubtract(a,b,c,d,op):
        x, y = 0, 1
        if op == '+':
                x = int((a*(lcm(b,d)//b) + c*(lcm(b,d)//d)))
                y = int(lcm(b,d))
                x, y = reduceForm(x, y)
        else:
                c *= -1
                x = int((a*(lcm(b,d)//b) + c*(lcm(b,d)//d)))
                y = int(lcm(b,d))
                x, y = reduceForm(x, y)
        return x,y

# for *: a*c/b*d and for / : a*d/b*c
def multiDivision(a,b,c,d,op):
        x,y = 0,1
        if op == '*':
                x,y = a*c, b*d
                x,y = reduceForm(x,y)
        else:
                x,y = a*d, b*c
                x,y = reduceForm(x, y)
        return x,y

# simply divide num and den by thei