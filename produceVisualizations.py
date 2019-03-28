import matplotlib.pyplot as plt
import pandas as pd

def monthNuber(issue_d, ):
    monthYear = issue_d.split('-')
    months= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    offset = int(monthYear[1]) - 2008
    return offset * len(months) + months.index(monthYear[0]) + 1

def getTickLabels(orderedGradeRows, tickmarks = 6):
    monthlabels = [str(orderedGradeRows.loc[orderedGradeRows['order'] == i]['issue_d']).split()[1] for i in range(0, len(orderedGradeRows)) if i % int((len(orderedGradeRows)/tickmarks)) == 0]
    return monthlabels

def createPlot(dataFrame, value, xticks, y_label, name, legend = "Grade", x_label = 'Issue Month'):
    plot = dataFrame.pivot(index='order', columns='grade', values=value).plot()
    plot.legend(title=legend)
    plot.set_xlabel(x_label)
    plot.set_xticklabels(xticks)
    plot.set_ylabel(y_label)
    plot.figure.savefig(name +".png")
    return plot


def main():
    csv = pd.read_csv('LoanStats3a.csv', low_memory=False)
    gradeSumByDate = csv.groupby(['grade', 'issue_d']).agg(['sum', 'count', 'mean'])['loan_amnt'].reset_index()
    orderedList = [monthNuber(issue_d=i) for i in gradeSumByDate['issue_d']]
    gradeSumByDate['order'] = pd.Series(orderedList)
    gradeSumByDate = gradeSumByDate.sort_values(by='order')
    xticks = getTickLabels(gradeSumByDate.loc[gradeSumByDate['grade'] == 'A'].sort_values('order'))
    # now we have an ordered set of data and xticks lets make some graphs
    meanplot = createPlot(gradeSumByDate, "mean", xticks, "Average Loan Size", 'meanplot')
    sumplot = createPlot(gradeSumByDate, "sum", xticks, "Total Dollars Loaned in Tens of Millions", "sumplot")
    countplot = createPlot(gradeSumByDate, "count", xticks, "Number of Loans", "countplot")
    countplot.figure.show()
    meanplot.figure.show()
    sumplot.figure.show()


if __name__ == "__main__":
    main()
