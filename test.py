num = []
low = []
up = []
letter = []
def pw(x):
    for char in x:
        letter.append(char)
        if char == "A" or "B" or "C" or "D":
            up.append(char)
        elif char == "a" or "b" or "c" or "d":
            low.append(char)
        elif char == "1" or "2" or "3" or "4"