import sys

input = sys.stdin.readline

n = int(input()) - 1# 인덱스로 맞추기 위해서
string = list("WelcomeToSMUPC")


print(string[n % 14])