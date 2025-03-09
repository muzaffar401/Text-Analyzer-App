# 📝 Text Analyzer

A powerful **Text Analyzer** web app built with **Streamlit** that provides various text analysis features, including:

✅ Word and character count  
✅ Vowel count  
✅ Longest and shortest word detection  
✅ Reverse text conversion  
✅ Most frequent word identification  
✅ Palindrome detection  
✅ Uppercase and lowercase conversion  
✅ Synonym and antonym finder  
✅ AI-powered grammar and spelling correction using **Groq API** 🚀  

## ✨ Features
- **Analyze text** for word count, character count, vowels, and more.
- **Find synonyms and antonyms** for any word.
- **AI-powered grammar and spelling correction** using **Groq API**.
- **Real-time results** with an interactive UI.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/muzaffar401/Text-Analyzer-App.git
cd text-analyzer
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🛠️ Groq API Setup
This app uses the **Groq API** for grammar and spelling correction. Follow these steps to set it up:

### 1️⃣ Get Your API Key
1. Go to the [Groq Website](https://groq.com/) and sign up.
2. Navigate to **API Keys** in your account settings.
3. Generate a new API key and copy it.

### 2️⃣ Add Your API Key
Replace the API key in the `app.py` file:
```python
groq_api_key = "your_api_key_here"
client = groq.Client(api_key=groq_api_key)
```

---

## 🤖 AI Model Used
The AI-powered grammar and spelling correction feature uses **Llama 3.3-70B-Versatile**:

🔹 **Model Name**: `llama-3.3-70b-versatile`
🔹 **Provider**: Groq API
🔹 **Capabilities**:
  - Advanced **grammar correction**
  - **Spelling error detection**
  - Context-aware text improvements

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✉️ Contact
Created by **Muzaffar Ahmed** for **Sir Hamza's Assignment**. Reach out via email or GitHub for any queries!

