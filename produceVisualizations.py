import matplotlib.pyplot as plt
import pandas as pd

def monthNuber(issue_d):
    monthYear = issue_d.split('-')
    months= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    offset = int(monthYear[1]) - 2008
    return offset * 12 + months.index(monthYear[0]) + 1

def getTickLabels(orderedGradeRows):
    interestingrows = [orderedGradeRows.loc[orderedGradeRows['order'] == i] for i in range(0, len(orderedGradeRows)) if i % int((len(orderedGradeRows)/6)) == 0]
    monthlabels = [str(interestingrows[i]['issue_d']).split()[1] for i in range(len(interestingrows)-1)]
    return monthlabels



csv = pd.read_csv('LoanStats3a.csv', low_memory=False)
gradeSumByDate = csv.groupby(['grade', 'issue_d']).agg(['sum', 'count', 'mean'])['loan_amnt'].reset_index()
orderedList = [monthNuber(issue_d=i) for i in gradeSumByDate['issue_d']]
gradeSumByDate['order'] = pd.Series(orderedList)
gradeSumByDate = gradeSumByDate.sort_values(by='order')
xticks = getTickLabels(gradeSumByDate.loc[gradeSumByDate['grade'] == 'A'].sort_values('order'))
meanplot = gradeSumByDate.pivot(index='order', columns='grade', values='mean').plot()
meanplot.legend(title='Grade')
meanplot.set_xlabel('Issue Month')
meanplot.set_xticklabels(xticks)
meanplot.set_ylabel('Average Loan Size')
sumplot = gradeSumByDate.pivot(index='issue_d', columns='grade', values='sum').plot()
sumplot.set_xlabel('Issue Month')
sumplot.set_xticklabels(xticks)
sumplot.set_ylabel('Total Dollars Loaned in Tens of Millions')
sumplot.legend(title='Grade')
countplot = gradeSumByDate.pivot(index='issue_d', columns='grade', values='count').plot()
countplot.set_xlabel('Issue Month')
countplot.set_ylabel('Number of Loans')
countplot.set_xticklabels(xticks)
countplot.figure.savefig('maeanplot.png')
sumplot.figure.savefig('sumplot.png')
countplot.figure.savefig('countplot.png')
countplot.legend(title='Grade')
meanplot.figure.show()
countplot.figure.show()
sumplot.figure.show()
