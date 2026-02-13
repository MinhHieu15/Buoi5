m = float(input("Xin mời nhập cân nặng của bạn:"))
h = float(input("Xin mời nhập chiều cao của bạn:"))

bmi = m / h**2

result = "Thiếu cân" if bmi < 18.5 else ( "Bình thường" if 18.5 <= bmi < 24.9 else ( "Thừa cân" if 25 <= bmi < 29.9 else "Béo phì" ))

print("-"*20)
print("Chỉ số BMI của bạn là:",bmi)
print(f"Tình trạng cơ thể của bạn là:{result}")