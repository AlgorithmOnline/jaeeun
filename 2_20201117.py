import collections
def solution(phone_book):
    answer = True
    phone_book = collections.deque(phone_book)
    param = 0
    while len(phone_book)>=param:
        param+=1
        travel= phone_book.popleft()
        if any(list(map(lambda a: a.startswith(travel), phone_book))):
            answer=False
            break
        phone_book.append(travel)
    return answer
