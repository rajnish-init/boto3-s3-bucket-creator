# 🚀 Boto3 S3 Bucket Creator

This Python script uses **Boto3**, the AWS SDK for Python, to **create an S3 bucket** and **upload a file to it** in a specific region (`ap-south-1` - Mumbai). This project showcases a real-world use of Python to interact with AWS services programmatically.

---

## 🧰 Technologies Used

- **Python 3**
- **Boto3** (AWS SDK for Python)
- **AWS CLI** (for setting up credentials)

---

## 📁 Features

- Creates an S3 bucket with custom region configuration
- Gracefully handles if bucket already exists
- Uploads a local file to a folder path inside the bucket
- Uses `LocationConstraint` for region-specific bucket creation

---

## 📝 Why `LocationConstraint` is used?

When creating an S3 bucket **outside of the default AWS region (`us-east-1`)**, you **must specify the `LocationConstraint`**.

Since in this script we are creating the bucket in **`ap-south-1` (Mumbai)**, the `CreateBucketConfiguration` must explicitly mention:

```python
CreateBucketConfiguration={'LocationConstraint': region}

If this is not provided, AWS will throw an error saying "Invalid LocationConstraint" or will try to create the bucket in us-east-1.

