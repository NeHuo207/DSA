def so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return a[i], i
    return -1