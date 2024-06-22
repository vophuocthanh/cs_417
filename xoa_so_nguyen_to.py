#  Xóa các số nguyên tố

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def remove_primes(arr):
    return [x for x in arr if not is_prime(x)]

def input_array():
    input_str = input("nhap cac so nguyen, cach nhau 1 dau cach: ")
    return list(map(int, input_str.split()))

def main():
    array = input_array()
    result = remove_primes(array)
    print("Mang sau khi xoa so nguyen to:", result)

# Chạy chương trình
if __name__ == "__main__":
    main()
