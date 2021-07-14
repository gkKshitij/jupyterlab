chown -R user-id:group-id D:/workspace/kshitij/m76



import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from fuzzywuzzy import fuzz
xl_file = pd.ExcelFile(file_name)
dfs = pd.read_excel(file_name, sheet_name=None)
df = pd.read_csv('random_data.gz')
df = pd.read_excel('File.xlsx', sheetname='Sheet1')

#read from second header
mydata = pd.read_csv("workingfile.csv", header = 1)

#trimming nan values with threshold
df4 = df4.dropna(thresh=2, axis=1)

#trimming from top
df2 = df2.drop(df2.index[:148], axis=0)

#trimming from bottom
df2 = df2.drop(df2.index[:148], axis=0)

#change index
df1 = df1.set_index('No.')

#renaming columns
df4.rename(columns={'Unnamed: 2':'Name'}, inplace=True)

#pro style trimming
df1 = df1.iloc[0:143,0:11]


#dropping rows and columns with nan values
df1 = df1.dropna(how='all')
print(df1)
df1 = df1.dropna(how='all', axis=1)
print(df1)


#dropping duplicates
df['Events'] = df.groupby('Letters')['Numbers'].transform(pd.Series.value_counts)
df.drop_duplicates()



#drop particular rows
df1 = df1.drop([0, 2, 4, 8, 16])

#dropping columns
df1.drop('Unnamed: 0', axis=1)

#resetting index
df.reset_index(drop=True, inplace=True)

#using backward fill and forward fill methods
df = df.bfill(axis=0)
nba["College"].fillna( method ='ffill', inplace = True)

#replace 0 with NaN
#for all
df= df.replace({'0':np.nan, 0:np.nan})
#for particular columns
cols = ['No', 'CLZS', 'DARIBA SMELTERS', 'DEBARI SMELTERS', 'KAYAD MINES',
       'RAM CENTRAL STORE', 'RAM GEPL', 'RAM MILL', 'RAM OC',
       'RAM SARAL DRILL & ENGINEERING', 'RAM SHAFT SINKERS', 'RAM STORE',
       'RAM UG', 'RAM-OC', 'RAM-SECURITY', 'RD MILL', 'RD MINES',
       'RD POWER PLANT', 'SK MILL', 'SK MINES', 'ZAWAR MILL', 'ZAWAR MINES']
df0[cols] = df0[cols].replace({'0':np.nan, 0:np.nan})

#appending rows
df4.loc['16'] = [13, 'Chandra Shekhar', 'SJP', '223 days', '223 days']

#sort
df.sort_values(by=['col1'])

#concatenate
df.groupby(df.index).sum()

#lamda function
df = df.apply(lambda x: pd.Series(x.dropna().values)).fillna('')


#imp super merge
pd.merge(df_1, df_2, right_index=True, left_index=True)

#merge after making index same
mergedDf = empDfObj.merge(salaryDfObj, left_index=True, right_on='EmpID')
mergedDf = mergedDf.set_index('EmpID')

#generating random
df = pd.DataFrame(pd.np.random.randn(50000, 300))



#writing to excel
writer = pd.ExcelWriter('output.xlsx')
df99.to_excel(writer, sheet_name='mainoutput')
df1.to_excel(writer, sheet_name='first table')
df2.to_excel(writer, sheet_name='second table')
df3.to_excel(writer, sheet_name='third table')
writer.save()

report_name = 'example_report.xlsx'
sheet_name = 'Sheet1'
writer = pd.ExcelWriter(report_name, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name, index=False)
writer.save()



# define the workbook
workbook = writer.book
worksheet = writer.sheets[sheet_name]
# create a chart line object
chart = workbook.add_chart({'type': 'line'})
# configure the series of the chart from the spreadsheet
# using a list of values instead of category/value formulas:
#     [sheetname, first_row, first_col, last_row, last_col]
chart.add_series({
    'categories': [sheet_name, 1, 0, 3, 0],
    'values':     [sheet_name, 1, 1, 3, 1],
})
# configure the chart axes
chart.set_x_axis({'name': 'Index', 'position_axis': 'on_tick'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})
# place the chart on the worksheet
worksheet.insert_chart('E2', chart)
# output the excel file
writer.save()




#export as csv
export_csv = df.to_csv (r'C:\Users\CrazyGeeks\Desktop\dataframe.csv', index = None, header=True)

#export csv as gzip
df.to_csv('random_data.gz', compression='gzip', index=False)








for row in response.xpath('//*[@class="W(100%) M(0)"]//tbody//tr'):
    data = {
    'date' : row.xpath('td[1]//text()').extract_first(),
    'open': row.xpath('td[2]//text()').extract_first(),
    'high' : row.xpath('td[3]//text()').extract_first(),
    'low' : row.xpath('td[4]//text()').extract_first(),
    'close' : row.xpath('td[5]//text()').extract_first(),
    'adj' : row.xpath('td[6]//text()').extract_first(),
    'volume' : row.xpath('td[7]//text()').extract_first(),
    }
    print(name)