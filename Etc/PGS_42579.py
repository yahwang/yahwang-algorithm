def solution(genres, plays):
    answer = []
    records = {}
    total_genre = {}
    for idx, (i, j) in enumerate(zip(genres, plays)):
        records.setdefault(i, []).append((idx, j))
        total_genre[i] = total_genre.setdefault(i, 0) + j
    total_genre = sorted(list(total_genre.items()), key=lambda x: x[1], reverse=True)
    for genre, _ in total_genre:
        records[genre].sort(key=lambda x: x[1], reverse=True)
        answer.append(records[genre][0][0])
        if len(records[genre]) > 1:
            answer.append(records[genre][1][0])
    return answer
