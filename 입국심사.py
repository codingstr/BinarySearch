# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    # left: 최소시간, right: 최대 시간
    left, right = 1, min(times)*n
    # 입국심사를 하는데, 걸리는 시간의 총합이 가장 작은 것을 찾는다..
    while left <= right:
        # 중앙값: 심사위원에게 주어진 시간
        mid = (left+right)//2
        # 모든 심사위원이 처리한 사람 수 
        passedNum = 0
        for time in times:
            passedNum += mid // time
        # 대기 중인 사람보다 더 많이 처리하면 mid를 줄일 수 있다.
            if passedNum >= n:
                right = mid-1
                answer = mid
                break
        # 대기 중인 사람보다 더 적게 처리하면 mid가 커져야 한다.
        if passedNum < n:
            left = mid+1

    return answer