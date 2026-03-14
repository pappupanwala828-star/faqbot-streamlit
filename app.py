import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("FAQBot")

trainer = ListTrainer(bot)

faq_data = [
    "What is your name?",
    "I am FAQBot.",
    "What are your working hours?",
    "Our working hours are 9 AM to 5 PM.",
    "Where is the office?",
    "The office is located in the main building.",
    "How to contact support?",
    "You can contact support at support@gmail.com."
]

trainer.train(faq_data)

st.title("FAQBot Chat App")

user_input = st.text_input("Enter your message")

if st.button("Send"):
    response = bot.get_response(user_input)
    st.write("Bot:", response)