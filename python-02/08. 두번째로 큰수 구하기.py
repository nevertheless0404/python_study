# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지


import numbers


numbers = [0, 20, 100]
numbers = set(numbers)
numbers = list(numbers)
numbers.sort()

print(numbers[-2])
