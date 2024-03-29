#ex11.py 비트(2진수) 연산자: &, |, ^, ~
# 2진수로 연산할 때 0, 1 비교하는 거
# &: 둘 다 1이어야 하고, 마지막 자릿수 안 맞으면 비움
# |: 둘 중 하나라도 1이면 되고, 마지막 자릿수 안 맞아도 1이면 채움
# ^: 서로 입력이 다른 경우만 1이 나옴
#~: 보수 0은 1로, 1은 0으로, 양수면 음수로 바꿔버림 (3의 보수는 -4)

a = 27
b = 33
#a=22 22를 각 진수로 변환
print("2진수: ", bin(a)) #0b10110
print("8진수: ", oct(a)) #0o26
print("16진수: ", hex(a)) #0x16

print("2진수 a: ", bin(a))
print("2진수 b: ", bin(b))
print("a & b: ", bin(a&b)) # and 연산
print("a | b: ", bin(a|b)) # or 연산
print("a ^ b: ", bin(a^b)) # xor 연산
print("~b: ", bin(~b)) # complement(not) 연산