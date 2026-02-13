
#nhập từ bàn phím
while True:
    print("\n ===Chương trình tính học phí===")
    print("Bạn là học sinh chính quy hay không chính quy?")
    phan_loai= float(input("Nếu bạn là chính quy bấm 1 nếu bạn là không chính quy bấm 0:"))


#Phân loại
    if phan_loai == 1:
        i = float(input("Mời nhập số tín chỉ đã đăng kí:"))
        hoc_phi = (i > 15)*90*i + (i <= 15)*90*i
        tb_giam_hp = (i > 15)* \
        f"Do số tín chỉ đã đăng kí >15, giảm 10$ với mỗi tín chỉ (Mặc định là 100$): -{i*10:,.0f}$"

        print("-"*20)
        (tb_giam_hp !="") and print(tb_giam_hp)
        print(f"Số học phí cần trả: {hoc_phi:,.0f}$")
        break
    elif phan_loai == 0:
        i = float(input("Mời nhập số tín chỉ đã đăng kí:"))
        hoc_phi = i * 150

        print("-"*20)
        print(f"Số học phí cần trả: {hoc_phi:,.0f}$")
        break
    else:
        print("Cú pháp của bạn không hợp lệ")
