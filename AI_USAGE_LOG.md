## 🤖 AI Usage Log

This project was completed using an AI-assisted workflow. AI was used as a coding and analysis assistant, while all outputs were manually reviewed and verified before inclusion.

### Task 1: Data Cleaning

**Prompt Used**

> "This is 2019 happiness report which have 9 columns and 156 rows. I want you to analyze dataset and apply data cleaning step on it."

**AI Suggestions**

* Check for missing values
* Check for duplicates
* Validate data types
* Standardize column names
* Trim text fields
* Check for outliers

**My Decision**

I selected the following cleaning steps:

* Standardized column names
* Trimmed text fields
* Checked for outliers using the IQR method

**Verification**

* No missing values found
* No duplicate rows found
* Data types were already appropriate
* Verified the cleaning steps by reviewing the dataset overview and summary statistics

---

### Task 2: Analysis Question

**Prompt Used**

> "How do the top 10 countries differ from the bottom 10 in GDP, health, freedom, and social support?"

**AI Suggestion**

AI generated a reusable function that:

* Selected the top 10 happiest countries
* Selected the bottom 10 least happy countries
* Calculated average GDP, Healthy Life Expectancy, Freedom, and Social Support for both groups

**My Decision**

I used this analysis because it helps identify the factors that distinguish highly happy countries from less happy countries.

**Verification**

I reviewed the output averages and confirmed that the top 10 countries consistently scored higher in GDP, health, freedom, and social support.

---

### Task 3: Data Visualizations

#### Chart 1: Happiness Score vs GDP

**Prompt Used**

> "Create a scatterplot showing the relationship between happiness score and GDP."

**AI Output**

Generated Seaborn scatterplot code.

**Verification**

Confirmed that countries with higher GDP generally had higher happiness scores.

---

#### Chart 2: Healthy Life Expectancy vs GDP

**Prompt Used**

> "Create a scatterplot showing the relationship between healthy life expectancy and GDP."

**AI Output**

Generated Seaborn scatterplot code.

**Verification**

Confirmed a strong positive relationship between GDP and healthy life expectancy.

---

#### Chart 3: Correlation Heatmap

**Prompt Used**

> "Create a heatmap showing correlation between all columns."

**AI Output**

Generated correlation heatmap code using Seaborn.

**Verification**

Verified that GDP per Capita (0.794), Healthy Life Expectancy (0.780), and Social Support (0.777) showed the strongest positive correlations with Happiness Score.

---

### Task 4: Findings Summary

**Prompt Used**

> "Write a findings summary with real numbers."

**AI Output**

Generated a draft findings summary.

**Verification**

All reported values were checked against the dataset outputs before inclusion in the final project report.

---

### Reflection

AI significantly improved productivity by helping generate cleaning plans, reusable analysis functions, visualizations, and draft summaries. However, every recommendation and output was reviewed and validated against the actual dataset to ensure accuracy and understanding.
