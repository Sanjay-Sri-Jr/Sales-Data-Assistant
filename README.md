# 📊 Sales Data Assistant + LLaMA 3.2

**Sales Data Assistant** is an AI-powered chatbot built with Flask that uses Excel data to answer sales-related queries. It combines traditional data analysis (via **Pandas**) with the power of **LLaMA 3.2**, a cutting-edge large language model from Meta, to interpret natural language and provide intelligent responses.

---

## 🚀 Features

- 🧠 **Natural language query handling with LLaMA 3.2**
- 🔍 **Smart querying of sales data from Excel** (`SaleData.xlsx`)
- 📊 **Filter data by region, item, manager, or date**
- 💬 **Sample queries**:
  - “What were the total sales in Electronics?”
  - “What is the highest product sold”
  - “How many binders were sold?”
- 🌐 **Flask-based chat interface**

---

## 🤖 LLaMA 3.2 Integration

LLaMA 3.2 is used to:
- Interpret complex user queries
- Extract intent (e.g., date filters, item names, comparisons)
- Generate contextual, human-like responses


---

## 🧰 Tech Stack

- **Python** 🐍  
- **Flask** 🌐  
- **Pandas** 📊  
- **LLaMA 3.2** (via **[API/Local Hosting]**) 🧠  
- **HTML, JavaScript, CSS** for the frontend  

---

## 📁 Data Format

Ensure your Excel file (`SaleData.xlsx`) contains relevant columns like `Region`, `Item`, `Manager`, `Date`, `Sales`, etc. to allow accurate querying.

---

