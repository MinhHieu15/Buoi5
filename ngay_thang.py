#Nhập từ bàn phím
month = int(input("Nhập tháng (1-12):"))
year = int(input("Nhập năm:"))

#match case
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Tháng có 31 ngày.")
    case 4 | 6 | 9 | 11:
        print("Tháng có 30 ngày")
    case 2:
        if (year % 4 == 0) and (year % 100 == 0) or (year % 400 == 0):
            print("Tháng 2 có 29 ngày")
        else:
            print("Tháng có 28 ngày")
    case _:
        print("Không hợp lệ")