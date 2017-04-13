# Displaying top 10 brands
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
data=pd.read_csv("amazon_data_pandas.csv",encoding='utf-8')
data.columns = ['index','ProductName','BrandName','Price','Rating','Reviews','ReviewVotes','sentiment_compound_polarity','sentiment_neutral','sentiment_negative','sentiment_pos','sentiment_type']

pivot = pd.pivot_table(data,
            values = ['sentiment_compound_polarity'],
            index =  ['BrandName'],
                       columns= [],
                       aggfunc=[np.sum, np.mean, np.count_nonzero, np.std], 
                       margins=True, fill_value=0).sort_values(by=('count_nonzero', 'sentiment_compound_polarity'), ascending=False).fillna('')
top_10_brands = pivot.reindex().head(n=11)

top_10_brands.to_csv('top10brands.csv',sep=',',encoding='utf-8')
print top_10_brands