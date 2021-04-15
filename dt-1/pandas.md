# PANDAS

- R의 장점중에 제일 좋았던 것들이, DataFrame이였음. 그것을 그대로 가져온게 판다스. 
- 판다스는 넘파이를 이용해서 만들었기 때문에, 넘파이의 기능들은 기본적으로 판다스에 다 있다고 보면 됨. 거기에 플러스 알파(외부 데이터 읽고 쓰기, 데이터 분석, 시각화 등) 된 것. 
-  특히 표 형식의 데이터를 다룰 때 굉장히 편함. 

- 일반적인 엑셀 데이터 등은 2차원임. 2차원 형태의 데이터를 다루기 위한 자료형이 DataFrame
  - 표 형식, **Row(or Index)/Column**
  - **Column**은 데이터의 특징을 담음. 각 **Row**는 Record를 담음. 
- 넘파이 어레이도 2차원이 가능한데? 판다스 데이터 프레임은 넘파이 어레이를 가지고 만든것이 맞음. 그래서, 넘파이 어레이를 조금 더 쓰기 쉽게 만들어 놓은 것. 예를 들어, 각 컬럼과 각 로우에 이름을 붙이고 **str으로 인덱싱**을 하는 것 등이 가능함. 또한, 넘파이 어레이에서는 모든 값이 같은 자료형이여야 했으나, **다양한 자료형**을 담을 수 있는 것이 DF의 장점. 

#### Usage

```python
two_dimension_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimension_list, columns = ['name', 'english_score', 'math_score'], 
                    index = ['a', 'b', 'c', 'd'])
```



#### DataType of Pandas

| dtype        | 설명            |
| ------------ | --------------- |
| `int64`      | 정수            |
| `float64`    | 소수            |
| `object`     | 텍스트          |
| `bool`       | 불린(참과 거짓) |
| `datetime64` | 날짜와 시간     |
| `category`   | 카테고리        |



#### Method

```python
two_dimension_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

# df 만들면서 columns와 index넣기. df에서는 row를 index라고 많이 부름
my_df = pd.DataFrame(two_dimension_list, columns = ['name', 'english_score', 'math_score'], index = ['a', 'b', 'c', 'd'])
```

| method          | roles, result                                                |
| --------------- | ------------------------------------------------------------ |
| `my_df.index`   | `Index(['a', 'b', 'c', 'd'], dtype='object')`                |
| `my_df.columns` | `Index(['name', 'english_score', 'math_score'], dtype='object')` |
| `my_df.dtypes`  | name object <br />english_score int64<br />math_score int64 <br />dtype: object<br /><br />각 컬럼의 자료형 출력. object는 판다스에서의 문자열을 뜻함. 같은 컬럼 내에서는 모두 같은 자료형이여야 함. |
|                 |                                                              |
|                 |                                                              |
|                 |                                                              |



#### 데이터프레임을 만드는 다양한 방법

- **2차원 리스트나 2차원 numpy array로 DataFrame을 만들 수 있습니다**. 심지어 pandas Series를 담고 있는 리스트로도 DataFrame을 만들 수 있습니다.

  따로 column과 row(index)에 대한 설정이 없으면 그냥 0, 1, 2, ... 순서로 값이 매겨집니다.		
  
  ```python
  two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
    two_dimensional_array = np.array(two_dimensional_list)
    list_of_series = [
        pd.Series(['dongwook', 50, 86]), 
        pd.Series(['sineui', 89, 31]), 
        pd.Series(['ikjoong', 68, 91]), 
        pd.Series(['yoonsoo', 88, 75])
    ]
  
  
  
    # 아래 셋은 모두 동일합니다
    df1 = pd.DataFrame(two_dimensional_list)
    df2 = pd.DataFrame(two_dimensional_array)
    df3 = pd.DataFrame(list_of_series)
  ```
  
  ​	

- **파이썬 사전(dictionary)으로도 DataFrame을 만들 수 있습니다.**

  사전의 key로는 column 이름을 쓰고, 그 column에 해당하는 리스트, numpy array, 혹은 pandas Series를 사전의 value로 넣어주면 됩니다.

  ```python
  import numpy as np
  import pandas as pd
  
  names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
  english_scores = [50, 89, 68, 88]
  math_scores = [86, 31, 91, 75]
  
  dict1 = {
      'name': names, 
      'english_score': english_scores, 
      'math_score': math_scores
  }
  
  dict2 = {
      'name': np.array(names), 
      'english_score': np.array(english_scores), 
      'math_score': np.array(math_scores)
  }
  
  dict3 = {
      'name': pd.Series(names), 
      'english_score': pd.Series(english_scores), 
      'math_score': pd.Series(math_scores)
  }
  
  
  # 아래 셋은 모두 동일합니다
  df1 = pd.DataFrame(dict1)
  df2 = pd.DataFrame(dict2)
  df3 = pd.DataFrame(dict3)
  
  print(df1)
  ```

  

- **리스트가 담긴 사전이 아니라, 사전이 담긴 리스트로도 DataFrame을 만들 수 있습니다. **

  ```python
  import numpy as np
  import pandas as pd
  
  my_list = [
      {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
      {'name': 'sineui', 'english_score': 89, 'math_score': 31},
      {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
      {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
  ]
  
  df = pd.DataFrame(my_list)
  print(df)
  ```

  



#### 데이터 읽고 쓰기

```python
import pandas as pd

pd.read_csv(<파일경로>) # 자동으로 df return 첫번째 줄을 헤더로 자동으로 인식
pd.read_csv('경로', header=None) # 헤더 없는 경우
pd.read_csv('경로', header=None, index_col=0) # 제일 왼쪽 0번째 컬럼을 row/index이름으로 설정하라.
```





### DataFrame 다루기

- 예시  Dataframe

  `iphone_df = pd.read_csv('./resources/iphone.csv', index_col =0 )`

|               |     출시일 | 디스플레이 | 메모리 | 출시 버전 | Face ID |
| ------------: | ---------: | ---------: | -----: | --------: | ------: |
|      iPhone 7 | 2016-09-16 |        4.7 |    2GB |  iOS 10.0 |      No |
| iPhone 7 Plus | 2016-09-16 |        5.5 |    3GB |  iOS 10.0 |      No |
|      iPhone 8 | 2017-09-22 |        4.7 |    2GB |  iOS 11.0 |      No |
| iPhone 8 Plus | 2017-09-22 |        5.5 |    3GB |  iOS 11.0 |      No |
|      iPhone X | 2017-11-03 |        5.8 |    3GB |  iOS 11.1 |     Yes |
|     iPhone XS | 2018-09-21 |        5.8 |    4GB |  iOS 12.0 |     Yes |
| iPhone XS Max | 2018-09-21 |        6.5 |    4GB |  iOS 12.0 |     Yes |

#### 값 뽑아오기
| method                                                       | roles                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `iphone_df.loc['iPhone 8', '메모리']`                        | dataframe.loc['row이름', 'column이름']                       |
| `iphone_df.loc['iPhone X']` or `iphone_df.loc['iPhone X', :]` | row 통으로 받아오려면, **row이름**만 쓰면 됨. **:** 은 처음부터 끝까지 다 받아오라는 소리. |
| `type(iphone_df.loc['iPhone X', :])`                         | pandas.core.series.Series 시리즈는 판다스의 1차원 자료형.    |
| ` iphone_df.loc[:, '출시일']`or `iphone_df['출시일']`        | 해당 column에 해당되는 row를 다 가져오기.                    |
| `iphone_df.loc[:, ['출시일', '메모리']]` or `iphone_df[['출시일', '메모리']]` | 열 두줄 찾기                                                 |
| `iphone_df.loc[['iPhone X', 'iPhone XS Max'], :]` or `iphone_df.loc[['iPhone X', 'iPhone 8']]` | 행 두줄 찾기                                                 |
| `pd.merge(samsong_df, hyundee_df, on='요일')`                | 요일을 기준으로 데이터프레임 합치기. 함수는 두 데이터프레임을 각 데이터에 존재하는 고유값(key)을 기준으로 병합할때 사용한다. 요일이 같은 것 기준으로 **왼쪽에서 오른쪽으로** 붙여줌. |
| `pd.concat([df1, df2])`                                      | 말 그대로 물리적으로 이어줌. 위에서 아래로 쭉. 같은 열은 같은 열에 가서 **위에서** **아래로 붙음**. |
| `df.rename(columns = {'variable': 'Year', 'value': 'Income'}, inplace = False)` | 컬럼 이름 바꾸기, 딕셔너리 내부 key는 원래 이름 value는 바꿀 이름. |
| `iphone_df.loc['iPhone 8' : 'iPhone XS']`                    | 연속적으로 있을 때, 슬라이싱 가능. iPhone8부터,  iPhone XS까지 들고 옴. |
| `iphone_df['메모리':'Face ID']`**(X)**<br />`iphone_df.loc[:,'메모리':'Face ID']` **(O)** | 이렇게 하면, 아무것도 안나옴. 컬럼으로 슬라이싱은 복잡하게 써야 함. |
| `iphone_df.loc[[True, False, True, True, False, False, True]]` | True에 해당되는 row만 indexing 가능                          |
| `iphone_df.loc[:, [True, True, False, False, False]]`        | True에 해당되는 column들만 indexing 가능                     |
| `iphone_df.loc[iphone_df['디스플레이'] >5, :]` or `iphone_df.loc[iphone_df['디스플레이'] >5]` | 보통은 이렇게 쓰는 것.                                       |
| `iphone_df[(iphone_df['디스플레이'] > 5) & (iphone_df['Face ID']=='Yes')]` | 두 조건 동시에 찾기 [논리연산자 '&'](https://wikidocs.net/1161) |
| `df.iloc`                                                    | 숫자로 인덱싱 하기 위한 함수. **Integer Location**           |
| `iphone_df.iloc[2, 4]`                                       | 2번 로우 4번 컬럼을 가져옴.                                  |
| `iphone_df.iloc[[1, 3], [1, 4]]`                             | 복수의 행과 열 가져오기.                                     |
| `iphone_df.iloc[3:, 1:4]`                                    | 로우는 3번 인덱스부터 끝까지, 컬럼은 1부터 4 전까지 받아오라는 것 |
| `iphone_df[3:5]`                                             | iloc, loc 안쓰고 이렇게 숫자로 슬라이싱하면, 특이하게 **로우를 슬라이싱 하게 됨**. |
| `iphone_df.iloc[[1, 3], [1, 4]] = 'd'`                       | 조건에 해당되는 애들만 값 바꾸기.                            |
| `third_mask = df['course name'].isin(list)`                  | 컬럼 네임 value로 다양한 값을 한번에 찾고 싶음면, isin()안에 리스트를 주면, 쉽게 찾을 수 있음. |
|                                                              |                                                              |
|                                                              |                                                              |



#### 값 바꾸기

| method                                                       | role                                                       |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
| `iphone_df.loc['iPhone 8', '메모리'] = 새로운 값`            | 똑같이 찾고 나서, 그냥 거기에 새로운 값 할당해 주면 끝.    |
| `iphone_df.loc['iPhone 8'] = ['1993-03-07', '4.9', '2GB','iOS 11.0', 'No']` | 특정 행을 짚고 그 줄 싹다 요소 넣어주면 바뀜.              |
| `iphone_df.loc['iPhone 8'] = 'Hi'`                           | 이렇게 하면 해당 행의 모든 컬럼들이 싹다 한 값으로만 바뀜. |
| `iphone_df['디스플레이'] = ['4.7 in', '5.5 in', '4.7 in', '5.5 in', '5.8 in', '5.8 in', '6.5 in']` | 해당 컬럼에 해당되는 부분 싹다 바꾸기.                     |
| `iphone_df['Face ID'] = 'No'`                                | 해당 컬럼의 모든 값을 No로                                 |
| `iphone_df[['디스플레이', 'Face ID']] = 'x'`                 | 여러 줄 한번에 바꾸기. 두 컬럼 모두 x로 바뀜.              |
| `iphone_df.loc[['iPhone 7', 'iPhone X']] = 'o'`              | 여러 개의 행 한번에 바꾸기.                                |
| `iphone_df.loc['iPhone 8 Plus':'iPhone XS']='5'`             | 슬라이싱 해서 한번에 바꾸는 것도 가능함.                   |
| `iphone_df[iphone_df['디스플레이']>5]  = 'P'`                | 디스플레이 5 인치 넘는애들의 모든 것은 p로 바뀜.           |
|                                                              |                                                            |



#### 값 추가 혹은 삭제 

| methods                                                      | role                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `iphone_df.loc['iPhone XR'] = 'x'`                           | 없는 row를 찾고 값을 할당하면, 그 행이 새로 생김.            |
| `iphone_df['뭉카'] = '3'`                                    | Column 도 마찬가지임.                                        |
| `iphone_df.loc['하이', '바이'] = 3`                          | 아예 없는 행과 열로 해버리면, 해당 딱 그 칸에는 여전히 값이 할당되고 나머지는 NaN이라고 뜸. |
| `iphone_df.drop('iPhone XR', axis='index', inplace=False)`   | 해당 행을 삭제하겠다. <br />`axis = 'index' `행을 삭제하겠다는 것.<br />`inplcae = False`를 해 놓으면, 삭제 후 값을 리턴해 주는데 원래 변수에 그 값을 할당은 안함. inplace = True를 해 놓으면, 원래 값에 다시 저장. |
| `iphone_df.drop('제조사', axis='columns', inplace=True)`     | 열을 삭제하겠다.                                             |
| `iphone_df.drop(['iPhone 7', 'iPhone 8'], axis='index', inplace=False)` | 여러 행 한번에 삭제하기.                                     |
| `iphone_df.drop(['뭉카', '바이'], axis='columns', inplace=False)` | 여러 열 한번에 삭제하기.                                     |
|                                                              |                                                              |





#### Index/Column 설정하기

|    *INDEX NAME* | position | born | number | nationality |
| --------------: | -------: | ---: | -----: | ----------- |
| Roberto Firmino |       FW | 1991 |  no. 9 | Brazil      |
|      Sadio Mane |       FW | 1992 | no. 10 | Senegal     |
|   Mohamed Salah |       FW | 1992 | no. 11 | Egypt       |
|       Joe Gomez |       DF | 1997 | no. 12 | England     |
|  Alisson Becker |       GK | 1992 | no. 13 | Brazil      |

| methods                                                      | roles                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `liverpool_df.rename(columns={'position':'POSITION'})`       | position 컬럼 이름을 대문자로 바꾸기.  **rename함수 또한, 기존 df를 건들지 않음.** |
| `liverpool_df.rename(columns={'position':'POSITION'}, inplace=True)` | 기존 데이터프레임에 아예 반영하고 싶으면 여기서도 **inplace=True** 파라미터를 주면됨. |
| `liverpool_df.rename(columns={'position':'POSITION', 'number':'NUMBER'})` | Dict에 여러값들 한번에 보내줄 수 있음.                       |
| `liverpool_df.index.name = 'Player Name'`                    | 인덱스에 설명 붙여 주기. 인덱스 위에 ***INDEX NAME*** 자리에 player name이 들어가게 되는 것. |
| `liverpool_df.set_index('number', inplace=True)`             | number를 인덱스로 만들 수 있음. 근데 이렇게 하면 문제가 기존 인덱스(선수 이름들)가 날라가버림. 그래서, 이 함수를 쓰기 전에는 항상 기존 인덱스를 새로운 컬럼으로 할당해 주고 난 다음에 인덱스를 새로 정해야 함. 얘도 inplace필요함. |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |





#### 큰 데이터 쉽게 파악하기

`laptop_df = pd.read_csv('resources/laptops.csv')`

**큰 판다스 데이터프레임 다루기**

| methods                                                      | roles                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `laptops_df.head()` or `laptops_df.head(7)`                  | 앞에 다섯개 or 앞에 7개                                      |
| `laptops_df.tail()` or `laptops_df.tail(6)`                  | 뒤에 다섯개 or 뒤에 6개                                      |
| `laptop_df.shape`                                            | (#행, #열)로 출력됨.                                         |
| `laptop_df.info()`                                           | 모든 컬럼이 나열되고, 데이터타입 등을 모두 알 수 있음.       |
| `laptop_df.columns`                                          | 컬럼을 알 수 있음.                                           |
| `laptop_df.describe()`                                       | 각 컬럼에 대한 통계정보가 나옴.                              |
| `laptop_df.sort_values(by='price')`                          | 원하는 정보를 기준으로 정렬. price기준으로 정렬. 이것도 원래 df를 건들지는 않음. 새로운 df를 만든 것. |
| `laptop_df.sort_values(by='price', ascending=False, inplace=True)` | ascending=False하면 큰것이 위로 감. inplace=True해놓으면, 기존 df에다가 저장시킴. |

##### 큰 판다스 시리즈 다루기

| methods                                                      | Roles                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `laptop_df['brand'].unique()`                                | 해당 시리즈의 유니크한 value가 총 몇개가 있는지.             |
| `laptop_df['brand'].value_counts()`                          | 시리즈의 각 value들이 몇개씩 있는지.                         |
| `laptop_df['brand'].describe()`                              | 시리즈에서 describe를 쓰면, count, unique, top(가장 많이 나오는 value), freq(최빈 value가 총 몇번 등장하는지)이 나옴. |
| `df['room assignment'] = np.where(<bool_list>, 'not allowed', np.where(auditoriumboolseries, "Auditorium", np.where(largeroomboolseries, "Large room", np.where(mediumroomboolseries, "Medirum room", "Small room")))) df` | 해당 bool리스트를 찾아서 거기에 값을 할당함.                 |
|                                                              |                                                              |
|                                                              |                                                              |





#### Tip

- 컬럼들 중, 특정 이름 들어간 것들 찾고 싶을때. 값이 array로 나오면, str.contain쓰면 편함. 

  ```python
  searchfor = ['or', 'ap', 'hin', 'nited','many']
  colNames = df.columns[df.columns.str.contains('|'.join(searchfor))] 
  colNames```
  ```

- 