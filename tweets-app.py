import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set up the Streamlit page
st.set_page_config(page_title="Airline Tweets Sentiment Analysis", layout="wide")

# Title
st.title("Airline Tweets Sentiment Analysis")

# Load Data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/Prathyushabuduru/BP-tweets/refs/heads/main/Tweets.csv"
    return pd.read_csv(url)

tweets = load_data()

# Display data
st.subheader("Sample of Tweets Dataset")
st.dataframe(tweets.head())

# Sentiment distribution
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['airline_sentiment', 'count']

st.subheader("Distribution of Tweet Sentiments")
fig1 = px.pie(sentiment_counts, values='count', names='airline_sentiment',
              title='Count of Tweets by Sentiment')
st.plotly_chart(fig1)

# Tweet count by airline
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

st.subheader("Tweet Count by Airline")
fig2, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue='airline', data=airline_counts,
            palette='pastel', ax=ax, legend=False)
ax.set_title('Count of Tweets by Airlines')
ax.set_xlabel('Airline')
ax.set_ylabel('Count')
st.pyplot(fig2)

# Show raw data toggle
with st.expander("View full dataset"):
    st.dataframe(tweets)
