a = int(input("Nhập số lượng tam giác : "))
for chieudoc in range(a):
 for chieungang in range(a):
     if chieungang == range(a) or chieungang < chieudoc or chieungang == chieudoc :
      print("*",end="")
 print()