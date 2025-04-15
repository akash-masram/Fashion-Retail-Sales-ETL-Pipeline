# 🛍️ Fashion Retail Sales ETL Pipeline (AWS + PySpark)

This project demonstrates an end-to-end ETL pipeline using AWS Glue and PySpark. It processes raw fashion retail sales data stored in an AWS S3 bucket, transforms and cleans the data, and writes the processed output to another S3 location — ready for analytics and reporting.



## 📁 Project Structure

```
fashion-retail-sales-etl/ 
│ 
├── glue_jobs/ 
│ └── fashion_sales_etl.py # PySpark script for AWS Glue job 
│ 
├── iam/ 
│ └── glue_s3_access_policy.json # IAM policy to allow Glue to access S3 
│ 
├── sample_data/ 
│ └── Fashion_Retail_Sales.csv # Sample dataset (optional) 
│ ├── screenshots/ # Optional: AWS Glue Job, S3 structure screenshots 
│ └── README.md # Project documentation

```

## 📌 Problem Statement

Retail companies deal with large volumes of sales data stored in the cloud. This project automates the process of:

- Extracting raw sales data from S3  
- Cleaning and transforming the data using PySpark  
- Writing the processed data back to S3 for analytics use  


## 🛠️ Technologies Used
```
- AWS Glue  
- AWS S3  
- AWS IAM  
- AWS CloudWatch  
- PySpark  

```

## 📊 Dataset
**Source :** [Kaggle Dataset — Fashion Retail Sales](https://www.kaggle.com/datasets/atharvasoundankar/fashion-retail-sales)
**Name:** `Fashion_Retail_Sales.csv`  
**Stored at:** `s3://<your-s3-bucket-name>/raw/Fashion_Retail_Sales.csv`  

**Sample Columns:**
- Purchase Amount (USD)
- Review Rating
- Product Category  
- ...and more



## ⚙️ ETL Process

### 🔹 Extract
Read the CSV file from the raw S3 bucket.

### 🔹 Transform
- Convert `Purchase Amount (USD)` and `Review Rating` columns to numeric types.
- Fill missing `Review Rating` values with the average rating.
- Filter records where `Purchase Amount (USD)` > 3000.

### 🔹 Load
Write cleaned and filtered data to the processed S3 location:  
`s3://<your-s3-bucket-name>/processed/`


## 🚀 How to Deploy

### 1. Upload Dataset
Upload `Fashion_Retail_Sales.csv` to the S3 path:  
`s3://<your-s3-bucket-name>/raw/`

### 2. Create IAM Role
Create a role with permissions to access your S3 paths and attach it to your AWS Glue job.  
Use the `glue_s3_access_policy.json` file and **replace bucket names** with your actual S3 bucket.

### 3. Create and Run Glue Job
- Use AWS Glue Studio or the AWS Console
- Choose script mode
- Upload or paste the PySpark script
- Assign the IAM role
- Trigger the job
- Monitor progress via AWS Glue or CloudWatch

---
### 4. View Output
Check `s3://<your-s3-bucket-name>/processed/` for the transformed results.

---

## 📜 License

**MIT License** — Free to use and customize.

---

## 🙌 Acknowledgments

Thanks to the **AWS Free Tier** and community tutorials for helping build and test this project.
