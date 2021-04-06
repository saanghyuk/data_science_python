# requires python 3.7+
# https://dojang.io/mod/page/view.php?id=2469
# https://soooprmx.com/archives/8629

import asyncio
import time

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")

#     await say_after(1, 'hello')
#     await say_after(2, 'world')

#     print(f"finished at {time.strftime('%X')}")

# async def main_concurrently():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))

#     task2 = asyncio.create_task(
#         say_after(2, 'world'))

#     print(f"started at {time.strftime('%X')}")

#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main()) #약 3초 걸림
# asyncio.run(main_concurrently()) # 2초만에 실행 끝남



# Async For이나 Async With 둘다 중간 중간 다른 코루틴들이 있으면 비동기적으로 실행되는 것임. ㄴ
# Async with : 클래스나 함수를 비동기로 처리한 뒤 결과를 반환하는 문법.


class AsyncAdd:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  async def __aenter__(self):
    # await asyncio.sleep(1.0)
    print('AsyncAdd', self.a)
    print('AsyncAdd', self.b)
    return self.a + self.b  # __aenter__에서 값을 반환하면 자동으로 하단의 as에 지저어한 변수에 들어감

  async def __aexit__(self, exc_type, exc_value, traceback): #Async with as를 완전히 벗어나면 실행이 됨.
    print('finish')

class AsyncPrint:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  async def __aenter__(self):
    # await asyncio.sleep(1.0)
    print('AsyncPrint', self.a)
    print('AsyncPrint', self.b)
    return self.a + self.b  # __aenter__에서 값을 반환하면 자동으로 하단의 as에 지저어한 변수에 들어감

  async def __aexit__(self, exc_type, exc_value, traceback): #Async with as를 완전히 벗어나면 실행이 됨.
    print('finish')




async def main():
  async with AsyncAdd(1, 2) as result:
    print(result)
  async with AsyncPrint(3, 4) as result2:
    print(result2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


# # Async for 비동기로 반복하는 문법
# import asyncio

# class AsyncCounter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop

#     def __aiter__(self):
#         return self

#     async def __anext__(self):
#         if self.current < self.stop:
#             await asyncio.sleep(1.0)
#             r = self.current
#             self.current += 1
#             return r
#         else:
#             raise StopAsyncIteration

# async def main():
#     async for i in AsyncCounter(3):    # for 앞에 async를 붙임
#         print(i, end=' ')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
