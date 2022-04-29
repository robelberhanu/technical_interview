from calendar import month
import pandas as pd
import matplotlib.pyplot as plt 


# Import spreadsheet
file = pd.read_excel("Income and Expenditure.xlsx")


def plot_data(file):

    # Separate x and y values
    Month = list(file['Month'])
    Income = list(file['Income'])
    Expenses = list(file['Expenses'])

    plt.figure(figsize=(10,10))
    plt.style.use('seaborn')
    plt.title("Income vs Expenditure")
    plt.xlabel("Month")
    plt.ylabel("Income and Expenses")
    plt.plot(Month, Income, label ='Income')
    plt.plot(Month, Expenses, label ='Expenses')
    plt.legend()
    plt.show()

    
plot_data(file)
    
 