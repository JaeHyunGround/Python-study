# 1번 문제
# >>> shirt 가 출력됨!
# 3번째 조건과 4번째 조건이 참이 되는데 먼저 참이 되는 조건이 3번째 조건이므로 "shirt" 가 출력됨.
a = "Life is too short, you need python"

if "wife" in a :
    print("wife")
elif "python" in a and "you" not in a :
    print("python")
elif "shirt" not in a :
    print("shirt")
elif "need" in a :
    print("need")
else :
    print("none")

# 2번 문제
result = 0
i = 1
while i <= 1000 :
    if (i % 3 == 0) : # 빈 칸
        result = result + i
    i = i + 1

print(result)

# 3번 문제 (내가 짠 코드)
while i < 6 :
    print("*" * i)
    i = i + 1

# 3번 문제 (책에 있는 코드에서 빈 칸 채우기)
i = 0
while True :
    i = i + 1
    if (i > 5) :
        break
    print("*" * i)

# 4번 문제 // range(a, b) => a 이상 b 미만
for i in range(0, 100) :
    print(i + 1)

# 5번 문제
results = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
student = 0
sum = 0
for x in results :
    student = student + 1
    sum = sum + x
print(sum / student)

# 6번 문제 (리스트 내포 사용 x)
numbers = [1, 2, 3, 4, 5]
newnums = []

for n in numbers :
    if (n % 2 != 0) :
        newn = n * 2
        newnums.append(newn)
print(newnums)


# 6번 문제 (리스트 내포 사용)
numbers = [1, 2, 3, 4, 5]

result = [n * 2 for n in numbers if n % 2 != 0]
print(result)