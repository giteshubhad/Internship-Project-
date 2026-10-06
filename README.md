# E-Commerce Sales and Customer Behavior Analysis using Python

**Internship:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares  
**Project Type:** Data Analytics using Python

## Project Description
This project analyses e-commerce transaction data to identify sales trends, profitable products, customer behaviour, regional performance, and key business KPIs. The workflow covers data loading, inspection, validation, aggregation, trend analysis and visualisation.

## Dataset
The project uses the supplied e-commerce dataset containing **300 orders and 14 columns**. The main fields include order information, customer ID, category, product, region, customer segment, quantity, unit price, discount, sales, cost, profit and payment method.

**Dataset file:** [ecommerce_sales_data.csv](ecommerce_sales_data.csv)

> Note: The dataset is provided as a separate supporting file so the notebook can run without modification.

## Technologies Used
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- CSV

## Project Analysis
1. Data loading and inspection
2. Missing-value and duplicate checking
3. Data type conversion and validation
4. Sales, profit, order and quantity KPIs
5. Product-wise sales analysis
6. Category-wise performance
7. Region-wise performance
8. Customer-segment analysis
9. Monthly sales trend
10. Top customer identification
11. Discount versus profit analysis
12. Business insights and conclusion

## Key Results
- Total Sales: **₹8,285,755.55**
- Total Profit: **₹2,305,833.95**
- Total Orders: **300**
- Total Quantity: **759**
- Average Order Value: **₹27,619.19**
- Highest-sales product: **Laptop**
- Highest-sales region: **Nagpur**
- Highest-profit category: **Electronics**

## Project Files
### Required internship submission files
- **`Gitesh_ECommerce_Sales_Analysis.ipynb`** — complete project code in Jupyter Notebook format.
- **`requirements.txt`** — Python dependencies required to run the project.
- **`Gitesh_ECommerce_Sales_Analysis_ProjectReport.docx`** — complete project documentation in Microsoft Word format.
- **`README.md`** — project overview, dataset link, technologies, setup/run instructions and key information.

### Supporting dataset
- **`ecommerce_sales_data.csv`** — dataset used by the notebook. Keep it in the same folder as the notebook.

## Setup and Run Instructions
### Option 1: Jupyter Notebook / JupyterLab
1. Install Python 3.x.
2. Put the notebook and `ecommerce_sales_data.csv` in the same folder.
3. Open a terminal in that folder.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start Jupyter:

```bash
jupyter notebook
```

6. Open `Gitesh_ECommerce_Sales_Analysis.ipynb` and run all cells.

### Option 2: Google Colab
Upload the notebook and dataset to Colab, then upload `ecommerce_sales_data.csv` to the Colab session before running the notebook.

## Expected Output
The notebook displays:
- dataset inspection and validation results
- KPI table
- product, category, region and segment summaries
- monthly sales trend
- top-customer table
- discount-versus-profit scatter plot
- key business findings

## Future Scope
The project can be extended with SQL database integration, an interactive Power BI dashboard, customer segmentation, sales forecasting, machine learning models, and automated business reporting.
