import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv('LoanStats3a.csv', low_memory=False)
gradeSumByDate = csv.groupby(['grade', 'issue_d']).agg(['sum', 'count', 'mean'])['loan_amnt'].reset_index()
print(gradeSumByDate)
meanplot = gradeSumByDate.pivot(index='issue_d', columns='grade', values='mean').plot()
sumplot = gradeSumByDate.pivot(index='issue_d', columns='grade', values='sum').plot()
countplot = gradeSumByDate.pivot(index='issue_d', columns='grade', values='count').plot()
meanplot.figure.savefig('maeanplot.png')
sumplot.figure.savefig('sumplot.png')
countplot.figure.savefig('countplot.png')


meanplot.figure.show()

