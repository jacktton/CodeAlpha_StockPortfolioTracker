Stock Portfolio Tracker
💡 Project Description

This is a simple Python-based Stock Portfolio Tracker developed as part of the Python Programming Internship at CodeAlpha.
The program allows users to manually input stock names and their quantities. Using predefined stock prices (hardcoded), it calculates the total investment value and optionally saves the summary to a .txt file.

It’s a beginner-friendly tool that demonstrates the use of dictionaries, input/output, loops, and basic file handling in Python.

⚙️ Features

Users can input multiple stock symbols and quantities.

Automatically calculates the total investment based on hardcoded prices.

Displays a detailed breakdown of the portfolio.

Option to save the portfolio summary to a text file.

🔑 Key Concepts Used

dictionary for storing stock prices

loops and conditionals for user input and flow control

file handling to optionally save the output

basic arithmetic for calculating total investment

🛠️ How to Run

Install Python (if not already installed)

Clone the repository or download the stock_tracker.py file

Run the script using the command:

python stock_tracker.py


Follow the on-screen instructions to input stocks and view your portfolio.

🖼️ Sample Output
Welcome to the Stock Portfolio Tracker!
Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT

Enter stock symbol (or type 'done' to finish): AAPL
Enter quantity of AAPL: 5
Enter stock symbol (or type 'done' to finish): TSLA
Enter quantity of TSLA: 2
Enter stock symbol (or type 'done' to finish): done

Your Portfolio:
AAPL: 5 shares × $180 = $900
TSLA: 2 shares × $250 = $500

Total Investment: $1400

📄 Output File (Optional)

If the user chooses to save, a file named portfolio_summary.txt will be created with the portfolio breakdown.
