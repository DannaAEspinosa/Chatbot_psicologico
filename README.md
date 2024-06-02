# 🤖 Psychological Healthcare Chatbot

## 📋 Project Overview

This project aims to develop a medium-complexity expert system using Python and the Experta library, coupled with Bayesian networks implemented via the pgmpy library. The primary goal is to provide a chatbot that offers personalized psychological support and guidance, addressing the challenges individuals face in accessing mental health services such as stigma, cost, and resource availability.

## 🎯 Objectives

- **OE4.1**: Implement computation with probabilities and understand the Principle of Maximum Entropy.
- **OE4.2**: Develop an expert system utilizing reasoning with Bayesian networks.
- **OE5.1-5.4**: Address the design, development, common errors, and software engineering principles in expert systems.

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Experta
- pgmpy
- dotenv

### Steps to Install and Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/psychological-healthcare-chatbot.git
    cd psychological-healthcare-chatbot
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On MacOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the PostgreSQL database**:
    - Create a PostgreSQL database named `psychological_healthcare`.
    - Update the `.env` file with your database credentials.

6. **Run the database migrations**:
    ```bash
    flask db upgrade
    ```

7. **Run the application**:
    ```bash
    flask run
    ```

## 🌟 Features

- User-friendly chatbot interface for conversational interactions.
- Psychological assessments, coping strategies, and intervention techniques.
- Bayesian networks for modeling relationships between symptoms, diagnoses, and treatments.
- Natural language processing for understanding and responding to user inputs.

## 🚀 Usage

1. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:5000/`.
    
2. **Register**:
    - Click on the `Register` button and fill in your details to create an account.
    
3. **Login**:
    - Click on the `Login` button and enter your credentials.

4. **Use the Chatbot**:
    - Once logged in, you can start interacting with the chatbot for psychological support.

## 🛠️ System Design

- **Requirements Analysis**: Scope of psychological issues addressed, target demographics, and user interface requirements.
- **Knowledge Acquisition**: Guidelines from mental health professionals, and knowledge base details.
- **System Implementation**: Use of Python, Experta, and pgmpy for rule-based reasoning and Bayesian decision-making.

## 🔍 Testing and Validation

Overview of testing methodologies used to ensure the chatbot's effectiveness, accuracy, and user experience, including usability testing and stress testing.

## 👥 Authors

- **Diana Lorena Balanta Solano**
- **Carlos Javier Bolaños Riascos**
- **Danna Alexandra Espinosa Arenas**
