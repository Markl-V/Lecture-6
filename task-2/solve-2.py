# TODO: Вставить сюда код задачи 2.
count = int(input())
total_sum = 0

for _ in range(count):
    num = int(input())
    if num%10 == 4 and num%6 == 0: 
        total_sum += num

print(total_sum)
