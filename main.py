import streamlit as st
import groq
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

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

# 3. Longest and Shortest Word
words = user_input.split()
if words:
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    st.subheader("Longest and Shortest Word")
    st.write(f"Longest Word: {longest_word}")
    st.write(f"Shortest Word: {shortest_word}")

# 4. Reverse Text
st.subheader("🔄 Reverse Text")
st.write(user_input[::-1])

# 5. Most Frequent Word
word_counts = Counter(words)
most_common_word, most_common_count = word_counts.most_common(1)[0]
st.subheader("Most Frequent Word")
st.write(f"'{most_common_word}' appears {most_common_count} times.")

# 6. Palindrome Detection
palindromes = [word for word in words if word.lower() == word.lower()[::-1] and len(word) > 1]
st.subheader("Palindrome Words")
st.write(palindromes if palindromes else "No palindromes found.")

# 7. Uppercase and Lowercase Conversion
st.subheader("🔄 Uppercase and Lowercase Conversion")
st.write("Uppercase Paragraph:")
st.write(user_input.upper())
st.write("Lowercase Paragraph:")
st.write(user_input.lower())

# 8. Synonyms & Antonyms Finder
st.subheader("Synonyms & Antonyms")
word_for_synonyms = st.text_input("Enter a word to find synonyms and antonyms:")
if word_for_synonyms:
    synonyms = set()
    antonyms = set()
    for syn in wordnet.synsets(word_for_synonyms):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    st.write(f"Synonyms: {', '.join(synonyms) if synonyms else 'None found'}")
    st.write(f"Antonyms: {', '.join(antonyms) if antonyms else 'None found'}")

# 9. Grammar and Spelling Correction using Groq API
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

# Footer
st.markdown("---")
st.write("Created by Muzaffar Ahmed for Sir Hamza's Assignment.")