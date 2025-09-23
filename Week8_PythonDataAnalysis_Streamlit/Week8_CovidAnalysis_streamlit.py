# In this code per the assignment requirements, 
# we'll use the covid 19 metadata dataset from Kaggle 
# to conduct a basic data analysis using streamlit 
#
#
# We'll embed the data engineering part in a function named load_data()
# by loading the csv file that we host on our D: partition
# As we are conducting a historical research over time we'll make sure
# the column related to publish_time is well parsed and both publish_time and title columns are not empty
# 
# Six (6) sections are in our research
#
# 1. The first section is related to the number of publications over time (year) 
# Through a slider, the user can adjust the range of period and view the evolution 
# with a bart chart. Here we can notice there have been a lot of publication from 2020 to 2022
#
# 2. The second section is related to the top 10 journals that have published COvid-19 reserachs
# We made that using horizontal bar charts
#
# 3. In the third section we allow the user to track the evolution of a keyword over the period
# in the papers.
# That led us to understand how was effectively adressed subjects using that word
#
# 4. In the fourth section we provide a top classement of Authors to point out the top 
# authors that have written publications in that period of time
#
# 5. The fifth section was related to a word cloud that showcase the words most used in all the 
# published papers. Here it'is demonstrated that it related to SARS Cov's effect and impact on patient
# 
# 6. The last section shows a distribution of words number in abstracts. It clearly demonstrate that
# abstract never exceeds 1000 words.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 Research Explorer", layout="wide")
sns.set_style("whitegrid")

@st.cache_data
def load_data():
    # Load dataset and preprocess
    df = pd.read_csv(r'D:\covid_metadata\metadata.csv')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df_clean = df.dropna(subset=['title', 'publish_time'])
    df_clean['year'] = df_clean['publish_time'].dt.year
    df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(str(x).split()))
    return df_clean

df_clean = load_data()

st.title("CORD-19 Research Explorer")
st.write("Explore COVID-19 research metadata with interactive visualizations.")

# Publications per Year section with year range filter
st.header("Publications per Year")

min_year = int(df_clean['year'].min())
max_year = int(df_clean['year'].max())
selected_year_range = st.slider("Select publication year range", min_year, max_year, (min_year, max_year))

# Filter data by year range
filtered_df = df_clean[(df_clean['year'] >= selected_year_range[0]) & (df_clean['year'] <= selected_year_range[1])]

year_counts = filtered_df['year'].value_counts().sort_index()

fig_year, ax_year = plt.subplots(figsize=(10, 5))
sns.barplot(x=year_counts.index, y=year_counts.values, color='skyblue', ax=ax_year)
ax_year.set_title("Publications by Year")
ax_year.set_xlabel("Year")
ax_year.set_ylabel("Number of Publications")
st.pyplot(fig_year)

# Top 10 Journals section
st.header("Top 10 Journals Publishing COVID-19 Research")

top_journals = filtered_df['journal'].value_counts().head(10)

fig_journals, ax_journals = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax_journals)
ax_journals.set_title("Top 10 Journals Publishing COVID-19 Research")
ax_journals.set_xlabel("Number of Publications")
ax_journals.set_ylabel("Journal")
st.pyplot(fig_journals)

# Interactive keyword trend over time
st.header("Keyword Trend Over Time")
keyword_input = st.text_input("Enter keyword to explore its trend over time", "vaccine")

def keyword_trend(df, kw):
    text_data = (df['title'].fillna('') + ' ' + df['abstract'].fillna('')).str.lower()
    filtered = df[text_data.str.contains(kw.lower())]
    trend = filtered.groupby('year').size()
    return trend

if keyword_input.strip():
    trend = keyword_trend(df_clean, keyword_input.strip())
    if not trend.empty:
        fig, ax = plt.subplots()
        sns.lineplot(x=trend.index, y=trend.values, marker='o', ax=ax)
        ax.set_title(f"Number of Papers Containing '{keyword_input}' by Year")
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.write(f"No papers found containing '{keyword_input}'.")

# Top authors by publication count
st.header("Top Authors by Publication Count")
top_n_authors = st.slider("Number of top authors to display", 5, 30, 10)

authors_series = (
    df_clean['authors']
    .dropna()
    .str.split(';')
    .explode()
    .str.strip()
    .value_counts()
)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=authors_series.head(top_n_authors).values, y=authors_series.head(top_n_authors).index, palette='coolwarm', ax=ax2)
ax2.set_xlabel("Number of Publications")
ax2.set_ylabel("Author")
ax2.set_title(f"Top {top_n_authors} Authors")
st.pyplot(fig2)

# Word cloud of paper titles
st.header("Word Cloud of Paper Titles")

words_to_exclude = set(WordCloud().stopwords).union({"covid", "covid-19", "sars-cov-2", "coronavirus", "pandemic"})
text = " ".join(df_clean['title'].dropna().tolist()).lower()

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=words_to_exclude,
    max_words=100,
    colormap='viridis'
).generate(text)

fig3, ax3 = plt.subplots(figsize=(14, 7))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
ax3.set_title("Most Common Words in Paper Titles (Excluding Common COVID Terms)")
st.pyplot(fig3)

# Abstract length distribution histogram
st.header("Abstract Length Distribution")

fig4, ax4 = plt.subplots()
sns.histplot(df_clean['abstract_word_count'], bins=50, kde=True, color='purple', ax=ax4)
ax4.set_xlabel("Number of Words in Abstract")
ax4.set_ylabel("Frequency")
ax4.set_title("Distribution of Abstract Lengths")
st.pyplot(fig4)

# Show sample data table
if st.checkbox("Show sample data"):
    st.subheader("Sample Data")
    st.dataframe(df_clean[['title', 'authors', 'journal', 'year', 'abstract_word_count']].sample(10))

# End message
st.write("Data powered by CORD-19 metadata dataset.")
