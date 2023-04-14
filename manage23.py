from tabulate import tabulate

numerical_order = 1
table = []
file = open("manage.txt", mode="r", encoding="utf-8-sig")
def getInfor():
    global numerical_order
    global table
    students = file.readline()
    while students != "":
        student = students.split(";")
        full_name = student[0]
        grade = student[1] 
        contact = student[2]
        location = student[3].strip()
        table.append([numerical_order, full_name, grade, contact, location])
        numerical_order += 1
        students = file.readline()
def search():
    to_search = str(input("Nhap tu khoa tim kiem: "))
    for search in table:
        if search == to_search:
            print("already")
def getMode():
    print("\n1. Information\n" + "2. Search\n" + "3. Edit\n" + "4. Quit\n")
    mode = int(input("Choose your mode: "))
    if mode == 1:
        print(tabulate(table, headers=["STT", "Ten", "Lop", "So Dien Thoai", "Que Quan"], tablefmt="fancy_grid"))
        getMode()
    elif mode == 2:
        search()
    else:
        pass
if __name__=="__main__":
    getInfor()
    getMode()
