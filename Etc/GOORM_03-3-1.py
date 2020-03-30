# 비타알고 시즌3 03월 3주차 DDR 문제


import sys

input = sys.stdin.readline

def solution():
	N = int(input())
	music = {}
	res = 1
	for _ in range(N):
		btn, play = input().split()
		music[play] = music.get(play,0)+1
		if music[play] >2:
			res = 0
			break
			
	print(res)

if __name__ == "__main__":
    solution()