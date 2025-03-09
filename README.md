# Text Analyzer using Streamlit & Groq API

## 📌 Project Overview
This project is a **Text Analyzer** built using **Streamlit** and powered by **Groq API** for AI-driven grammar and spelling correction. It allows users to analyze their text, count words and characters, replace words, convert text to uppercase/lowercase, and check grammar and spelling with AI. Additionally, the app provides a **Roman Urdu translation** of the corrected text.

## 🚀 Features
- Word and character count
- Vowel count
- Search and replace functionality
- Uppercase and lowercase conversion
- Type casting and basic operators
- AI-powered grammar and spelling correction using **Groq API**
- Roman Urdu translation of corrected text

---

## 🛠️ Installation & Setup Guide
### Prerequisites
Make sure you have the following installed on your system:
- Python 3.8+
- `uv` (Dependency management tool)
- `Streamlit`
- `groq` (Groq API client library)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/text-analyzer.git
cd text-analyzer
```

### 2️⃣ Install Dependencies using `uv`
```bash
uv venv .venv  # Create a virtual environment
source .venv/bin/activate  # Activate virtual environment (Linux/macOS)
.venv\Scripts\activate  # Activate virtual environment (Windows)
uv pip install -r requirements.txt  # Install dependencies
```

### 3️⃣ Set Up Groq API Key
1. **Create a Groq API Key:**
   - Go to [Groq API](https://groq.com/) and sign up or log in.
   - Navigate to the API section and generate a new API key.
   - Copy the API key.

2. **Store the API Key:**
   - Create a `.env` file in the project root directory and add:
     ```bash
     GROQ_API_KEY="your-api-key-here"
     ```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📚 How to Use the App
1. Open the app in your browser after running it.
2. Enter a paragraph or text in the input area.
3. Use various features like:
   - Checking word and character count.
   - Searching and replacing words.
   - Converting text to uppercase or lowercase.
   - Checking for spelling and grammar errors using AI.
   - Translating the corrected text into Roman Urdu.
4. Click on the respective buttons to perform actions.

---

## 🔗 API Usage - Groq
This project uses **Groq API** for text correction and translation.

### **Grammar & Spelling Correction API Request**
```python
response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Check the grammar and spelling of the following text: \n\n Your text here"}
    ],
    model="mixtral-8x7b-32768",
)
corrected_text = response.choices[0].message.content.strip()
```

### **Roman Urdu Translation API Request**
```python
response_translation = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Translate the following text into Roman Urdu: \n\n Corrected text here"}
    ],
    model="mixtral-8x7b-32768",
)
roman_urdu_text = response_translation.choices[0].message.content.strip()
```

---

## 👨‍💻 Author
**Muzaffar Ahmed** - Built for **Sir Hamza's Assignment**

Feel free to improve or contribute to the project!

---

## ⚖️ License
This project is for educational purposes and personal use. Feel free to modify and extend it as needed.

