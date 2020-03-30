# 비타알고 시즌3 03월 2주차 경품 추첨 문제

import sys

input = sys.stdin.readline

def solution():
	res = ''
	N, M = input().split()
	students = input().split()
	numbers = input().split()
	cnts = {}
	for student in students:
		cnts[student] = cnts.get(student,0)+1
	
	for number in numbers:
		res += str(cnts.get(number,'0'))
		res += ' '
	print(res)
	
if __name__ == "__main__":
    solution()