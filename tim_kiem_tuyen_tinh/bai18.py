def tim_kiem_ma_tran(M, x):
    for i in range(len(M)):        # Duyệt qua từng dòng
        for j in range(len(M[i])): # Duyệt qua từng cột của dòng đó
            if M[i][j] == x:
                return (i, j)
    return (-1, -1)