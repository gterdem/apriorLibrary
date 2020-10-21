from typing import Counter
import itertools


def getIndividualSupport(dataDictionary, totalTransactions, threshold=2):
    dataDict = Counter(sorted(dataDictionary))
    cleanedDict = [item for item in dataDict.items() if item[1] >= threshold]
    supportList = []
    for item in cleanedDict:
        if item[1] >= threshold:
            supportList.append((item[0], item[1] / totalTransactions))
    return supportList
    # myList = [value for value in dataDict.values() if value >= threshold]
    # for key, value in cleanedDict.items():
    #     if value >= threshold:
    #         supportList.append((key, value / totalTransactions))
    # return supportList


def getTransactions(data, printData=False):
    """Creates MarketTransaction object list from pandas.read_csv DataFramee object

    Args:
        data (DataFrame): pandas.read_csv result
        printData (bool, optional): Determines if the items will be printed out. Defaults to False.

    Returns:
        [list]: [list of MarketTransaction]
    """
    transactions = []
    for t in data.values:
        transaction = MarketTransaction(t)
        transactions.append(transaction)
        if printData:
            print(transaction.tId, transaction.Items)
    return transactions


def getCleanData(data):
    """Returns cleaned data from pandas dataframe

    Args:
        data ([DataFrame]): [pandas DataFrame object]

    Returns:
        [list]: [list object]
    """
    return [
        item
        for sublist in data.values
        for item in sublist
        if (str(item) != "nan" and not str(item).startswith("T"))
    ]


class MarketTransaction:
    def __init__(self, transaction):
        self.tId = transaction[0]
        self.Items = []
        for i in range(1, len(transaction)):
            if str(transaction[i]) != "nan":
                self.Items.append(transaction[i])

        self.Combinations = self.calculateCombinations()

    def calculateCombinations(self):
        combList = []
        for i in range(2, len(self.Items) + 1):
            # maybe check out powerset https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
            comb = itertools.combinations(self.Items, i)
            combList.append(list(comb))
        return combList