#Nhập từ bàn phím
print("========CHƯƠNG TRÌNH QUY ĐỔI TIỀN TỆ=======")
tien = float(input("Nhập số tiền cần chuyển đổi:"))
nguon_tien = str(input("Nhập loại tiền tệ nguôn (USD, EUR, JPY, GBP, VND, CNY):"))
dich_tien = str(input("Nhập loại tiền tệ đích (USD, EUR, JPY, GBP, VND, CNY):"))

#Chuyển đổi
match nguon_tien:
    case "USD":
        match dich_tien:
            case "EUR":
                tien = tien * 0.92
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}€")
            case "JPY":
                tien = tien * 150.00
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case "GBP":
                tien = tien * 0.79
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}£")
            case "VND":
                tien = tien * 24700
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}₫")
            case "CNY":
                tien = tien * 7.20
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case _:
                print("Đích tiền tệ không hợp lệ.")

    case "EUR":
        match dich_tien:
            case "USD":
                tien = tien * 1.18
                print("-"*20) 
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}$")
            case "JPY":
                tien = tien * 182,57
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case "GBP":
                tien = tien * 0.87
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}£")
            case "VND":
                tien = tien * 30766.58
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}₫")
            case "CNY":
                tien = tien * 8.15
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case _:
                print("Đích tiền tệ không hợp lệ.")

    case "GBP":
        match dich_tien:
            case "EUR":
                tien = tien * 1.35
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}€")
            case "USD":
                tien = tien * 1.35
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}$")
            case "JPY":
                tien = tien * 209.03
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case "VND":
                tien = tien * 35218.00
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}₫")
            case "CNY":
                tien = tien * 9.33
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case _:
                print("Đích tiền tệ không hợp lệ.")

    case "JPY":
        match dich_tien:
            case "USD":
                tien = tien * 0.0065
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}$")
            case "EUR":
                tien = tien * 0.0055
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}€")
            case "GBP":
                tien = tien * 0.0048
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}£")
            case "VND":
                tien = tien * 168.46
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}₫")
            case "CNY":
                tien = tien * 0.045
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case _:
                print("Đích tiền tệ không hợp lệ.")

    case "VND":
        match dich_tien:
            case "USD":
                tien = tien * 0.00027
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}$")
            case "EUR":
                tien = tien * 0.000033
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}€")
            case "GBP":
                tien = tien * 0.000028
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}£")
            case "JPY":
                tien = tien * 0.0059
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case "CNY":
                tien = tien * 0.00026
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case _:
                print("Đích tiền tệ không hợp lệ.")

    case "CNY":
        match dich_tien:
            case "EUR":
                tien = tien * 0.12
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}€")
            case "USD":
                tien = tien * 0.14
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}$")
            case "GBP":
                tien = tien * 0.10
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}£")
            case "JPY":
                tien = tien * 22.41
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}¥")
            case "VND":
                tien = tien * 3510.40
                print("-"*20)
                print(f"Số tiền sau khi quy đổi là {tien:,.2f}₫")
            case _:
                print("Đích tiền tệ không hợp lệ.")

    case _:
        print("Nguồn tiền tệ không hợp lệ.")    