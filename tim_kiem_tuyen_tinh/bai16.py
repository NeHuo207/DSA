def phan_tu_gan_x_nhat(a, x):
    if not a:
        return None
    
    min_diff = abs(a[0] - x)
    idx_gan_nhat = 0
    val_gan_nhat = a[0]
    
    for i in range(1, len(a)):
        diff = abs(a[i] - x)
        if diff < min_diff:
            min_diff = diff
            idx_gan_nhat = i
            val_gan_nhat = a[i]
            
    return val_gan_nhat, idx_gan_nhat