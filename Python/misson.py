# 1번 문제
Korea = 80
English = 75
Math = 55

avg = (Korea + English + Math) / 3
print(avg)

# 2번 문제
num = 14

if(num % 2 == 0):
    print("해당 숫자는 짝수입니다.")
else:
    print("해당 숫자는 홀수입니다.")

# 3번 문제 (슬라이딩)
hongnum = "881120-1068234"
front = hongnum[:6]
back = hongnum[7:]

print(front)
print(back)

# 4번 문제 (인덱싱)
pin = "881120-1068234"

if(pin[7] == "1"):
    print("이 사람의 성별은 남자입니다.")
elif(pin[7] == "2"):
    print("이 사람의 성별은 여자입니다.")


# 5번 문제 (replace => 재배치)
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6번 문제 (sort => 정렬, reverse => 거꾸로)
numlist = [1, 3, 5, 4, 2]
numlist.sort()
numlist.reverse()
print(numlist)

# 7번 문제 => join 함수가 이해가 잘 안되네 => join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수. => "구분자".join(리스트)
list = ["Life", "is", "too", "short"]
s = " ".join(list)
print(s)