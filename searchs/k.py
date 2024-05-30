def linear_search(arr: object, target: object) -> object:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 51321313213], 5))















"""
Linear search bu bizga algoritmlarni qidirishda
 yordam beradi bu juda tez ishlaydi lekin ,1 ta yomon tarafi katta toplamlarda sekin ishlaydi bu uning zaifligi """