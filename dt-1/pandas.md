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

| method                                                       | roles                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `iphone_df.loc['iPhone 8', '메모리']`                        | dataframe.loc['row이름', 'column이름']                       |
| `iphone_df.loc['iPhone X']` or `iphone_df.loc['iPhone X', :]` | row 통으로 받아오려면, **row이름**만 쓰면 됨. **:** 은 처음부터 끝까지 다 받아오라는 소리. |
| `type(iphone_df.loc['iPhone X', :])`                         | pandas.core.series.Series 시리즈는 판다스의 1차원 자료형.    |
| ` iphone_df.loc[:, '출시일']`or `iphone_df['출시일']`        | 해당 column에 해당되는 row를 다 가져오기.                    |
| `iphone_df.loc[:, ['출시일', '메모리']]` or `iphone_df[['출시일', '메모리']]` | 열 두줄 찾기                                                 |
| `iphone_df.loc[['iPhone X', 'iPhone XS Max'], :]` or `iphone_df.loc[['iPhone X', 'iPhone 8']]` | 행 두줄 찾기                                                 |
| `pd.merge(samsong_df, hyundee_df, on='요일')`                | 요일을 기준으로 데이터프레임 합치기. 함수는 두 데이터프레임을 각 데이터에 존재하는 고유값(key)을 기준으로 병합할때 사용한다. 요일이 같은 것 기준으로 **왼쪽에서 오른쪽으로** 붙여줌. |
| pd.concat([df1, df2])                                        | 말 그대로 물리적으로 이어줌. 위에서 아래로 쭉. 같은 열은 같은 열에 가서 **위에서** **아래로 붙음**. |
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
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |