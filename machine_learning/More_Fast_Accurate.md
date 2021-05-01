# 머신러닝, 더 빠르고 정확하게

머신러닝 알고리즘의 속도와 정확도를 높이는 법

이 이론들을 scikit-learn과 pandas라이브러리에서 적용하는 법. 

- #### Feature Scaling : Normalization

  **데이터 전처리** : 데이터를 그대로 사용하지 않고, 가공해서 모델을 학습시키는데 좀 더 좋은 형식으로 만들어 주는 것.

  그 중에서 먼저 Feature Scaling이라는 것을 본다. 

  **Feature Scaling** : 입력변수의 크기를 조정. 즉, 머신러닝 모델에 사용할 입력변수들의 크기를 조정해서 일정 범위 내에 떨어지도록 바꾸는 것. **Why?** Gradient Descent를 조금 더 빨리 할 수 있게 도와준다.  

  연봉과 나이의 차이가 너무 커서, 입력변수의 크기가 모두 일정 범위 내에 들어오도록 하게 하는 것. 

  ![6_1](./resources/6_1.png)

   How? Feature Scaling 하는 방법은 여러가지가 있음. 그 중 가장 직관적인 것은 **min-max normalization**.

  **min-max normalization** : 최솟값과 최댓값을 이용해서 데이터의 크기를 0과 1 사이로 바꿔준다(normalization의 뜻 자체가 숫자의 크기를 0과 1 사이로 만든다는 뜻). 

  가장 큰 210과 140의 차이를 구한 후 모든 값들을 돌면서 그 값에서 최솟값을 빼고 70으로 나눠줌. 왜 0과 1사이로 나올까? 최소와 최대의 차이가 70이니깐, 최대값을 1 최솟값을 0으로 잡고 도는 것. 당연하잖아. 

  **나와 최솟값의 차이 / 최댓값과 최솟값의 차이의 비율**

  ![6_1](./resources/6_2.png)

  ![6_1](./resources/6_3.png)

  #### 실습

  ```python
  import pandas as pd
  import numpy as np
  
  from sklearn import preprocessing
  
  NBA_FILE_PATH = '../resources/NBA_player_of_the_week.csv'
  nba_player_of_the_week_df = pd.read_csv(NBA_FILE_PATH)
  
  nba_player_of_the_week_df.describe()
  ```

  ![6_1](./resources/6_4.png)

  ```python
  height_weight_age_df = nba_player_of_the_week_df[['Height CM', 'Weight KG', 'Age']]
  height_weight_age_df.head()
  
  scaler = preprocessing.MinMaxScaler()
  normalized_data = scaler.fit_transform(height_weight_age_df)
  normalized_data
  
  normalized_df = pd.DataFrame(normalized_data, columns=['Height', 'Weight', 'Age'])
  normalized_df.describe()
  
  ```

  ![6_1](./resources/6_5.png)



- #### Feature Scaling과 Gradient Descent

  