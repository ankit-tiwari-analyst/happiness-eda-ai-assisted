
# 📝 Lesson 4 Assignment — your second portfolio piece, AI-assisted

# Phase 1 — Load & overview Dataset

import pandas as pd
import sweetviz as sv

df = pd.read_csv('Happiness.csv')

df.shape
df.head(3)
df.info()
df.describe()
df.isnull().sum()
df.columns.tolist()


# Stage 1: Run a sweetviz report. Note 2-3 things it flags.

report = sv.analyze(df)
report.show_html('happiness_sweetviz.html')

print('''Note: 1. "GDP and Happiness are correlated 0.79, suggesting wealth is one of the 
strongest predictors of national happiness — but I should check if this holds within regions too, 
since correlation alone doesn't separate cause from effect."''')

print('''Note: 2. "Healthy life expectancy and GDP per capita are correlated 0.84, suggesting healthy is one of the strongest
predictors of GDP per capita - because when people are healthy they more productive which increase GDP."''')

print('''Note: 3. Freedom to make life choices of Score are correlated 0.57, suggesting Freedom to make life choices is one of the strong
predictors of Score - beause when people free to take there own decesion they happiness score increase.''')


# Stage 2: Use the AI cleaning-plan prompt. Document your decisions in the AI Usage Log format from Part 3.

# 1. Standardize column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(' ', '_')
)

# 2. Trim text fields
df['country_or_region'] = (
    df['country_or_region']
      .str.strip()
)

# 3. Check outliers
def outlier_count_iqr(df, column):

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return df[
        (df[column] < lower) |
        (df[column] > upper)
    ].shape[0]

numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    print(f"{col}: {outlier_count_iqr(df, col)} outliers")


print('# AI USAGE LOG')
print('='*50)
print('Data Cleaning')
print('Prompt used: "this is 2019 happiness report which have 9 columns and 156 rows i want you to analyze dataset and apply data cleaning step on it ."')
print('✅ No missing values found.')
print('✅ No duplicate rows found.')
print('✅ Data types are already appropriate.')
print('AI suggested: "This dataset is already very clean. The main cleaning tasks are standardizing column names, trimming text fields, validating data types, and checking for outliers before performing exploratory data analysis (EDA)."')
print('My decision: "i chose to standardizing column name, trimming text fields, checking for outliers because which make data more readable and professional')
print(' Verified: "i already got a overview of data which help me to take decision"')
print('='*50)


# Stage 3: Pick 3 analysis questions about your dataset. For each, write an RTCF prompt, get AI's code, verify it runs and makes sense, and log it.

# Q1. list of country which score is greater then Avarage score.

# Calculate average score
avg_score = df['score'].mean()

# Countries with score greater than average
above_avg = df[df['score'] > avg_score][['country_or_region', 'score']]

print("Average Score:", round(avg_score, 2))
print("\nCountries with Score greater than Average:")
print(above_avg)


# Q2. List of country which GDP per capital and Healthy life expectancy is greater then avarage.

# Calculate averages
avg_gdp = df['gdp_per_capita'].mean()
avg_health = df['healthy_life_expectancy'].mean()

# Filter countries
result = df[
    (df['gdp_per_capita'] > avg_gdp) &
    (df['healthy_life_expectancy'] > avg_health)
][['country_or_region', 'gdp_per_capita', 'healthy_life_expectancy']]

print("Average GDP per Capita:", round(avg_gdp, 3))
print("Average Healthy Life Expectancy:", round(avg_health, 3))

print("\nCountries above average in both GDP per Capita and Healthy Life Expectancy:")
print(result)


'''Q3. you are a senior Data Analyst. How do the top 10 countries differ from the bottom 10 in GDP, health, freedom, and social support?
i'm working with happiness dataset in pandas and i'm a beginner who understand grouping, filtering. Format your answer as: the function code, followed by
a 2-sentence explanation of how to use it.'''

def compare_top_bottom_10(df):
    """
    Compare the average GDP, health, freedom, and social support
    between the top 10 and bottom 10 countries by happiness score.
    """

    top_10 = df.nlargest(10, 'score')
    bottom_10 = df.nsmallest(10, 'score')

    comparison = pd.DataFrame({
        'Top 10 Avg': [
            top_10['gdp_per_capita'].mean(),
            top_10['healthy_life_expectancy'].mean(),
            top_10['freedom_to_make_life_choices'].mean(),
            top_10['social_support'].mean()
        ],
        'Bottom 10 Avg': [
            bottom_10['gdp_per_capita'].mean(),
            bottom_10['healthy_life_expectancy'].mean(),
            bottom_10['freedom_to_make_life_choices'].mean(),
            bottom_10['social_support'].mean()
        ]
    },
    index=[
        'GDP per Capita',
        'Healthy Life Expectancy',
        'Freedom to Make Life Choices',
        'Social Support'
    ])

    return comparison.round(3)


# Example usage
result = compare_top_bottom_10(df)
print(result)

print('# AI USAGE LOG')
print('='*50)
print('analysis questions')
print('Prompt used: " you are a senior Data Analyst. How do the top 10 countries differ from the bottom 10 in GDP, health, freedom, and social support? im working with happiness dataset in pandas and im a beginner who understand grouping, filtering. Format your answer as: the function code, followed by a 2-sentence explanation of how to use it."')
print('AI suggested: "This function splits the dataset into the 10 happiest and 10 least happy countries based on the score column, then calculates the average GDP per capita, healthy life expectancy, freedom, and social support for each group. Run the function on your DataFrame and compare the averages to see which factors most distinguish the happiest countries from the least happy ones."')
print('My decision: "I compared the top 10 and bottom 10 countries by happiness score to identify the factors that most distinguish highly happy countries from less happy ones. This helps reveal whether GDP, health, freedom, and social support are associated with higher levels of happiness and provides actionable insights from the dataset."')
print(' Verified: "i already got a overview of data which help me to take decision"')
print('='*50)


# Stage 4: Generate 2-3 charts using specific (not vague) prompts. Save as PNG.

# prompt 1. using pandas and seaborn, create Scatterplot chart show the relation between happiness score and GDP, titled 'Relation_between_happiness_and_GDP', SAVE as PNG with dpi=150.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Sort by GDP for better visualization
df = df.sort_values('gdp_per_capita', ascending=False)

# Create figure
plt.figure(figsize=(12, 6))

# scatterplot chart
sns.scatterplot(
    data=df,
    x='gdp_per_capita',
    y='score'
)

# Title and labels
plt.title('Relationship Between Happiness and GDP')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')

# Save chart
plt.savefig(
    'Relation_between_happiness_and_GDP.png',
    dpi=150,
    bbox_inches='tight'
)

plt.show()

# prompt 2. using pandas and seaborn, create Scatterplot chart show the relation between Healthy life expectancy and GDP, titled 'Relation_between_Healthy_life_expectancy_and_GDP', SAVE as PNG with dpi=150.


# Create figure
plt.figure(figsize=(10, 6))

# Scatter plot
sns.scatterplot(
    data=df,
    x='gdp_per_capita',
    y='healthy_life_expectancy'
)

# Add title and labels
plt.title('Relationship between Healthy life expectancy and GDP')
plt.xlabel('GDP per Capita')
plt.ylabel('Healthy Life Expectancy')

# Save chart as PNG
plt.savefig(
    'Relation_between_Healthy_life_expectancy_and_GDP.png',
    dpi=150,
    bbox_inches='tight'
)

# Display chart
plt.show()

# prompt 3. using pandas and seaborn, create heatmap chart showing correlation between all columns, titled 'Correlation_between_columns', save as PNG WITH 150 dpi.


# Select numeric columns and calculate correlation matrix
corr_matrix = df.corr(numeric_only=True)

# Create figure
plt.figure(figsize=(10, 8))

# Heatmap
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=0.5
)

# Title
plt.title('Relationship between columns')

# Save chart as PNG
plt.savefig(
    'Correlation_between_columns.png',
    dpi=150,
    bbox_inches='tight'
)

# Display chart
plt.show()


# Stage 5: Write a findings summary in your own words (like Week 2's conclusions) — AI can help draft it, but the final insights must be verified by you against the actual numbers.

print('''1. Average Happiness Score
    The average happiness score across all 156 countries is 5.407.''')

print('''2. Strongest Factors Related to Happiness
    Based on the correlation analysis:

Factor	Correlation with Happiness Score
GDP per Capita ,0.794
Healthy Life Expectancy	,0.780
Social Support	,0.777
Freedom to Make Life Choices	,0.567
Perceptions of Corruption	,0.386
Generosity	,0.076

Key Insight: GDP per Capita, Healthy Life Expectancy, and Social Support have the strongest 
positive relationships with happiness.''')

print('''3. Top 10 vs Bottom 10 Countries
Factor	,Top 10 Avg	,Bottom 10 Avg
GDP per Capita	,1.387	,0.398
Healthy Life Expectancy	,1.018	,0.426
Freedom to Make Life Choices	,0.579	,0.229
Social Support	,1.544	,0.662

Key Differences
The happiest countries have a GDP per Capita of 1.387, compared to only 0.398 for the least happy countries.
The happiest countries have a Healthy Life Expectancy score of 1.018, more than double the 0.426 observed in the least happy countries.
Social Support is 1.544 among the happiest countries versus 0.662 among the least happy countries.
Freedom to Make Life Choices is 0.579 in the top 10 countries and only 0.229 in the bottom 10 countries.''')

print('''Overall Conclusion

The analysis suggests that economic prosperity (GDP), good health, and strong social support systems 
are the most important factors associated with higher happiness levels. Countries with higher GDP per Capita, better Healthy Life Expectancy, 
greater Freedom, and stronger Social Support consistently achieve much higher Happiness Scores than countries lacking these characteristics.''')



