import emoji
from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd

def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df['Users'] == selected_user]
    # fetches no. of msg's
    num_msg = df.shape[0]

    # fetches no. of words
    words = []
    for word in df['Messages']:
       words.extend(word.split())

    # fetches no. of media shared

    num_media = df[df['Messages'] == '<Media omitted>'].shape[0]

    # fetches no. of links shared

    extract = URLExtract()
    links = []
    for link in df["Messages"]:
        links.extend(extract.find_urls(link))

    return num_msg,len(words),num_media,len(links)

def most_busy_users(df):
    x = df["Users"].value_counts().head()
    y = round((df["Users"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'Name','Users':'Percent Contribute'})
    return x,y

def word_cloud(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    text = " ".join(df['Messages'].dropna().astype(str))
    wc = WordCloud(width = 1000 , height=500,min_font_size=10,background_color='#22273a',colormap='summer',prefer_horizontal=1.0, contour_color='white',contour_width=0).generate(text)

    return wc

def most_common_words(selected_user,df):
    if selected_user != "Overall":
        df = df[df['Users'] == selected_user]
    temp = df[df['Messages'] != "<Media omitted>"]
    temp = temp[temp["Messages"] != '<this edited>/n']
    with open ('stop_hinglish.txt','r') as f:
        stop_words = f.read()
    words = []
    for i in temp['Messages']:
        for word in i.lower().split():
            if word not in stop_words:
              words.append(word)
    most_common_words_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_words_df

def emoji_counter(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    emojis = []
    for msg in df["Messages"]:
        emojis.extend([c for c in msg if emoji.is_emoji(c)])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(20))
    return emoji_df











