""" def lang(x):
    print("English")
lang("This is english language.") """

""" input = input("type sentence in english or french")
print(input.split())
lf = []
lf.append(input.split(" "))
print(lf) """
# if something > something:
    #print english
#elif something2 > something1:
    #print french
#elif something1 == something2:
    #print french

T = 0
t = 0
S = 0
s = 0

def lang(x):
    t = 0
    for char in x:
        if "T" or "t":
            t = t + 1
        elif "S" or "s":
            s = s + 1

lang("s s t")

if t > s:
    print("english")
elif s > t:
    print("french")
elif t == s:
    print("french")
