# 🌍 World Happiness Report 2019 - AI-Assisted Exploratory Data Analysis

## 📌 Project Overview

This project analyzes the **World Happiness Report 2019** dataset using **Python, Pandas, Seaborn, Matplotlib, and Sweetviz**.

The objective was to explore the factors that influence national happiness and demonstrate an AI-assisted data analysis workflow, including:

* Data exploration
* Data cleaning
* Outlier detection
* Correlation analysis
* Visualizations
* Insight generation
* AI usage documentation

---

## 📊 Dataset Information

* Dataset: World Happiness Report 2019
* Rows: 156
* Columns: 9

### Features

| Column                       |
| ---------------------------- |
| Overall Rank                 |
| Country or Region            |
| Score                        |
| GDP per Capita               |
| Social Support               |
| Healthy Life Expectancy      |
| Freedom to Make Life Choices |
| Generosity                   |
| Perceptions of Corruption    |

---

## 🛠 Tools & Libraries Used

* Python
* Pandas
* Seaborn
* Matplotlib
* Sweetviz

---

## 🧹 Data Cleaning Performed

The dataset was already very clean.

### Cleaning Steps

1. Standardized column names
2. Trimmed text fields
3. Checked for outliers using the IQR method

### Results

* No missing values found
* No duplicate records found
* Data types were already appropriate

---

## 🔍 Analysis Questions

### Question 1

Which countries have a happiness score above the global average?

### Question 2

Which countries have both GDP per capita and healthy life expectancy above the global average?

### Question 3

How do the top 10 happiest countries differ from the bottom 10 countries in:

* GDP per capita
* Healthy life expectancy
* Freedom to make life choices
* Social support

---

## 📈 Visualizations

### 1. Relationship Between Happiness and GDP

Scatter plot showing the relationship between GDP per capita and happiness score.

### 2. Relationship Between Healthy Life Expectancy and GDP

Scatter plot showing how health and economic prosperity are connected.

### 3. Correlation Heatmap

Heatmap displaying correlations among all numerical variables.

---

## 📋 Key Findings

### Average Happiness Score

* Global average happiness score: **5.407**

### Correlation with Happiness Score

| Factor                       | Correlation |
| ---------------------------- | ----------: |
| GDP per Capita               |       0.794 |
| Healthy Life Expectancy      |       0.780 |
| Social Support               |       0.777 |
| Freedom to Make Life Choices |       0.567 |
| Perceptions of Corruption    |       0.386 |
| Generosity                   |       0.076 |

### Top 10 vs Bottom 10 Countries

| Factor                       | Top 10 Avg | Bottom 10 Avg |
| ---------------------------- | ---------: | ------------: |
| GDP per Capita               |      1.387 |         0.398 |
| Healthy Life Expectancy      |      1.018 |         0.426 |
| Freedom to Make Life Choices |      0.579 |         0.229 |
| Social Support               |      1.544 |         0.662 |

### Conclusion

The analysis indicates that:

* GDP per capita is strongly associated with happiness.
* Healthy life expectancy is a major contributor to happiness.
* Social support systems play a critical role in national well-being.
* Freedom to make life choices is significantly higher in happier countries.

Countries with stronger economic conditions, healthier populations, and better social support networks tend to report substantially higher happiness scores.

---

## 🤖 AI-Assisted Workflow

AI was used to:

* Review dataset quality
* Suggest cleaning strategies
* Generate reusable analysis functions
* Create visualization code
* Draft findings summaries

All AI-generated suggestions were reviewed, executed, and verified against actual dataset results before inclusion.

---

## 📂 Project Structure

```text
├── Happiness.csv
├── Week_4_Final_Project.py
├── happiness_sweetviz.html
├── Relation_between_happiness_and_GDP.png
├── Relation_between_Healthy_life_expectancy_and_GDP.png
├── Correlation_between_columns.png
├── README.md
```

---

## 👨‍💻 Author

**Ankit Tiwari**

AI-Assisted Exploratory Data Analysis Portfolio Project

2026
