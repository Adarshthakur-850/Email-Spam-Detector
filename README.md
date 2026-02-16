# Email Spam Detector

A Python-based email spam classification system that uses natural language processing (NLP) and machine learning techniques to classify emails as **Spam** or **Not Spam (Ham)**. The project includes preprocessing, feature extraction, model training, evaluation, and visualization components.

---

## 🚀 Project Overview

Spam emails are unsolicited and often unwanted messages that clutter inboxes and can pose security risks. This project builds an automated system that accurately identifies whether an email is spam using machine learning.

✔️ Preprocesses email text data  
✔️ Trains a classification model on labeled dataset  
✔️ Evaluates model performance with metrics and plots  
✔️ Saves trained model for inference  

## 📁 Repository Structure

```

Email-Spam-Detector/
│
├─ **data/**               ← Data files used for training/testing
├─ **src/**                ← Source code (modules/functions)
├─ **models/**             ← Saved trained model files (.pkl)
├─ **plots/**              ← Visual evaluation graphs (confusion matrix, etc.)
├─ main.py                ← Main entry script
├─ requirements.txt       ← Required Python libraries
├─ README.md              ← Project documentation

````



## 🛠️ Features

- Data cleaning and preprocessing
- Text vectorization (e.g., TF-IDF)
- Machine learning classification (e.g., Naive Bayes, SVM)
- Model evaluation and visualization
- Save/load trained models for inference

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adarshthakur-850/Email-Spam-Detector.git
   cd Email-Spam-Detector


Create & activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

▶️ Usage
📌 Train the Model
python main.py train


This will preprocess the dataset, fit the model, and save it to the models/ folder.

📌 Predict on New Emails
python main.py predict


Enter email text when prompted — the system will classify it as Spam or Not Spam.

📊 Evaluation

After training, evaluation metrics and plots (e.g., confusion matrix, accuracy scores) are stored in the plots/ directory. Use them to analyze model performance.

💡 Example Output
Enter email text: "Congratulations! You've won a free trip!"
Prediction: SPAM
Confidence: 93%

🤝 Contributing

Contributions are welcome! If you’d like to improve the project:

Fork the repository

Create a new branch (feature/your-feature)

Commit your changes

Open a Pull Request

📄 License

This project is open source and available under the MIT License.

🧠 About

This repository demonstrates a practical implementation of an email spam detection system using NLP and traditional machine learning techniques. It can serve as a foundation for further enhancements, including deep learning or deployment as a web app.
