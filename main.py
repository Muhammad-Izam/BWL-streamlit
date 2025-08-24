import streamlit as st
import random
import time
from datetime import datetime, date
import base64

# Configure the page
st.set_page_config(
    page_title="💖 For My Jaan 💖",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Poppins:wght@300;400;600&display=swap');
    
    .main-header {
        font-family: 'Dancing Script', cursive;
        font-size: 4rem;
        background: linear-gradient(45deg, #ff6b6b, #feca57, #ff9ff3, #54a0ff);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 2rem 0;
        animation: gradient 3s ease infinite, float 6s ease-in-out infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .love-card {
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.3) 0%, rgba(255, 105, 180, 0.3) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        text-align: center;
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .heart-animation {
        font-size: 2rem;
        color: #ff6b6b;
        animation: heartbeat 1.5s ease-in-out infinite;
        display: inline-block;
        margin: 0 0.5rem;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        pointer-events: none;
        z-index: -1;
    }
    
    .heart {
        position: absolute;
        font-size: 1.5rem;
        color: rgba(255, 182, 193, 0.7);
        animation: float-up 6s infinite ease-in;
    }
    
    @keyframes float-up {
        0% {
            opacity: 0;
            transform: translateY(100vh) scale(0);
        }
        10% {
            opacity: 1;
            transform: translateY(90vh) scale(1);
        }
        90% {
            opacity: 1;
            transform: translateY(-10vh) scale(1);
        }
        100% {
            opacity: 0;
            transform: translateY(-10vh) scale(0);
        }
    }
    
    .message-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .photo-frame {
        border: 3px solid #ff6b6b;
        border-radius: 15px;
        padding: 10px;
        background: linear-gradient(45deg, #ff9a9e, #fecfef);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        margin: 1rem auto;
        max-width: 300px;
    }
    
    .love-quote {
        font-family: 'Dancing Script', cursive;
        font-size: 1.8rem;
        color: #ff6b6b;
        text-align: center;
        margin: 2rem 0;
        font-style: italic;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b, #ff9ff3);
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
    }
    
    .memory-section {
        background: linear-gradient(135deg, rgba(255, 154, 158, 0.2), rgba(254, 207, 239, 0.2));
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
    }
    
    .countdown-box {
        background: linear-gradient(135deg, #ffeaa7, #fab1a0);
        color: Black;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Floating hearts background
st.markdown("""
<div class="floating-hearts">
    <div class="heart" style="left: 10%; animation-delay: 0s;">💖</div>
    <div class="heart" style="left: 20%; animation-delay: 1s;">💕</div>
    <div class="heart" style="left: 30%; animation-delay: 2s;">💗</div>
    <div class="heart" style="left: 40%; animation-delay: 3s;">💘</div>
    <div class="heart" style="left: 50%; animation-delay: 4s;">💖</div>
    <div class="heart" style="left: 60%; animation-delay: 5s;">💕</div>
    <div class="heart" style="left: 70%; animation-delay: 1.5s;">💗</div>
    <div class="heart" style="left: 80%; animation-delay: 2.5s;">💘</div>
    <div class="heart" style="left: 90%; animation-delay: 3.5s;">💖</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'love_messages_shown' not in st.session_state:
    st.session_state.love_messages_shown = []
if 'current_message' not in st.session_state:
    st.session_state.current_message = ""

# Main header
st.markdown('''
<div class="main-header">
    Happiest Birthday to my Beautiful Queen Laiba 💖
</div>
''', unsafe_allow_html=True)

# Heart animations
st.markdown('''
<div style="text-align: center; margin: 2rem 0;">
    <span class="heart-animation">💖</span>
    <span class="heart-animation">💕</span>
    <span class="heart-animation">💗</span>
    <span class="heart-animation">💘</span>
    <span class="heart-animation">💖</span>
</div>
''', unsafe_allow_html=True)

# Love messages collection
love_messages = [
    "You are the sunshine that brightens my darkest days, my Prettiest Laiba 🌞💖",
    "Every moment with you feels like a beautiful dream I never want to wake up from ifykyk that srf sakoon maza sab kuch apke sth hi ata hai💭✨",
    "Your smile is my favorite notification, ur your msgs nitofication makes me smile everytime, your laugh is my favorite song 😊🎵",
    "In your eyes, I found my home. In your heart, I found my love 🏠💕",
    "Apke sath jb hota hun tw itna acha acha horha hota hai sab kuch aik jo feelings aati hain andr se sakoon wali ur sab acha acha✨💫",
    "You are not just my love, you are my best friend, my soulmate, my jaan, my Princess, my everything 👫💖",
    "Bhale ap mujhse dur rehti hain baht ghr dur hai but koi bt nhi apse bt krke aesa lagta ke hrwaqt mery sath hain ap mery dil mei rehti hain ur sabkuch hi ap hain 🌍💕",
    "Every love story is beautiful, but ours is my favorite 📖💗",
    "With you, I've learned what true love really means ✨",
    "You make me want to be the best version of myself every single day 💖"
]

# Love quotes
love_quotes = [
    "In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine.",
    "You are my today and all of my tomorrows.",
    "I choose you. And I'll choose you over and over and over. Without pause, without a doubt, in a heartbeat.",
    "You are my sun, my moon, and all my stars.",
    "Every love story is beautiful, but ours is my favorite."
]

# Main content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Welcome message
    st.markdown('''
    <div class="love-card">
        <h2 style="color: #ff6b6b; font-family: 'Dancing Script', cursive;">
            Welcome to Your Special Place 💕
        </h2>
        <p style="font-size: 1.2rem; color: #F0FFF0;">
            ye website apke liye banayi hai maine khas tor pr apko birthday wish krne keliye,iska hr pixel pyaar se bhara hai ur isme hr lafz hr alfaaz mohabbat se likha hai, kiunke ap meri life mei aik precious gem hain meri jaan💓
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # Interactive love message generator
    st.markdown("### 💌 Love Message Just for You, ur isme jb bhi button press krogi tw aik new msg ayega🤭")
    
    if st.button("💖 Generate a Love Message 💖", key="love_msg"):
        available_messages = [msg for msg in love_messages if msg not in st.session_state.love_messages_shown]
        
        if not available_messages:
            st.session_state.love_messages_shown = []
            available_messages = love_messages
        
        selected_message = random.choice(available_messages)
        st.session_state.love_messages_shown.append(selected_message)
        st.session_state.current_message = selected_message
        st.balloons()
    
    # Display current message
    if st.session_state.current_message:
        st.markdown(f'''
        <div class="message-card">
            <h3>💕 A Message from My Heart</h3>
            <p style="font-size: 1.3rem; line-height: 1.6;">
                {st.session_state.current_message}
            </p>
        </div>
        ''', unsafe_allow_html=True)

# Three column layout for features
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    <div class="memory-section">
        <h3 style="color: #ff6b6b; text-align: center;">🌹 Why You're Special</h3>
        <ul style="list-style: none; padding: 0;">
            <li>💖 Your beautiful smile</li>
            <li>🌟 Your kind heart</li>
            <li>✨ Your amazing personality</li>
            <li>💕 The way you care for others</li>
            <li>🦋 Your gentle nature</li>
            <li>🌸 Your inner beauty</li>
            <li>🥰 Your behaviour with me</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="memory-section">
        <h3 style="color: #ff6b6b; text-align: center;">💫 Our Journey</h3>
        <div style="text-align: center;">
            <p>🌅 <strong>Every sunrise</strong> reminds me of you</p>
            <p>🌙 <strong>Every moonlight</strong> carries my love to you</p>
            <p>⭐ <strong>Every star</strong> in the sky knows your name</p>
            <p>🌈 <strong>Every rainbow</strong> is a promise of our future</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)



# Love quote section
st.markdown("---")
selected_quote = random.choice(love_quotes)
st.markdown(f'''
<div class="love-quote">
    "{selected_quote}"
</div>
''', unsafe_allow_html=True)
# Photo section
st.markdown("---")
st.markdown('''
            <div class="love-card">
                <h2 style="color: #ff6b6b; font-family: 'Dancing Script', cursive;">
                    Some moment or memorries with you💕
                </h2>
            </div>
''', unsafe_allow_html=True)
# Display images in a 3-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.31_ba1458fd.jpg")
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.31_7795a782.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.31_1c2f6f85.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.30_30860c07.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.30_fe88ec49.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.30_2603e3fe.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.29_08b08059.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.26_705816cd.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.25_ada9e799.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.26_dd14ea91.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.29_c1309864.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.26_8361edaf.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 12.53.29_b79c6cc2.jpg")
    
# some pictures of you
st.markdown('''
            <div class="love-card">
                <h2 style="color: #ff6b6b; font-family: 'Dancing Script', cursive;">
                    Some memorries of you💕
                </h2>
            </div>
''', unsafe_allow_html=True)
# Display images in a 3-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.24.42_43faa781.jpg")
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.43.24_07558f01.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.15.00_738b9bc9.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.27.22_a256e0ef.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.27.59_582b6304.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.28.46_a9bdacdb.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.32.40_2f9fe82b.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.32.40_79153192.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.32.43_cafac905.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.32.46_bcc6e7ea.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.32.45_45310e63.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.32.52_873d5603.jpg") 
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.33.14_d7c73735.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.33.14_e26ced9c.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.33.19_72263ce2.jpg")
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.41.08_fc2e45d1.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.41.09_833d3774.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.41.09_bf021132.jpg")
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.41.10_59c86d8f.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.24.43_1027f171.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.43.37_fb303a34.jpg")
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-23 at 21.21.26_f48a1902.jpg") 
with col2:
    st.image("E:\project python\WhatsApp Image 2025-08-23 at 21.21.26_a4ccb00b.jpg")
with col3:
    st.image("E:\project python\WhatsApp Image 2025-08-21 at 23.43.38_e8702cc2.jpg")
with col1:
    st.image("E:\project python\WhatsApp Image 2025-08-23 at 21.21.27_baca6846.jpg")


# Time together counter (example)
st.markdown("---")
st.markdown("### 💞Counting Our Beautiful Days Together💞")

# You can customize this date to when you first met or started dating
start_date = date(2023, 12, 17)  # Change this to your actual date
today = date.today()
days_together = (today - start_date).days

st.markdown(f'''
<div class="countdown-box">
    💕 We've shared {days_together} beautiful days together! 💕
    <br>
    And counting to the ♾️ inshaallah🥰
</div>
''', unsafe_allow_html=True)

# Promises section
st.markdown("### 💍 My Promises to You")
st.markdown('''
<div class="love-card">
    <div style="text-align: left; font-size: 1.1rem;">
        💖 I promise to love you more each day<br>
        💕 I promise ke kabhi daantunga nhi<br>
        🌟 I promise to support your dreams<br>
        💕 I promise to make you smile when you're sad<br>
        ✨ I promise to be your best friend forever<br>
        🌹 I promise and want to each and every moment with you<br>
        🌹 I promise to smile you everyday<br>
        💘 I promise to never stop showing you how much you mean to me
    </div>
</div>
''', unsafe_allow_html=True)

# Footer with love
st.markdown("---")
st.markdown('''
<div style="text-align: center; padding: 2rem; 
            background: linear-gradient(135deg, rgba(255, 182, 193, 0.3), rgba(255, 105, 180, 0.3));
            border-radius: 15px; margin-top: 2rem;">
    <h3 style="color: #ff6b6b; font-family: 'Dancing Script', cursive;">
        💖 Made with Endless Love for My Sweetheart Laiba 💖
    </h3>
    <p style="font-size: 1.1rem; color: #F8F8FF;">
        You are my heart, my Peincess, my koucho poucho, my bubu, my soul, my penguin,you are my everything. mery pas alfaazz tw nhi bachy hain abb kuch kehny keliye bs ye aik chota sa gift samjh lo ya aik chota sa simple sa wish meri taraf se meri jaan keliye!💕
    </p>
    <h3 style="color: #ff6b6b; font-family: 'Dancing Script', cursive;">
        💖Happiest Birthday Meri Jaan💖
    </h3>
    <div style="font-size: 2rem; margin-top: 1rem;">
        💖💕💗💘💖💕💗💘💖
    </div>
</div>
''', unsafe_allow_html=True)

