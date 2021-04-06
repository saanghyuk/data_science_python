# Python Lecture



### Module

- 게임을 만들려면, 캐릭터/인터페이스/상점 등 엄청 많은 부분이 필요함. 이걸 다 한 파일로 뭉치려면, 파일이 엄청 커지고 복잡해짐. 수정하려고 하면 어떤걸 수정해야 하는지부터 굉장히 애매함. 
- 그래서 코드를 파일 단위로 나누게 됨. 아이템은 items.py, 상점은 stores.py에 넣는것. 이런 파일 단위를 모듈이라고 함. 그리고, 코드 재사용이 가능. 



- 모듈을 가져오는 방법

  - 특정 함수만 필요할 때 - 이렇게 쓰면, 그냥 circle이라고 쓰면 됨. 

  ```python
  from are import circle, square
  
  import area as ar - 새로운 이름으로 사용 가능함. 
  
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