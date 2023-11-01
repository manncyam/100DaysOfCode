# Day72 Data Exploration with Pandas

Goal: To Answer the questions below:

1. Which degrees have the highest starting salaries?
2. Which majors have the lowest earnings after college?
3. Which degrees have the highest earning potential?
4. What are the lowest risk college majors from an earnings standpoint?
5. Do business, STEM (Science, Technology, Engineering, Mathematics) or HASS (Humanities, Arts, Social Science) degrees earn more on average?

## First Look at data

```python
import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
df.head()
```

or use command below to generate markdown table

```python
df.head().to_markdown()
```

|      | Undergraduate Major   | Starting Median Salary | Mid-Career Median Salary | Mid-Career 10th Percentile Salary | Mid-Career 90th Percentile Salary | Group    |
| ---: | :-------------------- | ---------------------: | -----------------------: | --------------------------------: | --------------------------------: | :------- |
|    0 | Accounting            |                  46000 |                    77100 |                             42200 |                            152000 | Business |
|    1 | Aerospace Engineering |                  57700 |                   101000 |                             64300 |                            161000 | STEM     |
|    2 | Agriculture           |                  42600 |                    71900 |                             36300 |                            150000 | Business |
|    3 | Anthropology          |                  36800 |                    61500 |                             33800 |                            138000 | HASS     |
|    4 | Architecture          |                  41600 |                    76800 |                             50600 |                            136000 | Business |

Questions to ask to get to know more about dataset:

1. How many rows does our dataframe have?
   
   ```python
   df.rows ?
   df.count ?
   df.rows.count
   ``` 