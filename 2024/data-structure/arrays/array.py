# Python arrays 

# Time Complexity
# 접근하거나 수정 또는 end에 추가/삭제하는 데 O(1)
# 다른 곳에 삽입/삭제하는 데 O(n)

# Space Complexity
# 필요한 공간 = (n 이상인 배열의 용량) * item의 크기
# 배열의 용량이 2배로 늘어나 2n이 되더라도 상수 배수는 빅오 표기법에서 무시되므로 여전히 O(n)

import sys

def array_test():
    ar = [3, 2, 4, 5]

    print("size:", len(ar)) # size: 4
    print("capacity:", sys.getsizeof(ar)) # capacity: (auto-size) ex)88

    print("is Empty?",len(ar) == 0) # is Empty? False

    ar.pop()

    ar.append(6)

    print(ar) # [3, 2, 4, 6]

    print("Value of Index 2:", ar[2]) # Value of Index 2: 4
    # index of given value
    print("Index of 4:", ar.index(4)) # Index of 4: 2

    # remove the first occurence of item with given value
    ar.remove(4) 
    print("Removed 4:", ar) # Removed 4: [3, 2, 6]


    ar.reverse()
    print("reversed", ar) # reversed [6, 2, 3]
    print("sorted return", sorted(ar)) # sorted return [2, 3, 6]

    ar.insert(2, 9)
    print(ar) # [6, 2, 9, 3]

    del ar[0]
    print(ar) # [2, 9, 3]


    ar.sort()
    print("sorted in place", ar) # sorted in place [2, 3, 9]



def main():
    array_test()

if __name__ == "__main__":
    main()