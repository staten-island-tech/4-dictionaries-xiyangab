#assesment practice 1
""" def lang(x):
    t = 0
    s = 0
    for char in x:
        if char == "T" or char == "t":
            t = t + 1
        elif char == "S" or char == "s":
            s = s + 1
    if t > s:
        print("english")
    elif s >= t:
        print("french")

lang("TtSsS")
 """
#assesment practice 2
def spaces(y,t):
    x = 0
    for char in y and t:
        if char == "C":
            x = x + 1
    print(x)
spaces("CCCCCCCCCC","C.C.C.C.C.")