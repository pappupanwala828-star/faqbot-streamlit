import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
bot = ChatBot("FAQBot")

trainer = ListTrainer(bot)

# Training data
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

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Enter your message")

if st.button("Send") and user_input:

    # Get bot response
    response = bot.get_response(user_input)

    # Save messages
    st.session_state.messages.append(("User", user_input))
    st.session_state.messages.append(("Bot", str(response)))

# Display chat history
for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")