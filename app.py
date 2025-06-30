import streamlit as st
from streamlit import sidebar
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd






import helper
import preprocessor

st.set_page_config(
    page_title="LEXIQ - WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Combined CSS styles
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom fonts and colors */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a1d29 0%, #2c3245 100%);
        color: #ffffff;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1a1d29;
    }

    /* Landing page styles */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 5%;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    .logo {
        font-size: 28px;
        font-weight: 800;
        color: #6366f1;
        letter-spacing: -0.5px;
    }

    .nav-menu {
        display: flex;
        gap: 40px;
        align-items: center;
    }

    .nav-item {
        color: #ffffff;
        font-weight: 500;
        font-size: 16px;
        opacity: 0.8;
    }

    .try-now-btn {
        background: #6366f1;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        border: none;
    }

    /* Hero section */
    .hero-content h1 {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.2;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
    }

    .hero-content .highlight {
        color: #6366f1;
    }

    .hero-content p {
        font-size: 18px;
        color: #ffffff;
        opacity: 0.8;
        line-height: 1.6;
        margin-bottom: 30px;
        text-align: center;
    }

    /* Card styling for analytics */
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 10px 0;
        color: #6366f1;
    }

    .metric-label {
        font-size: 1.1rem;
        color: #ffffff;
        opacity: 0.8;
    }

    .metric-change {
        font-size: 0.9rem;
        margin-top: 10px;
    }

    .positive-change {
        color: #2dd36f;
    }

    .negative-change {
        color: #ff4961;
    }

    /* Chat analysis preview card */
    .chat-analysis-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        margin: 20px auto;
        max-width: 500px;
    }

    .card-header {
        background: linear-gradient(135deg, #a855f7 0%, #6366f1 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
    }

    .metric-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .metric-bar {
        height: 6px;
        border-radius: 3px;
        margin-top: 8px;
        width: 200px;
    }

    .bar-blue {
        background: linear-gradient(90deg, #3b82f6 0%, #1d4ed8 100%);
    }

    .bar-purple {
        background: linear-gradient(90deg, #8b5cf6 0%, #7c3aed 100%);
    }

    .bar-green {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
    }

    .chart-item {
        text-align: center;
        padding: 10px;
    }

    .chart-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }

    .chart-label {
        color: #ffffff;
        font-size: 14px;
        opacity: 0.8;
    }
</style>
""", unsafe_allow_html=True)



# Sidebar
with sidebar:
    st.markdown(
        "<center><h1 style='font-size: 42px; color: #6366f1;'>LEXIQ</h1></center>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h3 style='text-align: center; background:linear-gradient(135deg, #0fd850 10%, #f9f047 100%); 
        -webkit-background-clip: text; color: transparent;'>Your Personal Chat Analyzer</h3>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        'Upload Your File',
        type=['txt'],
        help="Export your WhatsApp chat as a .txt file"
    )

# Main content
if not uploaded_file:


    st.markdown("""
        <style>
        .header {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 10vh;
        }

        .logo {
            font-size: 64px;
            font-weight: bold;
            background: linear-gradient(90deg, #00416A, #0078AA); 
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>

        <div class="header">
            <div class="logo">LEXIQ</div>
        </div>
    """, unsafe_allow_html=True)




    # Hero section
    st.markdown("""
    <div class="hero-content">
        <h1>Unlock the <span class="highlight">insights</span> in your WhatsApp chats</h1>
        <p>LEXIQ analyzes your conversations and reveals patterns, sentiments, and engagement metrics you never knew existed.</p>
    </div>
    """, unsafe_allow_html=True)

    # Preview card
    with st.container():
        # st.markdown('<div class="chat-analysis-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Chat Analysis Preview</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<div class="metric-label">Message Count</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-value" style="font-size: 1.5rem;">1,243</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-bar bar-blue" style="width: 85%;"></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<div class="metric-label">Response Time</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-value" style="font-size: 1.5rem;">4.2 min</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-bar bar-purple" style="width: 60%;"></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<div class="metric-label">Sentiment</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-value" style="font-size: 1.5rem;">76% Positive</div>',
                        unsafe_allow_html=True)
        st.markdown('<div class="metric-bar bar-green" style="width: 76%;"></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                '<div class="chart-item"><div class="chart-icon">📊</div><div class="chart-label">Statistics</div></div>',
                unsafe_allow_html=True)
        with col2:
            st.markdown(
                '<div class="chart-item"><div class="chart-icon">📈</div><div class="chart-label">Trends</div></div>',
                unsafe_allow_html=True)
        with col3:
            st.markdown(
                '<div class="chart-item"><div class="chart-icon">💬</div><div class="chart-label">Messages</div></div>',
                unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h3 style="color: #ffffff;">👈 Upload your WhatsApp chat file to get started!</h3>
        <p style="color: #ffffff; opacity: 0.8;">Use the file uploader in the sidebar to begin your analysis</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 📖 How to Export WhatsApp Chat")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
                **For Android:**
                1. Open WhatsApp and go to the chat
                2. Tap the three dots menu
                3. Select "More" → "Export chat"
                4. Choose "Without media"
                5. Save the .txt file
                """)

    with col2:
        st.markdown("""
                **For iPhone:**
                1. Open WhatsApp and go to the chat  
                2. Tap the contact/group name
                3. Scroll down and tap "Export Chat"
                4. Choose "Without Media"
                5. Save the .txt file
                """)

    st.info("📝 **Note**: This analyzer works with text-only chat exports. Media files are not required.")



else:
    # Analytics Dashboard
            st.title("🔍 Chat Analytics Dashboard")

            bytes_data = uploaded_file.getvalue()
            data = bytes_data.decode('utf-8')
            df = preprocessor.preprocess(data)



            user_list = df['Users'].unique().tolist()
            user_list.sort()
            user_list.insert(0, 'Overall')

            selected_user = st.sidebar.selectbox("Show Analysis wrt", user_list)

            chat_df = df[['Users', 'Messages', 'Date']].tail(20)  # Last 20 messages

            # WhatsApp-style CSS
            st.markdown("""
               <style>
               .chat-bubble {
                   max-width: 80%;
                   padding: 10px 15px;
                   border-radius: 15px;
                   margin: 8px 0;
                   font-size: 14px;
                   line-height: 1.5;
                   word-wrap: break-word;
               }
               .left {
                   background-color: #2a2f32;
                   color: white;
                   align-self: flex-start;
                   border-top-left-radius: 0;
               }
               .right {
                   background-color: #005c4b;
                   color: white;
                   align-self: flex-end;
                   border-top-right-radius: 0;
                   margin-left: auto;
               }
               .sender {
                   font-weight: bold;
                   font-size: 12px;
                   color: #8ed1fc;
                   margin-bottom: 3px;
               }
               .timestamp {
                   font-size: 10px;
                   color: #ccc;
                   margin-top: 5px;
                   text-align: right;
               }
               .chat-container {
                   display: flex;
                   flex-direction: column;
               }
               </style>
               """, unsafe_allow_html=True)

            # Render each message as a chat bubble
            for _, row in chat_df.iterrows():
                is_user = row['Users'] == selected_user  # Change to your own name if needed
                bubble_class = "right" if is_user else "left"
                st.markdown(f"""
                   <div class="chat-container">
                       <div class="chat-bubble {bubble_class}">
                           <div class="sender">{row['Users']}</div>
                           <div>{row['Messages']}</div>
                           <div class="timestamp">{row['Date'].strftime('%b %d, %I:%M %p')}</div>
                       </div>
                   </div>
                   """, unsafe_allow_html=True)

            if st.sidebar.button('Show Analysis'):
                num_msg, words, media, links = helper.fetch_stats(selected_user, df)

                # Top metrics cards
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Total Messages</div>
                        <div class="metric-value">{num_msg}</div>
                        <div class="metric-change positive-change">+12.5% from last week</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Total Words</div>
                        <div class="metric-value">{words}</div>
                        <div class="metric-change positive-change">+7.2% from last week</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Media Shared</div>
                        <div class="metric-value">{media}</div>
                        <div class="metric-change positive-change">+3.1% from last week</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Links Shared</div>
                        <div class="metric-value">{links}</div>
                        <div class="metric-change negative-change">-5.3% from last week</div>
                    </div>
                    """, unsafe_allow_html=True)

                # Finding the busiest user in the group
                if selected_user == "Overall":
                    # Get the top 5 most busy users
                    x, y = helper.most_busy_users(df)
                    fig = px.bar(
                        x=x.values,
                        y=x.index,
                        orientation='h',
                        text=x.values,
                        labels={'x': "Message Count", 'y': 'User'},
                        color=x.values,
                        color_continuous_scale='Viridis'
                    )

                    fig.update_layout(
                        title="Top 5 Active Users",
                        height=400,
                        showlegend=False,
                        xaxis_title="Message Count",
                        yaxis_title='Users',
                        template='plotly_white',
                        plot_bgcolor='#22273a',
                        paper_bgcolor='#22273a',
                        font=dict(color='white')

                    )

                    fig.update_traces(
                        texttemplate="%{text} Msg's",
                        textposition='outside',
                        marker_line_color='white',
                        marker_line_width=0.5
                    )
                    col1, col2 = st.columns(2)
                    with col1:
                        st.plotly_chart(fig, use_container_width=True)

                    with col2:
                        # Sort values based on count
                        sorted_data = y.sort_values('count', ascending=False)

                        # Calculate percentages
                        percentages = sorted_data['count'] / sum(sorted_data['count']) * 100

                        # Create a new DataFrame with percentages
                        plot_data = pd.DataFrame({
                            'Percent_Contribute': sorted_data['Percent Contribute'],
                            'count': sorted_data['count'],
                            'percentage': percentages
                        })

                        # Group small slices into "Others"
                        threshold = 3  # percentage threshold
                        main_data = plot_data[plot_data['percentage'] >= threshold]
                        others = plot_data[plot_data['percentage'] < threshold]

                        if not others.empty:
                            others_row = pd.DataFrame({
                                'Percent_Contribute': ['Others'],
                                'count': [others['count'].sum()],
                                'percentage': [others['percentage'].sum()]
                            })
                            plot_data = pd.concat([main_data, others_row], ignore_index=True)
                        else:
                            plot_data = main_data

                        # Create Plotly pie chart
                        fig = px.pie(
                            plot_data,
                            values='count',
                            names='Percent_Contribute',
                            color_discrete_sequence=px.colors.sequential.algae,  # Use blue color palette
                            hole=0.4,  # Creates a donut chart effect
                        )

                        # Update layout with your preferred color theme
                        fig.update_layout(
                            title_text='Contribution Distribution',
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=-0.2,
                                xanchor="center",
                                x=0.5
                            ),
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#22237a'),
                            title_font_color='#ffffff',
                        )

                        # Make the hovering information more informative
                        fig.update_traces(
                            textposition='inside',
                            textinfo='percent',
                            hoverinfo='label+percent+value',
                            marker=dict(line=dict(color='#ffffff', width=2))
                        )

                        # Display the chart in Streamlit
                        st.plotly_chart(fig, use_container_width=True)
                    col1,col2 = st.columns(2)
                    top_pos = df.sort_values(by='Sentiment', ascending=False).head(5)[
                        ['Users', 'Messages', 'Sentiment']]
                    top_neg = df.sort_values(by='Sentiment').head(5)[['Users', 'Messages', 'Sentiment']]


                    # Define a message card function
                    def render_message_card(user, message, sentiment, sentiment_type):
                        emoji = "💚" if sentiment_type == "positive" else "💔"
                        color = "#00cc99" if sentiment_type == "positive" else "#ff4d4d"
                        return f"""
                                                        <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; margin-bottom:10px; border-left:5px solid {color};">
                                                            <p style="margin:0; color:#888;">{emoji} <b style="color:#fff;">{user}</b></p>
                                                            <p style="margin:5px 0; color:#ccc;">{message}</p>
                                                            <p style="margin:0; color:{color}; font-weight:bold;">Sentiment: {sentiment:.2f}</p>
                                                        </div>
                                                        """


                    # Layout in two columns

                    with col1:
                        st.subheader("💚 Top 5 Positive Messages")
                        for _, row in top_pos.iterrows():
                            st.markdown(
                                render_message_card(row['Users'], row['Messages'], row['Sentiment'], "positive"),
                                unsafe_allow_html=True)
                    with col2:
                        st.subheader("💔 Top 5 Negative Messages")
                        for _, row in top_neg.iterrows():
                            st.markdown(
                                render_message_card(row['Users'], row['Messages'], row['Sentiment'], "negative"),
                                unsafe_allow_html=True)
                    col1,col2 = st.columns(2)
                    mean_sentiments = df.groupby('Users')['Sentiment'].mean()
                    most_positive = mean_sentiments.idxmax()
                    most_negative = mean_sentiments.idxmin()
                    with col1:
                        st.markdown(
                            f"### 🌟 Most Positive User: `{most_positive}`  \nAverage Sentiment Score: `{mean_sentiments[most_positive]:.2f}`")
                    with col2:
                        st.markdown(
                            f"### ⚡ Most Negative User: `{most_negative}`  \nAverage Sentiment Score: `{mean_sentiments[most_negative]:.2f}`")


                    # Group by month and calculate average sentiment
                    monthly_sentiment = df.groupby('Month')['Sentiment'].mean().reset_index()

                    # Optional: Map month numbers to names
                    monthly_sentiment['Month'] = pd.to_datetime(monthly_sentiment['Month'], format='%m').dt.strftime(
                        '%B')

                    # Create the smooth line + gradient area chart
                    fig = go.Figure()

                    fig.add_trace(go.Scatter(
                        x=monthly_sentiment['Month'],
                        y=monthly_sentiment['Sentiment'],
                        mode='lines',
                        line=dict(color='deepskyblue', width=2),
                        fill='tozeroy',
                        fillcolor='rgba(0, 191, 255, 0.2)',  # soft gradient
                        name='Avg Sentiment'
                    ))

                    # Update layout for dark theme
                    fig.update_layout(
                        title='Monthly Sentiment Analysis',
                        xaxis_title='Month',
                        yaxis_title='Average Sentiment',
                        template='plotly_dark',
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='white'),
                        height=350
                    )

                    # Display in Streamlit
                    st.plotly_chart(fig, use_container_width=True)

                # plotting the word cloud

                df_wc = helper.word_cloud(selected_user, df)
                wc_array = np.array(df_wc)

                fig = go.Figure()
                fig.add_trace(go.Image(z=wc_array))
                fig.update_layout(
                    paper_bgcolor='#22273a',
                    plot_bgcolor='#22273a',
                    margin=dict(l=0, r=0, t=0, b=0)
                )

                st.plotly_chart(fig, use_container_width=True)

                # Most common words used by Users

                most_df = helper.most_common_words(selected_user, df)

                col1, col2 = st.columns(2)

                with col1:

                    with st.container():
                        # Apply the container styling directly using markdown
                        st.markdown("""
                            <div style="
                                background-color: #22273a;
                                border-radius: 10px;
                                padding: 20px;
                                margin: 10px 0;
                                color: white;
                            ">
                                <h3>Frequently Used Words</h3>
                            </div>
                            """, unsafe_allow_html=True)

                        # Get your data

                        # Create a horizontal bar chart with Plotly
                        fig = px.bar(
                            x=most_df[1],
                            y=most_df[0],
                            orientation='h',
                            color_discrete_sequence=['#6f78f5'],  # Changed to better match dark background
                            labels={'x': 'Frequency', 'y': 'Words'},
                        )

                        # Customize the layout for better aesthetics with dark theme
                        fig.update_layout(
                            plot_bgcolor='#22273a',  # Match the card background
                            paper_bgcolor='#22273a',  # Match the card background
                            margin=dict(l=20, r=20, t=10, b=20),
                            font=dict(family="Arial, sans-serif", size=12, color="#ffffff"),
                            hoverlabel=dict(font_size=12, font_family="Arial, sans-serif"),
                            xaxis=dict(
                                showgrid=True,
                                gridcolor='rgba(255,255,255,0.1)',
                                tickfont=dict(color="#ffffff")
                            ),
                            yaxis=dict(
                                showgrid=False,
                                tickfont=dict(color="white")
                            ),
                            # Remove title since we added it in the HTML
                        )

                        # Show the chart in Streamlit
                        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

                emoji_df = helper.emoji_counter(selected_user, df)
                fig = go.Figure(data=[go.Pie(
                    labels=emoji_df[0],  # Emoji labels
                    values=emoji_df[1],  # Emoji counts
                    hole=.4,  # Creates the donut hole
                    textposition='outside',  # Shows text outside the slices
                    textinfo='percent',  # Shows percentage
                    textfont=dict(size=12, color='white'),
                    marker=dict(
                        # Auto-assign colors from a colorful palette
                        colors=['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC949'],
                        line=dict(color='#FFFFFF', width=1)
                    ),
                    showlegend=True
                )])

                # Update layout for better aesthetics
                fig.update_layout(
                    title=dict(
                        text="Top Emojis",
                        font=dict(size=18, color='white'),
                        x=0.5,
                        y=0.95
                    ),
                    plot_bgcolor='#22273a',
                    paper_bgcolor='#22273a',
                    margin=dict(l=20, r=20, t=50, b=20),
                    legend=dict(
                        orientation="h",
                        yanchor="top",
                        y=-0.1,
                        xanchor="center",
                        x=0.5,
                        font=dict(size=12)
                    ),
                    annotations=[
                        dict(
                            text=f"Total: {sum(emoji_df[1])}",
                            showarrow=False,
                            font=dict(size=14),
                            x=0.5,
                            y=0.5
                        )
                    ]
                )

                # Show the chart in Streamlit
                with col2:
                    st.plotly_chart(fig, use_container_width=True)



                # Sentiment Analysis

                # Example top messages

