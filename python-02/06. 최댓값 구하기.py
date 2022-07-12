# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

import numbers
from unittest import result


nnumbers = [0, 20, 100]
t = 0
for i in numbers:
    if t == 0 or i > t:
        t = i
print(t)
