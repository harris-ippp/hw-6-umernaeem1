import pandas as pd

from matplotlib import pyplot as plt

from e1 import *

list = []
for x in ELECTION_ID:
    file_name = 'president_general_' + str(x[0]) + '.csv'
    header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(file_name, index_col = 0,
                   thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = x[0]
    df['Democratic Share'] = df['Democratic']/df['Total Votes Cast']
    df['Republican Share'] = df['Republican']/df['Total Votes Cast']
    df = df[["Democratic Share", "Republican Share", "Total Votes Cast", "Year"]]

    list.append(df)

big_data = pd.concat(list)
county = {'Accomack County':'accomack_county.pdf', 'Albemarle County':'albemarle_county.pdf', \
          'Alexandria City':'alexandria_city.pdf', 'Alleghany County':'alleghany_county.pdf'}

for x, y in county.items():
    df = big_data[big_data.index == x]
    plt.plot(df['Year'], df['Democratic Share'], label = 'Democratic Share')
    plt.plot(df['Year'], df['Republican Share'], label = 'Republican Share')
    plt.xlabel("Year")
    plt.ylabel("Vote Share")
    plt.title("Vote Share vs Years\n" + x)
    plt.legend()
    plt.savefig(y)
