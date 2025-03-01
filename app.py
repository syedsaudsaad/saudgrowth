# streamlit
import streamlit as st

# This must be the first Streamlit command you call
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Your remaining Streamlit code goes here
st.title("Welcome to the Growth Mindset Project")


st.write=("Embrace challenges,learn from mistakes,and unlock your full potential.This AI-powered app helps you build a growth mindset a growth mindset with reflection, challenges,and a chievements!🌟")

# quote section
st.header=("🌞 Today's Growth Mindset Quote")
st.write=("/sucess is not final, failure is not fatal: it is the courage to continue thatcount./- winston churchill")

st.header("❤️‍🔥 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# condition
if user_input:
    st.success(f"🔶youre facing: {user_input}. keep pushing forward towords goal!🌹")
else:
    st.warning("Tell us about your challenge to get stared!")

    #reflexing
    st.header("Reflect on Your Learning")
    reflection= st.text_area("Write your reflections here:")

    if reflection:
        st.success(f"💐Great Insight! Your reflection:{reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")

#acheivements
st.header=("⭕ Celebrate Your Wins!")
achivement = st.text_input("Share something you've recently accomplished:")

if achivement:
    st.success(f"🍪 Amazing! You achieved:{achivement}")
else:
    st.info("Big or small, every acheivement counts! Share one now 📆")

    #footer
    st.write("- - -")
    st.write("✅ keep believing in yourself. Growth is ajourey, not a destination!💯")
    st.write("***❎ created by SYED SAUD SAAD***")
