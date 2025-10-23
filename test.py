def broke(q,a,b,c):
    total = 0
    while q != 0:
        total = total + 1
        q = q - 1
        a = a + 1
        if a == 35:
            a = 0
            q = q + 30
        total = total + 1
        q = q - 1
        b = b + 1
        if b == 100:
            a = 0
            q = q + 60
        total = total + 1
        q = q - 1
        c = c + 1
        if c == 10:
            c = 0
            q = q + 9
    print(f"Martha played {total} times before going broke.")
broke(48,3,10,4)
        