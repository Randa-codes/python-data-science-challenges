# 📂 File Formats Challenge – JSON & CSV

This folder includes two hands-on Python challenges focused on working with **file formats** — a key skill in data science, backend development, and real-world data pipelines.

---

## 💡 Challenge 1: JSON – Dictionary Serialization & Deserialization

We created a Python dictionary, saved it to a `.json` file, and read it back using the built-in `json` module.

### 🔧 Steps:
1. Define a dictionary in Python
2. Serialize (save) it using `json.dump()`
3. Deserialize (load) it using `json.load()`

✅ Example:
```json
{
  "name": "Lisa",
  "Age": 21
}



##💡 Challenge 2: CSV – Product Inventory Analysis with Pandas
We created a product inventory using a pandas DataFrame, saved it to a .csv file, and calculated the total value for each product by multiplying the price and quantity.

###🔧 Steps:
Define a DataFrame with product names, prices, and quantities

Add a new column: Total Value = Prices × Quantities

Save the updated table using df.to_csv()
✅ Example:
Products,Prices,Quantities,Total Value
Laptop,2000,2,4000
Phone,1500,3,4500
TV,5000,1,5000
Coffee Machine,3000,2,6000

>This challenge helped reinforce how to manipulate tabular data and export it for further use in data pipelines and reports
