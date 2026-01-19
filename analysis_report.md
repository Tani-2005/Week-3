# Sales Data Analysis Report

## Dataset Overview
The sales dataset contains 100 records and 7 columns, representing sales transactions across different dates, products, customers, and regions. The data was analyzed using Python and the pandas library.

---

## Dataset Structure

**Total Rows:** 100  
**Total Columns:** 7  

### Columns Included
- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

### Data Types
- Integer columns: Quantity, Price, Total_Sales  
- Object columns: Date, Product, Customer_ID, Region  

---

## Data Quality Check

All columns were checked for missing values.

**Result:**  
No missing values were found in the dataset.  
This indicates that the dataset was clean and did not require missing value handling.

---

## Sales Analysis Results

### Key Metrics
- **Total Sales:** ₹12,365,048.00  
- **Average Sales:** ₹123,650.48  
- **Highest Single Sale:** ₹373,932.00  
- **Lowest Single Sale:** ₹6,540.00  

### Best-Selling Product
- **Laptop**

The best-selling product was identified by grouping sales data by product and calculating total sales for each product.

---

## Summary of Findings
- The dataset is complete with no missing values.
- Sales values vary significantly, indicating a wide range of transaction sizes.
- Laptops generated the highest overall sales among all products.
- The analysis successfully identified key performance metrics using pandas.

---

## Conclusion
This analysis demonstrates how Python and the pandas library can be used to explore, clean, and analyze real-world sales data efficiently. The project helped build practical data analysis skills, including dataset exploration, metric calculation, and insight generation.
