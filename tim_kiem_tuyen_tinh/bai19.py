def tim_kiem_sv(ds_sv, ma_sv_can_tim):
    for sv in ds_sv:
        if sv['ma_SV'] == ma_sv_can_tim:
            print("--- Thông tin sinh viên tìm thấy ---")
            print(f"Mã SV: {sv['ma_SV']}")
            print(f"Họ tên: {sv['ho_ten']}")
            print(f"Điểm TB: {sv['diem_TB']}")
            return
    print(f"Không tìm thấy sinh viên có mã: {ma_sv_can_tim}")