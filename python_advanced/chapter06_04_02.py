# Chapter06-04-02
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체의 return을 yield라는 키워드를 통해 사용함(여러 쓰레드를 사용한 효과 내기 위한 기법).
# 실행  STOP  다른작업으로 위임 STOP 이후 그 지점부터 재실행 원리
# Non-Blocking 비동기 처리에 적합.

# Block IO(내가 뭔가 요청을 할때 모든 쓰레드나 루틴들이 멈춰 있는 것, 얘가 일을 끝내야 나머지가 일을 할 수 있는 상황)
# Block IO는 지금까지 사용하던 순차 실행을 의미함.
# Chapter06-4-2
# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행 원리
# non-blocking 비동기 처리에 적합

# BlockIO -> Thread 사용
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결
# 비순차 실행

import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 시작 시간
start = timeit.default_timer()
urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/', 'https://gmarket.co.kr/']


def fetch(url):
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    urlopen(url)
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(fetch, url)

if __name__ == '__main__':
    # 함수 실행
    main()
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Time : ', duration)