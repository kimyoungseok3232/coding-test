# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    genre_play = {}
    for genre, play in zip(genres, plays):
        genre_play[genre] = genre_play.get(genre, 0) + play
    
    genre_list = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_list:
            genre_list[genre] = []
        genre_list[genre].append((play, idx))
    
    for key, val in sorted(genre_play.items(), key = lambda x: -x[1]):
        answer.extend(sorted(genre_list[key], key= lambda x: (-x[0], x[1]))[:2])
    
    return [x[1] for x in answer]