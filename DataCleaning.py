import pandas as pd 
import csv 

df = pd.read_csv("./final.csv")
#It will give us the number of rows and number of columns 
#df.shape()
#expected output(4284,85)

#command to delete the column 
del df["hyperlink"]

#renaming the column 
df = df.rename({
    'pl_hostname' : 'solar_system_name',

},axis = 'columns')

df.to_csv("DataCleaned.csv")

