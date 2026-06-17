def insertion_sort_students(students):
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0:
            s = students[j]
            # s phải "nhỏ hơn" key thì mới shift (tức s cần đứng sau key)
            if s[1] < key[1] or (s[1] == key[1] and s[0] > key[0]):
                students[j + 1] = students[j]
                j -= 1
            else:
                break
        students[j + 1] = key
    return students
 
students = [('An', 8), ('Ba', 9), ('Cu', 8)]
print("Bài 14:", insertion_sort_students(students))  # [('Ba',9),('An',8),('Cu',8)]