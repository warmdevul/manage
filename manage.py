from tabulate import tabulate

stt = 1
table = []
table_new = []
def getInfor():
 file = open("manage.txt", mode="r", encoding="utf-8-sig")
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 global stt
 global table
 table = [[stt, ten, lop, sdt, que],]
 stt += 1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
 sinhvien = file.readline()
 sv = sinhvien.split(";")
 ten = sv[0]
 lop = sv[1] 
 sdt = sv[2]
 que = sv[3].strip()
 table.append([stt, ten, lop, sdt, que])
 stt +=1
getInfor()
print("1. Information\n" + "2. Search\n" + "3. Edit\n" + "4. Quit\n")
mode = int(input("Choose your mode: "))
if mode == 1:
 print(tabulate(table, headers=["STT", "Ten", "Lop", "So Dien Thoai", "Que Quan"], tablefmt="fancy_grid"))
