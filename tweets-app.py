import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Twitter Sentiment Analysis", layout="centered")

# Title of the app
st.title("✈️ Twitter Sentiment Analysis for Airlines")

# Load the data
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/Prathyushabuduru/BP-tweets/refs/heads/main/Tweets.csv'
    df = pd.read_csv(url)
    return df

tweets = load_data()

# Show the first few rows of the data
st.subheader("📄 Sample of Tweet Data")
st.dataframe(tweets.head())

# Pie chart of sentiment counts
st.subheader("📊 Tweet Sentiment Distribution")

sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['airline_sentiment', 'count']

fig_pie = px.pie(
    sentiment_counts,
    values='count',
    names='airline_sentiment',
    title='Count of Tweets by Sentiment',
    hole=0.3
)
st.plotly_chart(fig_pie)

# Bar plot of tweet counts by airline
st.subheader("📉 Number of Tweets by Airline")

airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

fig_bar, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue='airline', data=airline_counts, palette='pastel', legend=False, ax=ax)
ax.set_title('Count of Tweets by Airlines')
ax.set_xlabel('Airline')
ax.set_ylabel('Count')
st.pyplot(fig_bar)




