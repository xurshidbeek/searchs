def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    print(binary_search([13232, 233, 356, 45, 51321313213], 5))











    """
    
    BInary search bu bu ham algoritmlarni qidiradi va bu katta hajimdagi malumotlarni yaxshi va tyez qidiradi
      ammo bu tez qidirishi uchun malumotlar tartiblangan bolishi lozim """