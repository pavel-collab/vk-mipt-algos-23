'''
Дана последовательность чисел. Нужно найти длину максимальной возрастающей подпоследовательности.

Нельзя просто пройтись по последовательности и вычеркнуть все лишнее. В последовательности
может быть несколько разных возрастающих подпоследовательностей. Контрпример:
[10, 3, 20, 4, 1, 5, 6] 
Возрастающие подпоследовательности [10, 20], [3, 4, 5, 6], [1, 5, 6]

Заводим массив dp размером = размеру исходной последовательности 
(тогда индекс в массиве dp соответствует индексу в массиве с последовательностью).
Для каждого элемента в последовательности в массив dp записываем длину максимальной возрастающей
подпоследовательности, членом которой он может быть.
'''

def foo(arr: list) -> int:
    if len(arr) == 0 or len(arr) == 1:
        return len(arr)
    
    dp = [1 for _ in range(len(arr))]

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] <= arr[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)

def main():
    # arr = [3, 1, 4, 7, 2, 11, 9]
    arr = [10, 3, 20, 4, 1, 5, 6] 
    print(foo(arr))

if __name__ == '__main__':
    main()