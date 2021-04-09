# Python Lecture



### Module

- 게임을 만들려면, 캐릭터/인터페이스/상점 등 엄청 많은 부분이 필요함. 이걸 다 한 파일로 뭉치려면, 파일이 엄청 커지고 복잡해짐. 수정하려고 하면 어떤걸 수정해야 하는지부터 굉장히 애매함. 
- 그래서 코드를 파일 단위로 나누게 됨. 아이템은 items.py, 상점은 stores.py에 넣는것. 이런 파일 단위를 모듈이라고 함. 그리고, 코드 재사용이 가능. 



- 모듈을 가져오는 방법

  - 특정 함수만 필요할 때 - 이렇게 쓰면, 그냥 circle이라고 쓰면 됨.

  ```python
  from are import circle, square
  
  ```

from shapes import area as ar - 새로운 이름으로 사용 가능함. 

  from area import square as sq 

  from area import *  - 모든 함수 다 가져옴
  ```




#### dir

- 파일 안에서 정의된 모든 함수를 확인할 수 있게 해줌. 

- __ 더블 언더스코어 함수들, 특수변수. 

- dir을 치면, 해당 파일에서 사용할 수 있는 모든 것이 나옴. import 된 것들도 나옴. 

  ```
  print(dir())
  ```

  아래처럼 치는 경우에는 dir에  square와 circle이 나옴. 

  ```
  from area import squre, circle
  ```

  

- 네임스페이스 : 파일에서 정의된 모든 이름들. 

  즉, dir은 네임스페이스를 리턴해 주는 것. 

- 파이썬에서는 똑같은 이름으로 여러 개의 함수가 정의되어 있을 때, 가장 나중에 정의된 함수를 쓰게 됨. 



#### 자주 쓰는 모듈

- Math - `math`는 기본적인 수학 모듈입니다. 여러 수학적인 함수를 제공해 줍니다.

  ```python
  import math
  
  # 코사인 함수 (모든 삼각함수는 라디안을 사용합니다)
  print(math.cos(0))
  
  # 로그 함수
  print(math.log10(100))
  ```

- random - random 모듈은 랜덤 한 숫자를 생성하기 위한 다양한 함수들을 제공해 줍니다.

  ```python
  import random
  
  # 랜덤한 정수 1 <= N <= 20 
  print(random.randint(1, 20))
  
  # 랜덤한 소수 0 <= x <= 1
  print(random.uniform(0, 1))
  ```

- datetime - `datetime` 모듈은 날짜와 시간을 다루기 위한 다양한 '클래스'를 갖추고 있습니다. 클래스의 개념을 잘 모르셔도 이 모듈을 사용하는 데에는 문제없습니다.

  ```python
  import datetime 
  
  # 현재 시간과 날짜
  today = datetime.datetime.now()
  print(today)
  
  # 출력값을 "요일, 월 일 연도"로 포매팅
  print(today.strftime("%A, %B %dth %Y"))
  
  # 특정 시간과 날짜
  pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
  print(pi_day)
  
  # 두 datetime의 차이
  print(today - pi_day)
  ```

- os - OS는 Operating System, 즉 운영체제의 약자입니다. `os` 모듈을 통해서 파이썬으로 운영체제를 조작하거나 운영체제에 대한 정보를 가져올 수 있습니다.

  ```python
  import os
  
  # 현재 어떤 계정으로 로그인 돼있는지 확인
  print(os.getlogin())
  
  # 현재 파일의 디렉토리 확인 
  print(os.getcwd())
  
  # 현재 프로세스 ID 확인 
  print(os.getpid())
  ```

- os.path - `os.path` 모듈은 파일 경로를 다룰 때 쓰입니다.

  ```python
  import os.path
  
  # 프로젝트 디렉토리 경로 '/Users/codeit/PycharmProjects/standard_modules'
  # 현재 파일 경로 '/Users/codeit/PycharmProjects/standard_modules/main.py'
  
  # 주어진 경로를 절대 경로로
  print(os.path.abspath('..'))
  
  # 주어진 경로를 현재 디렉토리를 기준으로 한 상대 경로로
  print(os.path.relpath('/Users/codeit/PycharmProjects'))
  
  # 주어진 경로들을 병합
  print(os.path.join('/Users/codeit/PycharmProjects', 'standard_modules'))
  ```

  

- Re - 프로그래밍에서 Regular Expression (RegEx, re, 한국어로는 정규 표현식)은 특정한 규칙/패턴을 가진 문자열을 표현하는 데 사용됩니다.

  ```python
  import re 
  
  # 알파벳으로 구성된 단어들만 매칭
  pattern = re.compile('^[A-Za-z]+$')
  print(pattern.match('I'))
  print(pattern.match('love'))
  print(pattern.match('python3'))
  
  print()
  
  # 숫자가 포함된 단어들만 매칭
  pattern = re.compile('.*\d+')
  print(pattern.match('I'))
  print(pattern.match('love'))
  print(pattern.match('python3'))
  
  ```

- pickle - `pickle` 을 사용하면 파이썬 오브젝트(객체)를 바이트(byte) 형식으로 바꿔서 파일에 저장할 수 있고 저장된 오브젝트를 읽어올 수도 있습니다.

  ```python
  import pickle
  
  # 딕셔너리 오브젝트
  obj = {'my': 'dictionary'}  
  
  # obj를 filename.pickle 파일에 저장
  with open('filename.pickle', 'wb') as f:
      pickle.dump(obj, f)
  
  # filename.pickle에 있는 오브젝트를 읽어옴 
  with open('filename.pickle', 'rb') as f:
      obj = pickle.load(f)
  
  print(obj)
  ```

- json - `json` 모듈은 `pickle`과 비슷하지만 오브젝트를 JSON 형식으로 바꿔줍니다. JSON 형식에 맞는 데이터 (기본 데이터 타입들, 리스트, 딕셔너리)만 바꿀 수 있습니다.

  ```python
  import json
  
  # 딕셔너리 오브젝트
  obj = {'my': 'dictionary'}  
  
  # obj를 filename.json 파일에 저장
  with open('filename.json', 'w') as f:
      json.dump(obj, f)
  
  # filename.json에 있는 오브젝트를 읽어옴 
  with open('filename.json', 'r') as f:
      obj = json.load(f)
  
  print(obj)
  ```

- copy - `copy` 모듈은 파이썬 오브젝트를 복사할 때 쓰입니다.

  ```python
  import copy
  
  # '=' 연산자는 실제로 리스트를 복사하지 않음
  # 리스트를 복사하려면 슬라이싱을 사용하거나 copy.copy() 함수를 사용해야 함
  a = [1, 2, 3] 
  b = a
  c = a[:]
  d = copy.copy(a)
  a[0] = 4
  print(a, b, c, d)
  
  # 하지만 오브젝트 안에 오브젝트가 있는 경우 copy.copy() 함수는 가장 바깥에 있는 오브젝트만 복사함 
  # 오브젝트를 재귀적으로 복사하려면 copy.deepcopy() 함수를 사용해야 함
  a = [[1,2,3], [4,5,6], [7,8,9]]
  b = copy.copy(a)
  c = copy.deepcopy(a)
  a[0][0] = 4
  print(a, b, c)
  ```

- Sqlite3 - `sqlite3` 모듈을 통해 파이썬에서 SQLite 데이터베이스를 사용할 수 있습니다.

  ```python
  import sqlite3
  
  # 데이터베이스 연결
  conn = sqlite3.connect('example.db')
  
  # SQL 문 실행 
  c = conn.cursor()
  c.execute('''SELECT ... FROM ... WHERE ... ''')
  
  # 가져온 데이터를 파이썬에서 사용
  rows = c.fetchall()
  for row in rows:
      print(row)
  
  # 연결 종료
  conn.close()
  ```

  



### 파이썬의 모듈 검색 경로

- 파이썬은 모듈을 찾기 위해 특정 경로들을 검색함. 위 경로에 해당되는 곳들을 검색하게 됨. 

  ```python
  import sys
  
  print(sys.path)
  ```

- sys에 직접 내가 경로 추가하는 것도 가능함. 

  1. sys.path에  append()로 경로 추가 가능. 

     첫 번째 방법은 `sys.path`에 새로운 경로를 직접 추가하는 것입니다. `sys.path`는 결국 리스트이기 때문에 `.append()` 함수를 써서 쉽게 새로운 경로를 추가할 수 있습니다.

     예를 들어 `sys.path`에 바탕 화면의 경로를 추가하고 싶다면 아래와 같은 코드를 추가해 주면 됩니다.

     run.py

     ```python
     import sys
     sys.path.append('/Users/codeit/Desktop') # macOS
     sys.path.append('C:\\Users\\codeit\\Desktop') # Windows
     
     ```

     

  2. 영구적으로 경로 추가도 가능함(위 방법은 해당 파일에서 한번 찾아 보는 것). 

     `sys.path`에 어떤 경로를 `append()`해 주면 프로그램이 종료되면 그 경로는 `sys.path`에서 사라집니다. 그 경로에 있는 모듈을 쓰고 싶으면 매번 `append()`를 해 줘야 합니다.

     그럼 어떤 경로를 영구적으로 `sys.path`에 추가하려면 어떻게 해야 할까요?

     PyCharm의 설정 (Windows: File → Settings, macOS: PyCharm → Preferences)으로 가서 Project 탭 안에 있는 Project Interpreter를 클릭해 줍니다.

     > 1. PyCharm의 설정 (Windows: File → Settings, macOS: PyCharm → Preferences)으로 가서 Project 탭 안에 있는 Project Interpreter를 클릭해 줍니다.
     >
     > 2. 그리고 톱니바퀴 버튼을 누른 후 Show All 옵션을 클릭해 줍니다.
     > 3. 그런 다음에 파일 경로 아이콘을 클릭해 줍니다.
     > 4. 그리고 + 아이콘을 누른 후 원하는 경로를 추가해 줍니다 (밑에 사진은 바탕 화면의 경로를 추가해 줍니다).
     > 5. Ok를 눌러줍니다. 
     >
     > 

     

### 스크립트와 모듈

- 파이썬에서는 프로그램을 작동시키는 코드를 담은 실행 용도의 파일을 스크립트 라고 함.   Run.py

- 모듈은 프로그램에 필요한 변수들이나 함수들을 정의해 놓은 파일. 보통 직접 사용하지 않고, 다른 파일에서 가져다 씀. 

- 파이썬은 모듈을 임포트 하면, 그 모듈에 있는 모든 함수가 실행됨. 즉, area 모듈에 테스트를 위한 print 로그를 몇번 찍어 놓은 것이, run.py에서 가져와 쓰려고 해도 실행된다는 것. 만약 모듈을 가지고 오고는 싶은데 이상한 코드는 가지고 오고 싶지 않다면?

- __name__은 모듈의 이름을 정해져 있음. 

  직접 실행하면, 그 파일의 **name**은 **main**으로 설정 됨. 

  파일을 다른 곳에서 실행하면 name은 원래 모듈의 이름으로 설정됨. 

  ```python
  run.py
  
  import area
  
  ## 결과
  ## area 모듈 이름 : area
  ```

  ```python
  area.py
  
  print("area 모듈 이름 : {}".format(__name__))
  
  ## 결과
  ## area 모듈 이름 : __main__
  ```

  

- area가 직접 실행될떄만 실행시키고 싶은 테스트 코드가 있다면?

  ```python
  if __name__ == "__main__":
  	print("test")
  ```




- main을 만들고 오버라이딩 하면서 활용가능함. 

  ```python
  PI = 3.14
  
  # 원의 면적을 구해 주는 함수
  def circle(radius):
        return PI * radius * radius  
  
  # 정사각형의 면적을 구해 주는 함수
  def square(length):
        return length * length
  
  # 함수들을 테스팅 하는 메인 함수
  def main():
        # circle 함수 테스트
        print(circle(2) == 12.56)
        print(circle(5) == 78.4)
  
        # square 함수 테스트
        print(square(2) == 4)
        print(square(5) == 25)
  
  if __name__ == '__main__':
      main()
  ```

  이렇게 `main` 함수를 사용하면 파일에서 프로그램을 **작동시키는 코드가 어디 있는지 쉽게 알 수 있기 때문에 코드의 가독성이 올라갑니다**. 코드의 흐름과 의도를 더 쉽게 이해할 수 있는 거죠. 따라서 파이썬에서는 `main` 함수가 요구되지 않더라도 `if __name__ == '__main__'`과 `main()`을 사용하는 것을 추천드립니다.



### 패키지 

- 모듈들을 하나로 묶어 놓은 것. 즉, 아이템 모듈(items.py) 거래 모듈(trasaction.py)를 하나로 묶어서 상점 패키지를 만드는 것. 프로그램의 구성요소를 잘 정리할 수 있고, 재사용이 가능. 

- 패키지 만드는 법은 간단함. 

  하나로 묶어서 디렉토리로 만들고, init을 만들어 주면 됨. IDE에서 파이썬패키지 만들기를 하면, 자동으로 init을 만들어 주는 것. 

- 그걸 그냥 임포트 해서 사용하면 끝. 

  ```python
  import shapes.volume
  from shapes.area import square
  from shapes import volume
  

  print(shapes.volume.cube(3))
  print(square(1))
  
  ```
  
- 근데 여기서 중요한게 하단처럼 임포트 하니깐 에러가 남. 파이썬에서 패키지를 임포트 하면, 안에 있는 모듈들은 임포트가 안됨. 패키지 안에 있는 모듈들도 같이 임포트 하려면, __init__을 활용해야 함. 

  ```python
  import shapes
  
  shapes.area.circle(3)
  ```

  즉 정리하자면

  ```python
  from <package> import <module(s) # 가능
  from <package.module> import <member(s)> # 가능
  import shapes # 오류
  import shapes.volume.cube # 오류
  ```

  #### __init__

- init파일은 무슨 역할을 하는가?

  - init파일은 이것이 파이썬 패키지임을 말해주는 것. 3.3이전에서는 필수여서, 임포트 자체가 불가능했으나, 패키지 호환을 위해 init을 권장함.

  - init은 initialize의 줄임말. 즉, 패키지를 초기화 할 때 사용됨. 처음으로 뭔가를 임포트 하면 이게 제일 먼저 사용된다는 것. 
  - 실제로 임포트 해보면, init파일 내부가 먼저 실행됨. 

- init을 어떻게 활용행야 할 것인가?

  위에서 보면, import <package>를 하면, 내부 모듈들이 같이 임포트가 되지 않았었음. 패키지를 가져오면서, 내부 것들도 가지고 가려면 이때 init을 활용하는 것. 

  ```python
  __init__.py
  
  from shapes import area, volume
  
  run.py
  
  import shapes
  
  print(shapes.area.square(2))
  print(shapes.area.cube(2))
  ```

  init파일 내부에다가 위 처럼 임포트를 해 놓고 쓰면, 

  init에서는 패키지 임포트 할 때, 같이 임포트 하고 싶은 모듈들만 써 놓으면 됨. 

  

  ```python
  __init__.py 
  
  from shapes.area import circle, square
  
  run.py
  import shapes
  
  print(shapes.circle(2))
  print(shapes.square(2))
  ```

  위처럼 가지고 온다면, run에서는 circle과 square에 직접 접근 해야지. 즉, 위에서 run.py에서 직접 써도 똑같은데 편하게 미리 해놓은거야. 

- init파일에서 변수 정의하기

  여러 모듈에서 필요한 변수들은 __init__에서 한번에 정의해 주는게 좋음. 

  ```python
  __init__.py
  
  PI = 3.14
  
  
  area.py
  from shapes import PI
  
  
  def circle(radius):
      return PI * radius * radius
  ```

  상수 뿐만 아니라 여러 모듈에서 필요한 함수 또는 객체도 정의할 수 있음. 

  패키지 init에서 정의된 애들은 패키지 외부에서도 쓸 수 있음. 

  ```python
  run.py
  
  import shapes
  shapes.PI # 이렇게 사용 가능. 
  ```

  

  #### __all__

-  import *을 하면, 모든 모듈을 다 가지고 오라는 소리인데, 막상 dir을 찍어보면, 특수변수 이외에는 아무것도 안나옴. 

  ```
  from shapes import *

  print(dir())
  ```
  
  ```
  ['PI', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
  ```
  
  *를 패키지에 적용하면 아무 모듈도 적용이 안됨. 
  
-  이런 경우 init에서 바꿔 줘야 함. all은 우리가 import *를 했을때, 뭘 가져와야 하는지를 정의해 주는 함수. 꼭 모든 모듈을 넣어야 하는 것은 아님. 넣고 싶은 모듈을 넣으면 됨. 

  ```
   __all__=['area', 'volume']
  ```

  ```
  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'area', 'volume']
  ```

  

- __all__은 모듈에도 쓸 수 있음. ***from <패키지>.<모듈> import *** 한 경우에 뭐가 나왔으면 좋겠는지를 정의해 놓으면 돼. 

  ```
   area.py
   
   
  ```



#### 서브패키지

- 패키지 안에 다른 패키지가 있을 수 있음. 그걸 서브패키지 라고 함. 

- 서브패키지 사용하기. 하단처럼 해 놓으면, 이제 다른 곳에서 ***from mymath import stats***  혹은 ***import mymath.stats***이런 경우에, 해당 함수들이 같이 임포트 되는 것. *패키지를 임포트 하는 경우는 하단 모듈을 같이 안들고 간단는 것만 기억하면 됨.* 

  ```python
  stats/__init__.py
  from mymath.stats import average, spread
  
  shapes/__init__.py
  from mymath.shapes import area, volume
  ```

  ```
  mymath/__init__.py
  
  
  ```

  

- 참고사항

  ```python
  # 패키지 임포트(단 이렇게 패키지 임포트 하는 경우는 하단 모듈들 안가져옴. init에서 정의해놔야 함)
  import mymath
  
  # 서브패키지 임포트(단 이렇게 패키지 임포트 하는 경우는 하단 모듈들 안가져옴. init에서 정의해놔야 함)
  import mymath.shapes
  
  # 모듈 임포트
  import mymath.shapes.area
  
  # 모듈 안에 있는 변수나 함수는 이 방식으로 임포트 할 수 없음 
  import mymath.shapes.area.circle # 오류
  ```

  ```python
  # 패키지 안에 있는 패키지 임포트(단 이렇게 패키지 임포트 하는 경우는 하단 모듈들 안가져옴. init에서 정의해놔야 함)
  from mymath import shapes
  
  # 패키지 안에 있는 모듈 임포트
  from mymath.shapes import area
  
  # 모듈 안에 있는 함수 임포트
  from mymath.shapes.area import circle
  
  # import 뒤에는 . 을 쓸 수 없음 
  from mymath import shapes.area # 오류
  ```

  

#### 상대 경로

- . 현재경로, .. 상위경로. 

  ```python
  from .area import *  # 현재 패키지에 있는 area에서 모든 것을 가져와라
  from .volume import * # 현재 패키지에 있는 volume에서 모든 것을 가져와라
  ```





#### 외부 패키지

- 파이썬에는 이미 잘 만들어진 패키지들이 매우 많음. 여러 프로그래밍에서 유용하게 쓰이는 기능들을 다른 개발자가 만들어 놓은 것. 이런 것들을 **외부 패키지** 혹은 **외부 라이브러리**라고 말함. 잘 활용하는게 매우 중요함. 좋은 개발자는 결국 남의 코드를 잘 쓰는 사람임. 

- 패키지에 어떤 함수들이 있는지, 패키지의 함수들이 무엇을 하는지 알면 됨. 공식 문서를 통해 알 수 있음. 

- PyPI -> 파이썬 공식 패키지 저장소.

- 패키지 종류

  - 스탠다드 라이브러리 : 스탠다드 라이브러리는 프로그래밍에 필요한 가장 기본적인 기능들을 제공합니다. 스탠다드 라이브러리 안에는 자료형, 내장 함수, 스탠다드 모듈 등이 있습니다. 참고로 스탠다드 라이브러리는 패키지가 아닙니다. 여기서 '라이브러리'는 단순히 어떤 기능들의 모음을 뜻합니다. **스탠다드 라이브러리는 파이썬을 설치하면 기본적으로 딸려오기 때문에 따로 설치하지 않아도 됩니다**.

  - 외부 라이브러리 : 외부 라이브러리 또는 외부 패키지는 파이썬을 사용하는 일반 개발자들이 패키지를 만들어서 PyPI에 업로드해 놓은 것입니다. **외부 라이브러리는 파이썬의 일부가 아니고 우리가 직접 설치해야 합니다**.

- https://pypi.org/ -> 이 안에 모든 패키지들이 올라와 있음. documentation과 입문자 가이드들을 위한 모든 것들이 나와 있음. 

- 설치하고 사용하는 방법

  ```
  pip
  ```

- 파이썬 설치되어 있는 **버전 삭제 하는 방법**.
  - mac의 finder에서 Go -> Go to Folder -> `/Library/Frameworks/Python.framework/Versions`
  - 3.x버전을 휴지통으로 옮겨준다(비밀번호 입력하면 됨). 그리고 휴지통 가서 즉시삭제 누르기. 
  - 그리고 응용프로그램(Applications)에 있는 python3.x디렉토리를 휴지통으로 옮기고 즉시삭제 누르기. 

- 파이참에서 외부 패키지 설치하기. 

  **preference -> project:new_project -> project Interpreter -> +버튼  -> 원하는 패키지 검색 후 입력**. 

- **pip로 다운받기**

  ```
  pip install <package name>
  pip3 install <package name>
  ```

  *지울때는?*

  ```
  pip3 uninstall <package.name>
  ```

  *특정 패키지 버전 설치 하기*

  ```
  pip3 install pandas==1.1.0
  ```



#### 패키지 사용 예시(youtube_dl)

- 파이썬으로 유튜브 영상 다운받기. 

  ```
  pip install youtube_dl
  ```

  

  