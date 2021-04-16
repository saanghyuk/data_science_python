# Visualization

#### Matplotlib
```python
f%matplotlib inline
```


#### Line Graph

- 선 그래프. 내부 값들이 숫자일 때 그릴 수 있음. 변화를 보기 위함. 

| methods                                           | roles                                                        |
| ------------------------------------------------- | ------------------------------------------------------------ |
| `df.plot()`                                       | 그냥 판다스 데이터프레임에도 그래프 그리는 기능이 내장되어 있음. parameter로  kind를 넘겨줘야 함. `df.plot(kind='line')` 기본 디폴트값이 line chart. |
| `df.plot(y='KBS)` or `df.plot(y=['KBS', 'JTBC'])` | 특정 하나 혹은 특정 여러개만 그리고 싶을 때.                 |
|                                                   |                                                              |



#### Bar Chart

- 항목들에 대한 수치비교. 

| methods                             | roles                                                   |
| ----------------------------------- | ------------------------------------------------------- |
| `df.plot(kind='bar')`               |                                                         |
| `df.plot(kind='barh')`              | 가로로 눕히기                                           |
| `df.plot(kind='bar', stacked=True)` | 두 종류의 막대가 쌓이게 됨.                             |
| `df['Female'].plot(kind='bar')`     | 특정행을 뽑아서 쓸 수 있음. 시리즈에도 plot함수가 있음. |





#### Pie Graph

- 비율을 보여주기에 적합함

`df.plot(kind='pie')`

- index가 x가 됨. 기준을 잡고 싶으면, set_index를 사용해야 함. 



#### Histogram

- 각각 범위로 묶어서 보게 됨. 묶어서 세는 것. 	

| methods                                     | roles                                                        |
| ------------------------------------------- | ------------------------------------------------------------ |
| `df.plot(kind='hist', y='Height')`          | y데이터를 히스토 그램으로 보고 싶다는 것. 따로 설정 안하면 범위가 전체를 10개로 나누는 범위가 됨. |
| `df.plot(kind='hist', y='Height', bins=15)` | 범위를 15개로 나누고 싶으면, 이렇게 됨.                      |

#### Box Plot

- 시각적으로 통계 정보 보기 위해 사용. 총 5개의 통계값을 보기 위해 사용됨. 

  ![box_plot](./resources/box_plot.png)

  - 가운데 사각형 부분은 Box, 맨 위 아래 짝대기는 Whisker라고 부름. 
  - Box와 Whisker바깥 지점은 이상점(outlier)라고 부름. 이상점을 정하는 기준은 조금씩 다름. 

| methods                                                      | roles                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `df['math score'].describe()`                                | 박스플롯에서 볼 수 있는 모든 정보는, 사실 describe에 다 있음. describe를 시각화 하는 것이 박스 플롯이라고 생각하면 됨. |
| `df.plot(kind='box', y='math score')`                        | 박스 플롯 그리기.                                            |
| `df.plot(kind='box', y=['math score', 'reading score', 'writing score'])` | 여러 박스 플롯 동시에 보기.                                  |



#### Scatter Plot

- 연관성을 보기 위해 사용함. 뿌려진 점들의 모양을 보고 연관성을 찾을 수 있음. 

| methods                                                      | roles |
| ------------------------------------------------------------ | ----- |
| `df.plot(kind='scatter', x='math score', y='reading score')` |       |
|                                                              |       |


