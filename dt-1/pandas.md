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

