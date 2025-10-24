def broke(q,a,b,c):
    total = 0
    while q > 0:
        print(q,a,b,c)
        q = q - 1
        total = total + 1
        a = a + 1
        if a == 35:
            a = 0
            q = q + 30
        q = q - 1
        total = total + 1
        b = b + 1        
        if b == 100:
            b = 0
            q = q + 60
        q = q - 1
        total = total + 1
        c = c + 1
        if c == 10:
            c = 0
            q = q + 9
    print(f"Martha played {total} times before going broke.")
broke(77,4,9,3)
broke(48,3,10,4)