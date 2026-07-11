def hien_thi_menu():
    print("\n========= QUẢN LÝ DANH BẠ =========")
    print("1. Thêm liên hệ mới")
    print("2. Tìm kiếm số điện thoại theo tên")
    print("3. Tìm kiếm theo số điện thoại")
    print("4. Đếm số liên hệ bắt đầu bằng chuỗi số")
    print("5. Thoát chương trình")
    print("===================================")

def main():
    danh_ba = []
    
    while True:
        hien_thi_menu()
        luachon = input("Nhập lựa chọn của bạn (1-5): ").strip()
        
        if luachon == "1":
            ten = input("Nhập tên liên hệ: ").strip()
            sdt = input("Nhập số điện thoại: ").strip()
            danh_ba.append({"ten": ten, "sdt": sdt})
            print("-> Thêm liên hệ thành công!")
            
        elif luachon == "2":
            ten_tim = input("Nhập tên cần tìm: ").strip().lower()
            found = False
            for contact in danh_ba:
                if contact["ten"].lower() == ten_tim:
                    print(f"-> Kết quả: {contact['ten']} - SĐT: {contact['sdt']}")
                    found = True
            if not found:
                print("-> Không tìm thấy tên này trong danh bạ.")
                
        elif luachon == "3":
            sdt_tim = input("Nhập số điện thoại cần tìm: ").strip()
            found = False
            for contact in danh_ba:
                if contact["sdt"] == sdt_tim:
                    print(f"-> Kết quả: {contact['ten']} - SĐT: {contact['sdt']}")
                    found = True
                    break  # SĐT thường là duy nhất nên có thể dừng sớm
            if not found:
                print("-> Không tìm thấy số điện thoại này.")
                
        elif luachon == "4":
            prefix = input("Nhập chuỗi số đầu (ví dụ: 090): ").strip()
            count = 0
            print("Các liên hệ trùng khớp:")
            for contact in danh_ba:
                if contact["sdt"].startswith(prefix):
                    print(f"   {contact['ten']} - {contact['sdt']}")
                    count += 1
            print(f"-> Tổng số liên hệ tìm thấy: {count}")
            
        elif luachon == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()