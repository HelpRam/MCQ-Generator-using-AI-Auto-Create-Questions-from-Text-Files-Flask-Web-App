import os
import streamlit as st
from dotenv import load_dotenv  # Ensure you have python-dotenv installed
import google.generativeai as genai

# Load environment variables from the .env file (e.g., API keys)
load_dotenv()

# Configure the Google Gemini API by setting the API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please ensure it's correctly set in the environment variables.")
else:
    genai.configure(api_key=api_key)

# Specify the model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Function to create the prompt and interact with the Gemini API
def generate_mcq(grade, subject, subtopic, num_questions):
    prompt = f"""
    Generate {num_questions} multiple-choice questions for grade {grade} in the subject {subject} on the topic of {subtopic}. 
    Provide 4 answer options (A, B, C, D) for each question and highlight the correct answer.
    Format the output such that each question is followed by its options on separate lines.
    """

    try:
        # Use the specified model to generate content
        response = model.generate_content(prompt)
        return response.text.strip()  # Adjust based on the response structure

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Set up the page in Streamlit
st.set_page_config(page_title="MCQ Generator with Gemini LLM")

# Display a header for the app
st.header("Gemini LLM MCQ Generator")

# Collect inputs from the user about what kind of MCQs they want
grade = st.selectbox("Select Grade:", [str(i) for i in range(1, 13)])  # Generates grades from 1 to 12
subject = st.text_input("Enter Subject:", key="subject_input")
subtopic = st.text_input("Enter Subtopic:", key="subtopic_input")
num_questions = st.slider("Number of Questions:", min_value=1, max_value=10)

# Button to trigger MCQ generation
submit = st.button("Generate MCQs")

# When the button is clicked and the necessary inputs are provided
if submit and subject and subtopic:
    st.subheader(f"MCQs for {subject} ({subtopic}) - Grade {grade}")

    # Call the function to generate MCQs using the Gemini API
    response = generate_mcq(grade, subject, subtopic, num_questions)

    if response:
        # Split response by questions
        questions = response.split("\n\n")  # Adjust splitting based on API response format

        for idx, question_block in enumerate(questions):
            # Assuming the format is consistent with questions followed by their options
            question_parts = question_block.strip().split("\n")
            
            if len(question_parts) >= 5:  # Ensure at least 1 question and 4 options
                question_text = question_parts[0].strip()
                options = question_parts[1:5]  # Extract first 4 lines as options

                # Display the question with proper format
                st.write(f"**Question {idx + 1}:** {question_text}")
                
                # Display each option (A, B, C, D)
                st.write(f"A) {options[0].strip()}")
                st.write(f"B) {options[1].strip()}")
                st.write(f"C) {options[2].strip()}")
                st.write(f"D) {options[3].strip()}")

                # Add spacing between questions
                st.write("")
