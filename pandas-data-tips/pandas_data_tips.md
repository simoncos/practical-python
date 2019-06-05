

```python
import pandas as pd
import numpy as np
```


```python
pd.__version__ # 0.24.2
```




    '0.24.2'



- Getting Started: http://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
    - 10 Minutes to pandas: http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
    - Pandas Cheat Sheet: http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

# Design

## Primary Data Structures

| Dimensions | Name | Description |
| ---------- | ---- | ----------- |
| 1 | Series | homogeneously-typed array |
| 2	| DataFrame | size-mutable tabular structure with potentially heterogeneously-typed column |

- Pandas objects (Index, Series, DataFrame) can be thought of as containers for arrays, which hold the actual data and do the actual computation. For many types, the underlying array is a numpy.ndarray
- DataFrame is a container for Series, and Series is a container for scalars
- insert and remove objects from these containers in a dictionary-like fashion
- the axes are intended to lend more semantic meaning to the data

```python
for col in df.columns:
    series = df[col]
    # do something with series
```

## Mutability and copying of data

- All pandas data structures are value-mutable (the values they contain can be altered) but not always size-mutable.The length of a Series cannot be changed, but, for example, columns can be inserted into a DataFrame.

- However, the vast majority of methods produce new objects and leave the input data untouched. In general we like to favor immutability where sensible.

## Index

https://pandas.pydata.org/pandas-docs/version/0.23.4/api.html#index

`pd.Index`: Immutable ndarray implementing an ordered, sliceable set. The basic object storing axis labels for all pandas objects.


```python
display(pd.Index([1,2,3]))
display(pd.Index([1,3,2]))
display(pd.Index([1,2,3])[:2])
display(pd.Index([1,2,'a']))
display(pd.Index(['a','b','c']))
display(pd.Index(['a','b','b']))
display(pd.DatetimeIndex(['2000-01','2000-03','2001-01']))
```


    Int64Index([1, 2, 3], dtype='int64')



    Int64Index([1, 3, 2], dtype='int64')



    Int64Index([1, 2], dtype='int64')



    Index([1, 2, 'a'], dtype='object')



    Index(['a', 'b', 'c'], dtype='object')



    Index(['a', 'b', 'b'], dtype='object')



    DatetimeIndex(['2000-01-01', '2000-03-01', '2001-01-01'], dtype='datetime64[ns]', freq=None)


## Series

https://pandas.pydata.org/pandas-docs/stable/reference/series.html

index + single column data


```python
sr = pd.Series(data=[1,2], index=['row_1', 'row_2'])
display(sr)
display(type(sr))
```


    row_1    1
    row_2    2
    dtype: int64



    pandas.core.series.Series


## DataFrame

https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

index + tabular data


```python
df = pd.DataFrame(data=[1,2], index=['row_1', 'row_2'], columns=['col_1'])
display(df)

df = pd.DataFrame(data=[1,2], index=[('a',1), ('b',2)], columns=['col_1'])
display(df)

df = pd.DataFrame(data=[[1,2],[2,2]], index=[('a',1), ('b',2)], columns=['col_1', 'col_2'])
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>row_2</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
    </tr>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


### Conversion: Dict


```python
# dict to dataframe

df = pd.DataFrame({'col_1': [10, 'aa', (1,'e'), 30, 45],
                   'col_2': [13, 'cc', (3,'f'), 33, 48],
                   'col_3': [17, 'dd', (5,'g'), 37, 52]})
display(df)

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data, orient='columns')
display(df)

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data, orient='index')
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
      <th>col_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>13</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aa</td>
      <td>cc</td>
      <td>dd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(1, e)</td>
      <td>(3, f)</td>
      <td>(5, g)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>33</td>
      <td>37</td>
    </tr>
    <tr>
      <th>4</th>
      <td>45</td>
      <td>48</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_1</th>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>row_2</th>
      <td>a</td>
      <td>b</td>
      <td>c</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
</div>



```python
# dataframe to dict

df = pd.DataFrame({'col_1': [10, 'aa', (1,'e'), 30, 45],
                   'col_2': [13, 'cc', (3,'f'), 33, 48],
                   'col_3': [17, 'dd', (5,'g'), 37, 52]})
display(df)

print('----------\norient=dict:')
display( df.to_dict(orient='dict')) # default
print('orient=list:')
display(df.to_dict(orient='list'))

print('----------\norient=records:')
display(df.to_dict(orient='records'))
print('orient=index:')
display(df.to_dict(orient='index'))

print('----------\norient=split:')
display(df.to_dict(orient='split'))

print('----------\norient=series:')
display(df.to_dict(orient='series'))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
      <th>col_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>13</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aa</td>
      <td>cc</td>
      <td>dd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(1, e)</td>
      <td>(3, f)</td>
      <td>(5, g)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>33</td>
      <td>37</td>
    </tr>
    <tr>
      <th>4</th>
      <td>45</td>
      <td>48</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>


    ----------
    orient=dict:



    {'col_1': {0: 10, 1: 'aa', 2: (1, 'e'), 3: 30, 4: 45},
     'col_2': {0: 13, 1: 'cc', 2: (3, 'f'), 3: 33, 4: 48},
     'col_3': {0: 17, 1: 'dd', 2: (5, 'g'), 3: 37, 4: 52}}


    orient=list:



    {'col_1': [10, 'aa', (1, 'e'), 30, 45],
     'col_2': [13, 'cc', (3, 'f'), 33, 48],
     'col_3': [17, 'dd', (5, 'g'), 37, 52]}


    ----------
    orient=records:



    [{'col_1': 10, 'col_2': 13, 'col_3': 17},
     {'col_1': 'aa', 'col_2': 'cc', 'col_3': 'dd'},
     {'col_1': (1, 'e'), 'col_2': (3, 'f'), 'col_3': (5, 'g')},
     {'col_1': 30, 'col_2': 33, 'col_3': 37},
     {'col_1': 45, 'col_2': 48, 'col_3': 52}]


    orient=index:



    {0: {'col_1': 10, 'col_2': 13, 'col_3': 17},
     1: {'col_1': 'aa', 'col_2': 'cc', 'col_3': 'dd'},
     2: {'col_1': (1, 'e'), 'col_2': (3, 'f'), 'col_3': (5, 'g')},
     3: {'col_1': 30, 'col_2': 33, 'col_3': 37},
     4: {'col_1': 45, 'col_2': 48, 'col_3': 52}}


    ----------
    orient=split:



    {'index': [0, 1, 2, 3, 4],
     'columns': ['col_1', 'col_2', 'col_3'],
     'data': [[10, 13, 17],
      ['aa', 'cc', 'dd'],
      [(1, 'e'), (3, 'f'), (5, 'g')],
      [30, 33, 37],
      [45, 48, 52]]}


    ----------
    orient=series:



    {'col_1': 0        10
     1        aa
     2    (1, e)
     3        30
     4        45
     Name: col_1, dtype: object, 'col_2': 0        13
     1        cc
     2    (3, f)
     3        33
     4        48
     Name: col_2, dtype: object, 'col_3': 0        17
     1        dd
     2    (5, g)
     3        37
     4        52
     Name: col_3, dtype: object}


### Conversion: Numpy Array


```python
# array to dataframe
display(pd.DataFrame(np.array([3,2,1,0])))
display(pd.DataFrame(np.array([[3,2],[1,0]])))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



```python
# dataframe to array
df = pd.DataFrame({'col_1': [10, 'aa', (1,'e'), 30, 45],
                   'col_2': [13, 'cc', (3,'f'), 33, 48],
                   'col_3': [17, 'dd', (5,'g'), 37, 52]})
display(df)
display(df.to_numpy()) # Depreciated: .values / as_matrix()
display(df.to_numpy().T) 
display(df.T.to_numpy()) 
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
      <th>col_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>13</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aa</td>
      <td>cc</td>
      <td>dd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(1, e)</td>
      <td>(3, f)</td>
      <td>(5, g)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>33</td>
      <td>37</td>
    </tr>
    <tr>
      <th>4</th>
      <td>45</td>
      <td>48</td>
      <td>52</td>
    </tr>
  </tbody>
</table>
</div>



    array([[10, 13, 17],
           ['aa', 'cc', 'dd'],
           [(1, 'e'), (3, 'f'), (5, 'g')],
           [30, 33, 37],
           [45, 48, 52]], dtype=object)



    array([[10, 'aa', (1, 'e'), 30, 45],
           [13, 'cc', (3, 'f'), 33, 48],
           [17, 'dd', (5, 'g'), 37, 52]], dtype=object)



    array([[10, 'aa', (1, 'e'), 30, 45],
           [13, 'cc', (3, 'f'), 33, 48],
           [17, 'dd', (5, 'g'), 37, 52]], dtype=object)


### Reset Index


```python
df = pd.DataFrame(data=[1,2], index=[('a',1), ('b',2)], columns=['col_1'])
display(df)

display(df.reset_index())
display(df.reset_index(drop=True))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
    </tr>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>(a, 1)</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>(b, 2)</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


# File IO

## Input

- `pd.read_json`
- `pd.read_excel`
- `pd.read_csv`
- `pd.read_pickle` # for pandas objects or other objects such as python dict

More: https://pandas.pydata.org/pandas-docs/stable/reference/io.html

## Output

- `df.to_csv`
- `df.to_dict(orient=)`
- `df.to_excel`
- `df.to_pickle`

More: https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#serialization-io-conversion

### Excel with Style

StyleFrame: https://styleframe.readthedocs.io/en/0.2/#


```python
# Excel with style
from StyleFrame import StyleFrame, Styler

sf = StyleFrame.read_excel('xxx.xlsx', sheet_name='Sheet1') #, read_style=True / StyleFrame support only .xlsx

font_blue = Styler(font_color='blue')
font_red = Styler(font_color='red')

for col_name in sf.columns:
    sf.apply_style_by_indexes(indexes_to_style=sf[sf[col_name].isin(some_list)], # decide rows
                              styler_obj=font_blue,
                              cols_to_style=col_name) # decide cols
    sf.apply_style_by_indexes(indexes_to_style=sf[sf[col_name].isin(another_list)],
                              styler_obj=font_red,
                              cols_to_style=col_name)

sf.to_excel('xxx_styled.xlsx').save()
```

# Indexing / Selecting / Slicing

https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

index的label和integer position

## [ ]

- series: select row
- dataframe: select column


```python
sr = pd.Series(data=['aa','bb','cc', 'dd'], index=['a',1,2,3])
display(sr)
display(sr[pd.Index([1,3,2])])
display(sr[[1,3,2]])
display(sr[[1,'a',2]])
```


    a    aa
    1    bb
    2    cc
    3    dd
    dtype: object



    1    bb
    3    dd
    2    cc
    dtype: object



    1    bb
    3    dd
    2    cc
    dtype: object



    1    bb
    a    aa
    2    cc
    dtype: object



```python
df = pd.DataFrame(data=[[1,2],[3,4]], index=['row_1', 'row_2'], columns=['col_1','col_2'])
display(df)
display(df[['col_1']]) # column
# df[['row_1', 'row_2']] Error
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>row_2</th>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>row_2</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


## loc / iloc

### single index


```python
sr = pd.Series(data=['aa','bb','cc', 'dd'], index=['a',1,2,3])
display(sr)
```


    a    aa
    1    bb
    2    cc
    3    dd
    dtype: object



```python
df = pd.DataFrame(data=[1,2], index=['row_1', 'row_2'], columns=['col_1'])
display(df)
display(df.loc[['row_1', 'row_2']])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>row_2</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row_1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>row_2</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



```python
try:
    df.loc[('row_1', 'row_2')] # for multiindex: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
except Exception as e:
    print(type(e), e)
```

    <class 'KeyError'> 'row_2'


### tuple index


```python
df = pd.DataFrame(data=[1,2], index=[('a',1), ('b',2)], columns=['col_1'])
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
    </tr>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



```python
df.loc[('a',1)] # KeyError: 'a'
df.loc[('a',1),] # KeyError: "None of [('a', 1)] are in the [index]"
```


```python
display(df.loc[[('a',1)],])
display(df.loc[[('a',1),],])
display(df.loc[[('a',1), ('b',2)],])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
    </tr>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(df.loc[[('a',1),], 'col_1'])
```


    (a, 1)    1
    Name: col_1, dtype: int64


### hierarchical index (MultiIndex)

https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html


```python
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])] 
df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>1.086379</td>
      <td>-0.175958</td>
      <td>-0.362664</td>
      <td>-3.272982</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.144050</td>
      <td>0.675604</td>
      <td>0.828706</td>
      <td>-0.804913</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>2.520758</td>
      <td>-0.764423</td>
      <td>0.393462</td>
      <td>0.241439</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.212127</td>
      <td>0.879288</td>
      <td>1.259585</td>
      <td>-0.384230</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-2.359296</td>
      <td>-1.454042</td>
      <td>-1.251561</td>
      <td>-0.213912</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.453393</td>
      <td>-1.505561</td>
      <td>-0.959798</td>
      <td>1.392145</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>0.362104</td>
      <td>0.943573</td>
      <td>0.002784</td>
      <td>-1.076853</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.699699</td>
      <td>1.628535</td>
      <td>1.537032</td>
      <td>-0.600601</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(df.loc[('baz', 'two')]) # series
display(df.loc[[('baz', 'two')]]) # dataframe
display(df.loc[[('baz', 'two'), ('foo', 'one')]]) # dataframe
```


    0   -0.212127
    1    0.879288
    2    1.259585
    3   -0.384230
    Name: (baz, two), dtype: float64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baz</th>
      <th>two</th>
      <td>-0.212127</td>
      <td>0.879288</td>
      <td>1.259585</td>
      <td>-0.38423</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baz</th>
      <th>two</th>
      <td>-0.212127</td>
      <td>0.879288</td>
      <td>1.259585</td>
      <td>-0.384230</td>
    </tr>
    <tr>
      <th>foo</th>
      <th>one</th>
      <td>-2.359296</td>
      <td>-1.454042</td>
      <td>-1.251561</td>
      <td>-0.213912</td>
    </tr>
  </tbody>
</table>
</div>


### iloc


```python
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)

display(df.iloc[0]) # series
display(df.iloc[-1])

display(df.iloc[0:2]) # dataframe
display(df.iloc[1:])
display(df.iloc[-1:])
display(df.iloc[::2])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



    AAA      4
    BBB     10
    CCC    100
    Name: 0, dtype: int64



    AAA     7
    BBB    40
    CCC   -50
    Name: 3, dtype: int64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>


## Boolean Filtering


```python
df = pd.DataFrame(data=[[1,2],[2,1]], index=[('a',1), ('b',2)], columns=['col_1', 'col_2'])
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(type(df['col_1'] == 1))
display(df['col_1'] == 1)
display(df[df['col_1'] == 1])
```


    pandas.core.series.Series



    (a, 1)     True
    (b, 2)    False
    Name: col_1, dtype: bool



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(a, 1)</th>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



```python
# combine

bool_1 = df['col_1'] == 2
bool_2 = df['col_2'] == 1
display(bool_1)
display(bool_2)
display(bool_1 & bool_2)
display(df[bool_1 & bool_2])
```


    (a, 1)    False
    (b, 2)     True
    Name: col_1, dtype: bool



    (a, 1)    False
    (b, 2)     True
    Name: col_2, dtype: bool



    (a, 1)    False
    (b, 2)     True
    dtype: bool



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_1</th>
      <th>col_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(b, 2)</th>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



```python
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)

display(df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))])

display(df.loc[(df['BBB'] > 25) | (df['CCC'] >= -40), 'AAA'])
display(df)

df.loc[(df['BBB'] > 25) | (df['CCC'] >= -40), 'AAA'] = 1
display(df)

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>



    0    4
    1    5
    2    6
    3    7
    Name: AAA, dtype: int64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>


## sample


```python
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)
display(df.sample(n=2))
display(df.sample(n=2, axis=1))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>


# Math

https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats


## Unary Operation


```python
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(sum(df['AAA'])) # == df['AAA'].sum()
display(max(df['AAA'])) # == df['AAA'].max()
display(df['AAA'].mean())
display(df['AAA'].value_counts()) # series

display(df.sum()) # series
display(df * 2) # dataframe
display(df.describe()) # dataframe
```


    22



    7



    5.5



    7    1
    6    1
    5    1
    4    1
    Name: AAA, dtype: int64



    AAA     22
    BBB    100
    CCC     70
    dtype: int64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>20</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>40</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>60</td>
      <td>-60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14</td>
      <td>80</td>
      <td>-100</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.500000</td>
      <td>25.000000</td>
      <td>17.500000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.290994</td>
      <td>12.909944</td>
      <td>69.940451</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.000000</td>
      <td>10.000000</td>
      <td>-50.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.750000</td>
      <td>17.500000</td>
      <td>-35.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.500000</td>
      <td>25.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.250000</td>
      <td>32.500000</td>
      <td>62.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.000000</td>
      <td>40.000000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>


## Binary Operation


```python
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(df['AAA'] + df['BBB'])
display(df['AAA'] * df['BBB'])

import scipy.spatial.distance as distance
display(1 - distance.cosine(df['AAA'], df['BBB']))
```


    0    14
    1    25
    2    36
    3    47
    dtype: int64



    0     40
    1    100
    2    180
    3    280
    dtype: int64



    0.9759000729485331


# Iteration


do not have to convert to list/dict, Pandas can do iteration - performance


```python
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>


## Along axis


```python
for col in df:
    print(col)
```

    AAA
    BBB
    CCC



```python
for columns, series in df.iteritems():
    print(columns)
    print(series)
```

    AAA
    0    4
    1    5
    2    6
    3    7
    Name: AAA, dtype: int64
    BBB
    0    10
    1    20
    2    30
    3    40
    Name: BBB, dtype: int64
    CCC
    0    100
    1     50
    2    -30
    3    -50
    Name: CCC, dtype: int64



```python
for index, series in df.iterrows():
    print(index)
    print(series)

for row in df.itertuples():
    print(row)
```

    0
    AAA      4
    BBB     10
    CCC    100
    Name: 0, dtype: int64
    1
    AAA     5
    BBB    20
    CCC    50
    Name: 1, dtype: int64
    2
    AAA     6
    BBB    30
    CCC   -30
    Name: 2, dtype: int64
    3
    AAA     7
    BBB    40
    CCC   -50
    Name: 3, dtype: int64
    Pandas(Index=0, AAA=4, BBB=10, CCC=100)
    Pandas(Index=1, AAA=5, BBB=20, CCC=50)
    Pandas(Index=2, AAA=6, BBB=30, CCC=-30)
    Pandas(Index=3, AAA=7, BBB=40, CCC=-50)


## Apply / Map

- `map` works element-wise on a Series.
- `applymap` works element-wise on a DataFrame
- `apply` works on a row / column basis of a DataFrame (`df.apply()`), also works on series(`sr.apply()`)
    - If func returns a scalar or a list, `apply(func)` returns a Series.
    - If func returns a Series, `apply(func)` returns a DataFrame.


- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.applymap.html
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html



```python
import math

df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)
display(df['AAA'].apply(math.sqrt))
display(df.apply(np.sqrt, axis=0))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



    0    2.000000
    1    2.236068
    2    2.449490
    3    2.645751
    Name: AAA, dtype: float64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.000000</td>
      <td>3.162278</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.236068</td>
      <td>4.472136</td>
      <td>7.071068</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.449490</td>
      <td>5.477226</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.645751</td>
      <td>6.324555</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



```python
# apply + lambda

display(df['AAA'].apply(lambda x: pd.Series([x] * 5)))
display(df.apply(lambda x: x.loc[0] + 1, axis=0)) # index (row), axis=0
display(df.apply(lambda x: x, axis=1)) # column, axis=1
display(df.apply(lambda x: x.loc['AAA'] + 1, axis=1)) # column
display(df.apply(lambda x: x.loc['AAA'] + x.loc['BBB'], axis=1)) # multi-columns, same as: df['AAA'] + df['BBB']
display(df.apply(lambda x: max([x['BBB'], x['CCC']]), axis=1))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



    AAA      5
    BBB     11
    CCC    101
    dtype: int64



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



    0    5
    1    6
    2    7
    3    8
    dtype: int64



    0    14
    1    25
    2    36
    3    47
    dtype: int64



    0    100
    1     50
    2     30
    3     40
    dtype: int64



```python
# Normalize

df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
display(df)
df['CCC'] = df['CCC'].apply(lambda x: x/max(df['CCC'])) 
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-0.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-0.5</td>
    </tr>
  </tbody>
</table>
</div>


### Apply with Progress Bar


```python
from tqdm import tqdm

tqdm.pandas()

df.progress_apply(lambda x: max([x['BBB'], x['CCC']]), axis=1)
```

    100%|██████████| 4/4 [00:00<00:00, 2043.26it/s]





    0    10.0
    1    20.0
    2    30.0
    3    40.0
    dtype: float64




```python
from tqdm.autonotebook import tqdm

tqdm.pandas()

df.progress_apply(lambda x: max([x['BBB'], x['CCC']]), axis=1)
```

    /root/anaconda3/lib/python3.7/site-packages/tqdm/autonotebook/__init__.py:14: TqdmExperimentalWarning: Using `tqdm.autonotebook.tqdm` in notebook mode. Use `tqdm.tqdm` instead to force console mode (e.g. in jupyter console)
      " (e.g. in jupyter console)", TqdmExperimentalWarning)



    HBox(children=(IntProgress(value=0, max=4), HTML(value='')))


    





    0    10.0
    1    20.0
    2    30.0
    3    40.0
    dtype: float64



## Group

1. Splitting the data into groups based on some criteria
2. Applying a function to each group independently
3. Combining the results into a data structure


- https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
- https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

### Structure


```python
df = pd.DataFrame({'AAA': [1, 2, 8, 2],
                   'BBB': [1, 20, 30, 40],
                   'CCC': [0, 50, -30, -50]})
display(df)

grouped = df.groupby('AAA')
print(type(grouped))
print(grouped)

print('------------')

print(grouped.groups)
print(grouped.groups[8])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>


    <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fd539a2ee80>
    ------------
    {1: Int64Index([0], dtype='int64'), 2: Int64Index([1, 3], dtype='int64'), 8: Int64Index([2], dtype='int64')}
    Int64Index([2], dtype='int64')


### Iteration



```python
for name, data in grouped: # iterated as tuple(name, data)
    print(name)
    print(type(data), data)
```

    1
    <class 'pandas.core.frame.DataFrame'>    AAA  BBB  CCC
    0    1    1    0
    2
    <class 'pandas.core.frame.DataFrame'>    AAA  BBB  CCC
    1    2   20   50
    3    2   40  -50
    8
    <class 'pandas.core.frame.DataFrame'>    AAA  BBB  CCC
    2    8   30  -30


### Grouped by Time Period


```python
dates = pd.date_range('1/10/2000', periods=60)

df = pd.DataFrame(np.random.randn(60, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-10</th>
      <td>1.879183</td>
      <td>-0.282015</td>
      <td>-0.812072</td>
      <td>0.774624</td>
    </tr>
    <tr>
      <th>2000-01-11</th>
      <td>-0.430260</td>
      <td>-0.766843</td>
      <td>0.880136</td>
      <td>0.117777</td>
    </tr>
    <tr>
      <th>2000-01-12</th>
      <td>1.550647</td>
      <td>0.863026</td>
      <td>0.773138</td>
      <td>0.448203</td>
    </tr>
    <tr>
      <th>2000-01-13</th>
      <td>0.047851</td>
      <td>-1.312712</td>
      <td>-0.319924</td>
      <td>-0.250159</td>
    </tr>
    <tr>
      <th>2000-01-14</th>
      <td>0.408329</td>
      <td>-0.188547</td>
      <td>0.592483</td>
      <td>1.566940</td>
    </tr>
    <tr>
      <th>2000-01-15</th>
      <td>-0.983973</td>
      <td>-1.601270</td>
      <td>-0.662061</td>
      <td>0.656442</td>
    </tr>
    <tr>
      <th>2000-01-16</th>
      <td>1.708260</td>
      <td>-0.412328</td>
      <td>-0.125563</td>
      <td>0.519124</td>
    </tr>
    <tr>
      <th>2000-01-17</th>
      <td>0.126432</td>
      <td>-0.805028</td>
      <td>1.057307</td>
      <td>-0.642352</td>
    </tr>
    <tr>
      <th>2000-01-18</th>
      <td>-0.901246</td>
      <td>-2.330404</td>
      <td>0.775472</td>
      <td>-0.280216</td>
    </tr>
    <tr>
      <th>2000-01-19</th>
      <td>-1.515402</td>
      <td>-0.355997</td>
      <td>0.073722</td>
      <td>1.600156</td>
    </tr>
    <tr>
      <th>2000-01-20</th>
      <td>2.077658</td>
      <td>-1.820557</td>
      <td>-0.456590</td>
      <td>0.269721</td>
    </tr>
    <tr>
      <th>2000-01-21</th>
      <td>-1.046665</td>
      <td>-0.992133</td>
      <td>0.481277</td>
      <td>-0.147215</td>
    </tr>
    <tr>
      <th>2000-01-22</th>
      <td>-0.480208</td>
      <td>-0.427384</td>
      <td>-0.000824</td>
      <td>0.826097</td>
    </tr>
    <tr>
      <th>2000-01-23</th>
      <td>-0.631563</td>
      <td>1.368086</td>
      <td>-1.347121</td>
      <td>-2.345722</td>
    </tr>
    <tr>
      <th>2000-01-24</th>
      <td>0.140738</td>
      <td>-0.412111</td>
      <td>0.571476</td>
      <td>-0.456314</td>
    </tr>
    <tr>
      <th>2000-01-25</th>
      <td>-1.130528</td>
      <td>0.290524</td>
      <td>0.711561</td>
      <td>0.562747</td>
    </tr>
    <tr>
      <th>2000-01-26</th>
      <td>0.440369</td>
      <td>-2.498611</td>
      <td>0.419082</td>
      <td>-1.681362</td>
    </tr>
    <tr>
      <th>2000-01-27</th>
      <td>0.529171</td>
      <td>0.221156</td>
      <td>0.160933</td>
      <td>-0.005621</td>
    </tr>
    <tr>
      <th>2000-01-28</th>
      <td>1.415482</td>
      <td>1.032559</td>
      <td>0.483723</td>
      <td>0.933316</td>
    </tr>
    <tr>
      <th>2000-01-29</th>
      <td>0.152102</td>
      <td>-0.158823</td>
      <td>0.167715</td>
      <td>-1.826133</td>
    </tr>
    <tr>
      <th>2000-01-30</th>
      <td>-0.027573</td>
      <td>0.742606</td>
      <td>-0.788746</td>
      <td>1.646971</td>
    </tr>
    <tr>
      <th>2000-01-31</th>
      <td>-0.668336</td>
      <td>1.593356</td>
      <td>0.383978</td>
      <td>-0.391833</td>
    </tr>
    <tr>
      <th>2000-02-01</th>
      <td>1.285738</td>
      <td>0.329043</td>
      <td>1.041265</td>
      <td>-0.819866</td>
    </tr>
    <tr>
      <th>2000-02-02</th>
      <td>0.780435</td>
      <td>-1.380364</td>
      <td>-1.673513</td>
      <td>1.477997</td>
    </tr>
    <tr>
      <th>2000-02-03</th>
      <td>-0.249775</td>
      <td>-1.687410</td>
      <td>-0.036901</td>
      <td>-0.168110</td>
    </tr>
    <tr>
      <th>2000-02-04</th>
      <td>0.441963</td>
      <td>0.661410</td>
      <td>0.040005</td>
      <td>0.658418</td>
    </tr>
    <tr>
      <th>2000-02-05</th>
      <td>-0.467108</td>
      <td>-0.945761</td>
      <td>-0.036857</td>
      <td>-0.222480</td>
    </tr>
    <tr>
      <th>2000-02-06</th>
      <td>-0.860951</td>
      <td>-1.898914</td>
      <td>0.713060</td>
      <td>-0.206733</td>
    </tr>
    <tr>
      <th>2000-02-07</th>
      <td>0.421550</td>
      <td>0.013269</td>
      <td>-0.125181</td>
      <td>1.173027</td>
    </tr>
    <tr>
      <th>2000-02-08</th>
      <td>-1.557519</td>
      <td>-0.231209</td>
      <td>-1.347163</td>
      <td>0.348486</td>
    </tr>
    <tr>
      <th>2000-02-09</th>
      <td>1.093544</td>
      <td>0.347288</td>
      <td>0.778088</td>
      <td>-0.210887</td>
    </tr>
    <tr>
      <th>2000-02-10</th>
      <td>-1.007827</td>
      <td>1.198809</td>
      <td>-0.616618</td>
      <td>0.559148</td>
    </tr>
    <tr>
      <th>2000-02-11</th>
      <td>1.685716</td>
      <td>0.769161</td>
      <td>-0.522652</td>
      <td>1.040180</td>
    </tr>
    <tr>
      <th>2000-02-12</th>
      <td>0.732024</td>
      <td>-0.233874</td>
      <td>-0.729638</td>
      <td>0.183623</td>
    </tr>
    <tr>
      <th>2000-02-13</th>
      <td>0.469342</td>
      <td>-0.074991</td>
      <td>1.551511</td>
      <td>2.004232</td>
    </tr>
    <tr>
      <th>2000-02-14</th>
      <td>-0.750399</td>
      <td>0.503922</td>
      <td>0.931430</td>
      <td>-0.605640</td>
    </tr>
    <tr>
      <th>2000-02-15</th>
      <td>0.797389</td>
      <td>0.527649</td>
      <td>1.194978</td>
      <td>0.650961</td>
    </tr>
    <tr>
      <th>2000-02-16</th>
      <td>0.363964</td>
      <td>1.185855</td>
      <td>0.546622</td>
      <td>0.275241</td>
    </tr>
    <tr>
      <th>2000-02-17</th>
      <td>-0.866436</td>
      <td>0.505301</td>
      <td>-0.953725</td>
      <td>-0.474443</td>
    </tr>
    <tr>
      <th>2000-02-18</th>
      <td>0.121093</td>
      <td>0.230785</td>
      <td>1.930369</td>
      <td>1.135993</td>
    </tr>
    <tr>
      <th>2000-02-19</th>
      <td>0.418273</td>
      <td>0.126150</td>
      <td>-0.136750</td>
      <td>-0.099249</td>
    </tr>
    <tr>
      <th>2000-02-20</th>
      <td>1.113853</td>
      <td>-0.685349</td>
      <td>0.263227</td>
      <td>-0.372289</td>
    </tr>
    <tr>
      <th>2000-02-21</th>
      <td>0.317351</td>
      <td>0.485224</td>
      <td>0.031511</td>
      <td>-1.565946</td>
    </tr>
    <tr>
      <th>2000-02-22</th>
      <td>-0.764952</td>
      <td>0.565166</td>
      <td>0.017759</td>
      <td>-1.387330</td>
    </tr>
    <tr>
      <th>2000-02-23</th>
      <td>0.694061</td>
      <td>0.884745</td>
      <td>0.183642</td>
      <td>0.667891</td>
    </tr>
    <tr>
      <th>2000-02-24</th>
      <td>-0.329406</td>
      <td>-2.326962</td>
      <td>0.260697</td>
      <td>0.313343</td>
    </tr>
    <tr>
      <th>2000-02-25</th>
      <td>-0.281537</td>
      <td>-0.354575</td>
      <td>-0.540512</td>
      <td>-0.228770</td>
    </tr>
    <tr>
      <th>2000-02-26</th>
      <td>1.993343</td>
      <td>-0.116143</td>
      <td>0.809022</td>
      <td>0.876005</td>
    </tr>
    <tr>
      <th>2000-02-27</th>
      <td>0.801768</td>
      <td>-0.973785</td>
      <td>0.216941</td>
      <td>-0.633814</td>
    </tr>
    <tr>
      <th>2000-02-28</th>
      <td>0.685388</td>
      <td>0.344020</td>
      <td>-0.618957</td>
      <td>0.746396</td>
    </tr>
    <tr>
      <th>2000-02-29</th>
      <td>0.220366</td>
      <td>-0.524952</td>
      <td>-0.077050</td>
      <td>1.339360</td>
    </tr>
    <tr>
      <th>2000-03-01</th>
      <td>-0.465886</td>
      <td>-0.565051</td>
      <td>0.249617</td>
      <td>0.883099</td>
    </tr>
    <tr>
      <th>2000-03-02</th>
      <td>-0.286343</td>
      <td>0.853820</td>
      <td>0.132625</td>
      <td>1.956263</td>
    </tr>
    <tr>
      <th>2000-03-03</th>
      <td>-1.010800</td>
      <td>-0.634513</td>
      <td>-0.059249</td>
      <td>-1.322195</td>
    </tr>
    <tr>
      <th>2000-03-04</th>
      <td>0.824529</td>
      <td>0.591027</td>
      <td>-1.786807</td>
      <td>1.384207</td>
    </tr>
    <tr>
      <th>2000-03-05</th>
      <td>-0.103306</td>
      <td>-1.431728</td>
      <td>-0.077431</td>
      <td>-0.126732</td>
    </tr>
    <tr>
      <th>2000-03-06</th>
      <td>0.755524</td>
      <td>1.460424</td>
      <td>-1.109814</td>
      <td>-0.568003</td>
    </tr>
    <tr>
      <th>2000-03-07</th>
      <td>-1.508068</td>
      <td>-0.370230</td>
      <td>0.008641</td>
      <td>1.275203</td>
    </tr>
    <tr>
      <th>2000-03-08</th>
      <td>-0.867791</td>
      <td>-0.276403</td>
      <td>-0.550362</td>
      <td>-0.378691</td>
    </tr>
    <tr>
      <th>2000-03-09</th>
      <td>-2.506244</td>
      <td>0.430844</td>
      <td>-0.074127</td>
      <td>-0.759110</td>
    </tr>
  </tbody>
</table>
</div>



```python
for name, data in df.groupby(pd.Grouper(freq='M')): # or '1M'
    print('\n', name)
    print(data)
```

    
     2000-01-31 00:00:00
                       A         B         C         D
    2000-01-10  1.879183 -0.282015 -0.812072  0.774624
    2000-01-11 -0.430260 -0.766843  0.880136  0.117777
    2000-01-12  1.550647  0.863026  0.773138  0.448203
    2000-01-13  0.047851 -1.312712 -0.319924 -0.250159
    2000-01-14  0.408329 -0.188547  0.592483  1.566940
    2000-01-15 -0.983973 -1.601270 -0.662061  0.656442
    2000-01-16  1.708260 -0.412328 -0.125563  0.519124
    2000-01-17  0.126432 -0.805028  1.057307 -0.642352
    2000-01-18 -0.901246 -2.330404  0.775472 -0.280216
    2000-01-19 -1.515402 -0.355997  0.073722  1.600156
    2000-01-20  2.077658 -1.820557 -0.456590  0.269721
    2000-01-21 -1.046665 -0.992133  0.481277 -0.147215
    2000-01-22 -0.480208 -0.427384 -0.000824  0.826097
    2000-01-23 -0.631563  1.368086 -1.347121 -2.345722
    2000-01-24  0.140738 -0.412111  0.571476 -0.456314
    2000-01-25 -1.130528  0.290524  0.711561  0.562747
    2000-01-26  0.440369 -2.498611  0.419082 -1.681362
    2000-01-27  0.529171  0.221156  0.160933 -0.005621
    2000-01-28  1.415482  1.032559  0.483723  0.933316
    2000-01-29  0.152102 -0.158823  0.167715 -1.826133
    2000-01-30 -0.027573  0.742606 -0.788746  1.646971
    2000-01-31 -0.668336  1.593356  0.383978 -0.391833
    
     2000-02-29 00:00:00
                       A         B         C         D
    2000-02-01  1.285738  0.329043  1.041265 -0.819866
    2000-02-02  0.780435 -1.380364 -1.673513  1.477997
    2000-02-03 -0.249775 -1.687410 -0.036901 -0.168110
    2000-02-04  0.441963  0.661410  0.040005  0.658418
    2000-02-05 -0.467108 -0.945761 -0.036857 -0.222480
    2000-02-06 -0.860951 -1.898914  0.713060 -0.206733
    2000-02-07  0.421550  0.013269 -0.125181  1.173027
    2000-02-08 -1.557519 -0.231209 -1.347163  0.348486
    2000-02-09  1.093544  0.347288  0.778088 -0.210887
    2000-02-10 -1.007827  1.198809 -0.616618  0.559148
    2000-02-11  1.685716  0.769161 -0.522652  1.040180
    2000-02-12  0.732024 -0.233874 -0.729638  0.183623
    2000-02-13  0.469342 -0.074991  1.551511  2.004232
    2000-02-14 -0.750399  0.503922  0.931430 -0.605640
    2000-02-15  0.797389  0.527649  1.194978  0.650961
    2000-02-16  0.363964  1.185855  0.546622  0.275241
    2000-02-17 -0.866436  0.505301 -0.953725 -0.474443
    2000-02-18  0.121093  0.230785  1.930369  1.135993
    2000-02-19  0.418273  0.126150 -0.136750 -0.099249
    2000-02-20  1.113853 -0.685349  0.263227 -0.372289
    2000-02-21  0.317351  0.485224  0.031511 -1.565946
    2000-02-22 -0.764952  0.565166  0.017759 -1.387330
    2000-02-23  0.694061  0.884745  0.183642  0.667891
    2000-02-24 -0.329406 -2.326962  0.260697  0.313343
    2000-02-25 -0.281537 -0.354575 -0.540512 -0.228770
    2000-02-26  1.993343 -0.116143  0.809022  0.876005
    2000-02-27  0.801768 -0.973785  0.216941 -0.633814
    2000-02-28  0.685388  0.344020 -0.618957  0.746396
    2000-02-29  0.220366 -0.524952 -0.077050  1.339360
    
     2000-03-31 00:00:00
                       A         B         C         D
    2000-03-01 -0.465886 -0.565051  0.249617  0.883099
    2000-03-02 -0.286343  0.853820  0.132625  1.956263
    2000-03-03 -1.010800 -0.634513 -0.059249 -1.322195
    2000-03-04  0.824529  0.591027 -1.786807  1.384207
    2000-03-05 -0.103306 -1.431728 -0.077431 -0.126732
    2000-03-06  0.755524  1.460424 -1.109814 -0.568003
    2000-03-07 -1.508068 -0.370230  0.008641  1.275203
    2000-03-08 -0.867791 -0.276403 -0.550362 -0.378691
    2000-03-09 -2.506244  0.430844 -0.074127 -0.759110



```python
for name, data in df.groupby(pd.Grouper(freq='30d')):
    print('\n', name)
    print(data)
```

    
     2000-01-10 00:00:00
                       A         B         C         D
    2000-01-10  1.879183 -0.282015 -0.812072  0.774624
    2000-01-11 -0.430260 -0.766843  0.880136  0.117777
    2000-01-12  1.550647  0.863026  0.773138  0.448203
    2000-01-13  0.047851 -1.312712 -0.319924 -0.250159
    2000-01-14  0.408329 -0.188547  0.592483  1.566940
    2000-01-15 -0.983973 -1.601270 -0.662061  0.656442
    2000-01-16  1.708260 -0.412328 -0.125563  0.519124
    2000-01-17  0.126432 -0.805028  1.057307 -0.642352
    2000-01-18 -0.901246 -2.330404  0.775472 -0.280216
    2000-01-19 -1.515402 -0.355997  0.073722  1.600156
    2000-01-20  2.077658 -1.820557 -0.456590  0.269721
    2000-01-21 -1.046665 -0.992133  0.481277 -0.147215
    2000-01-22 -0.480208 -0.427384 -0.000824  0.826097
    2000-01-23 -0.631563  1.368086 -1.347121 -2.345722
    2000-01-24  0.140738 -0.412111  0.571476 -0.456314
    2000-01-25 -1.130528  0.290524  0.711561  0.562747
    2000-01-26  0.440369 -2.498611  0.419082 -1.681362
    2000-01-27  0.529171  0.221156  0.160933 -0.005621
    2000-01-28  1.415482  1.032559  0.483723  0.933316
    2000-01-29  0.152102 -0.158823  0.167715 -1.826133
    2000-01-30 -0.027573  0.742606 -0.788746  1.646971
    2000-01-31 -0.668336  1.593356  0.383978 -0.391833
    2000-02-01  1.285738  0.329043  1.041265 -0.819866
    2000-02-02  0.780435 -1.380364 -1.673513  1.477997
    2000-02-03 -0.249775 -1.687410 -0.036901 -0.168110
    2000-02-04  0.441963  0.661410  0.040005  0.658418
    2000-02-05 -0.467108 -0.945761 -0.036857 -0.222480
    2000-02-06 -0.860951 -1.898914  0.713060 -0.206733
    2000-02-07  0.421550  0.013269 -0.125181  1.173027
    2000-02-08 -1.557519 -0.231209 -1.347163  0.348486
    
     2000-02-09 00:00:00
                       A         B         C         D
    2000-02-09  1.093544  0.347288  0.778088 -0.210887
    2000-02-10 -1.007827  1.198809 -0.616618  0.559148
    2000-02-11  1.685716  0.769161 -0.522652  1.040180
    2000-02-12  0.732024 -0.233874 -0.729638  0.183623
    2000-02-13  0.469342 -0.074991  1.551511  2.004232
    2000-02-14 -0.750399  0.503922  0.931430 -0.605640
    2000-02-15  0.797389  0.527649  1.194978  0.650961
    2000-02-16  0.363964  1.185855  0.546622  0.275241
    2000-02-17 -0.866436  0.505301 -0.953725 -0.474443
    2000-02-18  0.121093  0.230785  1.930369  1.135993
    2000-02-19  0.418273  0.126150 -0.136750 -0.099249
    2000-02-20  1.113853 -0.685349  0.263227 -0.372289
    2000-02-21  0.317351  0.485224  0.031511 -1.565946
    2000-02-22 -0.764952  0.565166  0.017759 -1.387330
    2000-02-23  0.694061  0.884745  0.183642  0.667891
    2000-02-24 -0.329406 -2.326962  0.260697  0.313343
    2000-02-25 -0.281537 -0.354575 -0.540512 -0.228770
    2000-02-26  1.993343 -0.116143  0.809022  0.876005
    2000-02-27  0.801768 -0.973785  0.216941 -0.633814
    2000-02-28  0.685388  0.344020 -0.618957  0.746396
    2000-02-29  0.220366 -0.524952 -0.077050  1.339360
    2000-03-01 -0.465886 -0.565051  0.249617  0.883099
    2000-03-02 -0.286343  0.853820  0.132625  1.956263
    2000-03-03 -1.010800 -0.634513 -0.059249 -1.322195
    2000-03-04  0.824529  0.591027 -1.786807  1.384207
    2000-03-05 -0.103306 -1.431728 -0.077431 -0.126732
    2000-03-06  0.755524  1.460424 -1.109814 -0.568003
    2000-03-07 -1.508068 -0.370230  0.008641  1.275203
    2000-03-08 -0.867791 -0.276403 -0.550362 -0.378691
    2000-03-09 -2.506244  0.430844 -0.074127 -0.759110


### Group + Apply


```python
dates = pd.date_range('1/10/2000', periods=60)
df = pd.DataFrame(np.random.randn(60, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])

grouped = df.groupby(pd.Grouper(freq='1M'))
sr = grouped.apply(lambda x: sum(x['B']))
display(sr)
```


    2000-01-31    2.748909
    2000-02-29   -4.618390
    2000-03-31   -0.301911
    Freq: M, dtype: float64



```python
sr.index = sr.index.map(lambda x: str(x)[:7])
display(sr)
```


    2000-01    2.748909
    2000-02   -4.618390
    2000-03   -0.301911
    dtype: float64


# Missing Data

https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html

- pd.NaT
- np.nan
- isna()
- fillna()

# Performance 

http://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html

pandas is fast. Many of the low-level algorithmic bits have been extensively tweaked in Cython code. However, as with anything else generalization usually sacrifices performance. So if you focus on one feature for your application you may be able to create a faster specialized tool.

## Time

### Dependencies

https://pandas.pydata.org/pandas-docs/stable/install.html#recommended-dependencies

- numexpr
- bottlenect


### Use Wisely

https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6

- Avoid loops; they’re slow and, in most common use cases, unnecessary.
- If you must loop, use `.apply()`, not iteration functions. 
- Vectorization is usually better than scalar operations. Most common operations in Pandas can be vectorized.
- **Vector operations on NumPy arrays are more efficient than on native Pandas series.**

https://realpython.com/fast-flexible-pandas/

1. **Use vectorized operations: Pandas methods and functions with no for-loops.**
2. **Use the `.apply()` method with a callable.**
3. **Use `.itertuples()`: iterate over DataFrame rows as namedtuples from Python’s collections module.**
4. **Use `.iterrows()`: iterate over DataFrame rows as (index, pd.Series) pairs.** While a Pandas Series is a flexible data structure, it can be costly to construct each row into a Series and then access it.
5. Use “element-by-element” for loops, updating each cell or row one at a time with `df.loc` or `df.iloc`. (Or, `.at`/`.iat` for fast scalar access.)

---

1. Try to use vectorized operations where possible rather than approaching problems with the `for x in df`... mentality. If your code is home to a lot of for-loops, it might be better suited to working with native Python data structures, because Pandas otherwise comes with a lot of overhead.
2. If you have more complex operations where vectorization is simply impossible or too difficult to work out efficiently, use the `.apply()` method.
3. If you do have to loop over your array (which does happen), use `.iterrows()` or `.itertuples()` to improve speed and syntax.
4. **Pandas has a lot of optionality**, and there are almost always several ways to get from A to B. Be mindful of this, compare how different routes perform, and choose the one that works best in the context of your project.
5. Once you’ve got a data cleaning script built, avoid reprocessing by storing your intermediate results with HDFStore.
6. Integrating NumPy into Pandas operations can often improve speed and simplify syntax.

https://www.dataquest.io/blog/pandas-big-data/

1. **Downcasting numeric columns to more efficient types**.
2. **Converting string columns to the categorical type**.

### Parallelize

http://blog.adeel.io/2016/11/06/parallelize-pandas-map-or-apply/

### Cython / Numba / pandas.eval()

https://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html

## Space

https://towardsdatascience.com/why-and-how-to-use-pandas-with-large-data-9594dda2ea4c

1. chunking
2. drop useless columns


```python

```
