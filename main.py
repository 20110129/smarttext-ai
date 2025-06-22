
import streamlit as st
import openai
import os

# 🔐 Set your OpenAI key (can use text box or env variable)
openai.api_key = os.getenv("OPENAI_API_KEY") or st.text_input("Enter your OpenAI API key", type="password")

st.title("📚 SmartText AI")
st.write("This AI tool helps you Summarize, Generate Quizzes, or Rewrite your text easily.")

# Task selection
task = st.selectbox("Choose Task", ["Summarize", "Generate Quiz", "Rewrite"])
user_input = st.text_area("Paste your notes, text, or paragraph here:")

# Run the AI
if st.button("Run AI Tool") and user_input and openai.api_key:
    with st.spinner("Thinking..."):
        prompt = ""

        if task == "Summarize":
            prompt = f"Summarize this text in 5 bullet points:\n\n{user_input}"
        elif task == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions from the following text:\n\n{user_input}"
        elif task == "Rewrite":
            prompt = f"Rewrite this text in a simpler and clearer way:\n\n{user_input}"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=600
            )
            st.subheader(f"{task} Result:")
            st.write(response['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"Error: {str(e)}")
