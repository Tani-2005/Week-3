# Sales Analysis Output

## First 5 Rows of Dataset

```text
         Date     Product  ...  Region  Total_Sales
0  2024-01-01       Phone  ...    East       261100
1  2024-01-02  Headphones  ...   North        61624
2  2024-01-03       Phone  ...    West        43492
3  2024-01-04  Headphones  ...    East        30895
4  2024-01-05      Laptop  ...   North       318680

[5 rows x 7 columns]

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         100 non-null    object
 1   Product      100 non-null    object
 2   Quantity     100 non-null    int64
 3   Price        100 non-null    int64
 4   Customer_ID  100 non-null    object
 5   Region       100 non-null    object
 6   Total_Sales  100 non-null    int64
dtypes: int64(3), object(4)
memory usage: 5.6+ KB
None


Date           0
Product        0
Quantity       0
Price          0
Customer_ID    0
Region         0
Total_Sales    0
dtype: int64

Total Sales: ₹12,365,048.00
Average Sales: ₹123,650.48
Highest Single Sale: ₹373,932.00
Lowest Single Sale: ₹6,540.00
Best Selling Product: Laptop

Analysis completed successfully!
