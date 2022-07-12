# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

from unittest import result

numbers = [-10, -100, -30]
t = 0
for i in numbers:
    if t == 0 or i < t:
        t = i
print(t)
    
