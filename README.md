Cashback → Financial Growth App

Overview

This project transforms traditional cashback rewards into financial empowerment tools. Instead of giving users short-term cashback, the system encourages saving, investing, and wealth-building habits.


Features

1. Auto Micro-Invest (Cashback Replacement)

* Converts cashback into small investments
* Encourages long-term wealth growth instead of instant spending

2.  Financial Growth Score

* Calculates a score based on:

  * Savings
  * Spending habits
* Helps users track financial health

3. Smart Saving Triggers

* Detects high spending patterns
* Suggests actionable saving advice

4. Gamified Wealth Milestones

* Users earn badges based on their financial score:

  * Beginner
  * Smart Saver
  *  Wealth Master

Project Structure

cashback-replacement-app

frontend/          # User Interface
   index.html
   app.js

backend/           # Server Logic
   server.py

ai_model/          # AI / Logic Layer
    logic.py


Technologies Used

* Python (Backend)
* Flask (Web Framework)
* HTML, CSS, JavaScript (Frontend)

 How to Run the Project

1. Clone the repository

git clone <your-repo-link>
cd cashback-replacement-app


2. Install dependencies

pip install flask

3. Run the backend server

python backend/server.py

4. Open frontend

* Open `frontend/index.html` in your browser

How It Works

1. User enters spending, savings, and cashback
2. Frontend sends data to backend API
3. Backend processes data using AI logic:

   * Calculates investment amount
   * Computes growth score
   * Generates saving suggestions
   * Assigns milestone badge
4. Results are displayed to the user


 Example Output

Invested: ₹120
Score: 65
Suggestion: High spending! Save at least ₹500 today.
Milestone: Smart Saver

 Future Scope

* Integrate real investment APIs (stocks, mutual funds)
* Add user authentication and database
* Track financial growth over time (charts & analytics)
* Use machine learning for smarter predictions
* Deploy on cloud platforms for real-world usage


