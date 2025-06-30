import re
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer


def preprocess(data):
    pattern = (r'(\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\u202fPM)\s-\s(.*?):\s(.*)')
    matches = re.findall(pattern, data)
    dates = [str(match[0]).replace('\u202f', ' ') for match in matches]
    users = [match[1] for match in matches]
    messages = [match[2] for match in matches]
    df = pd.DataFrame({"Date": dates, "Users": users, "Messages": messages})
    df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%y, %I:%M %p", errors="coerce")


    df['Month'] = df['Date'].dt.month
    df["Month_name"] = df["Date"].dt.month_name()
    df['Year'] = df['Date'].dt.year
    df['Day'] = df['Date'].dt.day_name()
    df['date'] = df['Date'].dt.day
    df["Hour"] = df["Date"].dt.strftime('%I').astype(int)
    df["Minute"] = df["Date"].dt.minute
    df['AM_PM'] = df['Date'].dt.strftime('%p')
    # df['Date'] = df['Date'].dt.strftime('%m/%d/%Y, %I:%M %p')


    def get_sentiment_score(message):
        sentiments = SentimentIntensityAnalyzer()
        return sentiments.polarity_scores(message)['compound']

    df['Sentiment'] = df['Messages'].apply(get_sentiment_score)

    def polarity(score):
        if score >= 0.05:
            return 'positive'
        elif score <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    df['Sentiment_label'] = df['Sentiment'].apply(polarity)



    return df
