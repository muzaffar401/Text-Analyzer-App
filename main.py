import streamlit as st
import groq

# Set up Groq API client
groq_api_key = "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"  # Replace with your Groq API key
client = groq.Client(api_key=groq_api_key)

# Streamlit App Title
st.title("📝 Text Analyzer")
st.write("Analyze your text and improve its grammar and spelling using AI!")

# User Input
st.header("Enter Your Text")
user_input = st.text_area("Paste your paragraph here:", height=200)

# Validate input
if not user_input.strip():
    st.error("Please enter some text to analyze.")
    st.stop()

# Text Analysis Features
st.header("📊 Text Analysis")

# 1. Word and Character Count
word_count = len(user_input.split())
char_count = len(user_input)
st.subheader("Word and Character Count")
st.write(f"Total Words: {word_count}")
st.write(f"Total Characters (including spaces): {char_count}")

# 2. Vowel Count
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in user_input if char in vowels)
st.subheader("Vowel Count")
st.write(f"Total Vowels: {vowel_count}")

# 3. Search and Replace
st.subheader("🔍 Search and Replace")
search_word = st.text_input("Enter a word to search for:")
replace_word = st.text_input("Enter a word to replace it with:")
if search_word and replace_word:
    modified_text = user_input.replace(search_word, replace_word)
    st.write("Modified Paragraph:")
    st.write(modified_text)

# 4. Uppercase and Lowercase Conversion
st.subheader("🔄 Uppercase and Lowercase Conversion")
st.write("Uppercase Paragraph:")
st.write(user_input.upper())
st.write("Lowercase Paragraph:")
st.write(user_input.lower())

# 5. Type Casting
st.subheader("Type Casting")
st.write(f"Word Count (as string): {str(word_count)}")
st.write(f"Vowel Count (as string): {str(vowel_count)}")

# 6. Operators
st.subheader("Operators")
contains_python = "Python" in user_input
st.write(f"Does the text contain the word 'Python'? {contains_python}")

average_word_length = char_count / word_count if word_count > 0 else 0
st.write(f"Average Word Length: {average_word_length:.2f}")

# 7. Grammar and Spelling Correction using DeepSeek API
st.header("✨ AI-Powered Grammar and Spelling Check")
if st.button("Check Grammar and Spelling"):
    with st.spinner("Analyzing your text..."):
        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Fix the grammar and spelling errors in this text and provide the corrected version only:\n\n{user_input}",
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            corrected_text = response.choices[0].message.content.strip()
            st.subheader("Corrected Paragraph")
            st.write(corrected_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 8. Roman Urdu Translation (Using DeepSeek Model)
st.header("🌐 Translate to Roman Urdu")
if st.button("Translate to Roman Urdu"):
    with st.spinner("Translating your text..."):
        try:
            response_translation = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Translate this text into Roman Urdu only. Do not include explanations or any extra content:\n\n{user_input}",
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            roman_urdu_text = response_translation.choices[0].message.content.strip()
            st.subheader("Roman Urdu Translation")
            st.write(roman_urdu_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.write("Created by Muzaffar Ahmed for Sir Hamza's Assignment.")
