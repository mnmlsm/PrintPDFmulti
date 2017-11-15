p = int(input("How many pages are there in the PDF you want to print? "))
m = int(input("Do you want to print 2 or 4 pages per side? "))

s = ""

if m == 2:
    for n in range(1, p+1, 4):
        if n <= p:
            s+=str(n)
            s+=str(",")
        if n+2 <= p:
            s+=str(n+2)
            s+=str(",")
        if n+3 <= p:
            s+=str(n+3)
            s+=str(",")
        if n+1 <= p:
            s+=str(n+1)
            s+=str(",")
    s = s.rstrip(",")
    print("Copy string below into the 'pages to print' box.")
    print(s)
    print("In print options select 2 to a page, double sided, open to left (short side)")

if m == 4:
    for n in range(1, p+1, 8):
        if n <= p:
            s+=str(n)
            s+=str(",")
        if n+1 <= p:
            s+=str(n+1)
            s+=str(",")
        if n+4 <= p:
            s+=str(n+4)
            s+=str(",")
        if n+5 <= p:
            s+=str(n+5)
            s+=str(",")
        if n+6 <= p:
            s+=str(n+6)
            s+=str(",")
        if n+7 <= p:
            s+=str(n+7)
            s+=str(",")
        if n+2 <= p:
            s+=str(n+2)
            s+=str(",")
        if n+3 <= p:
            s+=str(n+3)
            s+=str(",")
    s = s.rstrip(",")
    print("Copy string below into the 'pages to print' box.")
    print(s)
    print("In print options select 4 to a page, double sided, open to top (short side)")

else:
    raise ValueError("Invalid inputs")
