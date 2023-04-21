def ten(s):
    a=s.split()
    ho=a[0]
    ten=a[len(a)-1]
    dem=" ".join(a[1:len(a)-1])
    print("Họ :",ho)
    print("Đệm :",dem)
    print("Tên :",ten)
    q="Tên quá ngắn"
    i="Tên quá dài"
    o="Tên bình thường"
    k=len(a)
    if k<=2:
        kq=q
        print(kq)
        return 
    if k>4:
        kq=i
        print(kq)
        return 
    if (k==2 or k==3 or k==4):
        kq=o
        print(kq)
        return 
s=input("Mời nhập họ tên: ")
ten(s)
