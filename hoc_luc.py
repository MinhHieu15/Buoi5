diem = float(input("Xin mời nhập điểm trung bình:"))

result = "Giỏi" if diem >= 8.5 else ( "Khá" if 7.0 <= diem <8.5 else ("Trung bình" if 5.0 < diem <7.0 else "Kém"))

print("-"*20)
print("Phân loại học sinh của bạn là:",result)