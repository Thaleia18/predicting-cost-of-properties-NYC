import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns


#####This data is about properties sold in New York City over 
#####a 12-month period from September 2016 to September 2017.

###I cleaned the data: remove duplicate data, clean null data, converted the categorical data in numerical data that I can use in the regression, and normalize the use of strings.


#######Data from
####https://www.kaggle.com/new-york-city/nyc-property-sales

sales_file_path = '../input/nyc-rolling-sales.csv'
sales_data = pd.read_csv(sales_file_path)
sales_data.columns =sales_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
sales_data.building_class_category=sales_data.building_class_category.str.strip().str.lower().str.replace(' ', '').str.replace('-', '_')
sales_data = sales_data.drop_duplicates(sales_data.columns, keep='last')
sales_data.describe() 
#print(sales_data.columns)

price=[]
land_square=[]
gross_square=[]
taxclass1=[]
taxclass2=[]
taxclass4=[]
Manhattan=[] #(1), 
Bronx=[] #(2), 
Brooklyn=[] #(3), 
Queens=[] #(4), 
State_Island=[]#5
buildingclass1=[]
buildingclass2=[]
buildingclass3=[]
buildingclass10=[]
buildingclass13=[]

#######YPU CAN DO THIS WITH GET DUMMIES
##########pd.get_dummies(data=data, columns=[''])
for i in range(len(sales_data.sale_price)):
    price.append(0) if sales_data.sale_price[i]==' -  ' else price.append(float(sales_data.sale_price[i]))
    land_square.append(0) if sales_data.land_square_feet[i]==' -  ' else land_square.append(float(sales_data.land_square_feet[i]))
    gross_square.append(0) if sales_data.gross_square_feet[i]==' -  ' else gross_square.append(float(sales_data.gross_square_feet[i]))
    taxclass1.append(1) if sales_data.tax_class_at_time_of_sale[i]==1 else taxclass1.append(0)
    taxclass2.append(1) if sales_data.tax_class_at_time_of_sale[i]==2 else taxclass2.append(0)
    taxclass4.append(1) if sales_data.tax_class_at_time_of_sale[i]==4 else taxclass4.append(0)    
    Manhattan.append(1) if sales_data.borough[i]==1 else Manhattan.append(0)    
    Bronx.append(1) if sales_data.borough[i]==2 else Bronx.append(0)    
    Brooklyn.append(1) if sales_data.borough[i]==3 else Brooklyn.append(0)    
    Queens.append(1) if sales_data.borough[i]==4 else Queens.append(0)    
    State_Island.append(1) if sales_data.borough[i]==5 else State_Island.append(0)    
    buildingclass1.append(1) if sales_data.building_class_category[i]=='01onefamilydwellings' else buildingclass1.append(0)
    buildingclass2.append(1) if sales_data.building_class_category[i]=='02twofamilydwellings' else buildingclass2.append(0)
    buildingclass3.append(1) if sales_data.building_class_category[i]=='03threefamilydwellings' else buildingclass3.append(0)
    buildingclass10.append(1) if sales_data.building_class_category[i]=='10coops_elevatorapartments' else buildingclass10.append(0)
    buildingclass13.append(1) if sales_data.building_class_category[i]=='13condos_elevatorapartments' else buildingclass13.append(0)

    
sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'])
sales_data.sale_date = [item.to_julian_date() for item in sales_data.sale_date] 

sales_data['price'] =price
sales_data['land_square'] =land_square
sales_data['gross_square'] =gross_square
sales_data['taxclass1']=taxclass1
sales_data['taxclass2']=taxclass2
sales_data['taxclass4']=taxclass4
sales_data['Manhattan']=Manhattan
sales_data['Bronx']=Bronx
sales_data['Brooklyn']=Brooklyn
sales_data['Queens']=Queens
sales_data['State_Island']=State_Island
sales_data['buildingclass1']=buildingclass1
sales_data['buildingclass2']=buildingclass2
sales_data['buildingclass3']=buildingclass3
sales_data['buildingclass10']=buildingclass10
sales_data['buildingclass13']=buildingclass13


#features=['borough','land_square', 'gross_square', 'year_built',
      # 'tax_class_at_time_of_sale','sale_date','price']
sales_data.describe()

#####I studied the building class categories, its relation with gross square and price.

#print(sales_data.building_class_category.unique())
plt.title(r'Building class category %')
(sales_data['building_class_category'].value_counts().head() / len(sales_data)).plot.bar()

ax1=sales_data[sales_data.building_class_category=='01onefamilydwellings'].plot.scatter(x='gross_square', y='price',c='red',title='Relation price vs gross square per building class',label='01onefamilydwellings')
sales_data[sales_data.building_class_category=='02twofamilydwellings'].plot.scatter(x='gross_square', y='price',c='black',label='02twofamilydwellings',ax=ax1)
sales_data[sales_data.building_class_category=='03threefamilydwellings'].plot.scatter(x='gross_square', y='price',c='blue',label='03threefamilydwellings',ax=ax1)
sales_data[sales_data.building_class_category=='10coops_elevatorapartments'].plot.scatter(x='gross_square', y='price',c='green',label='10coops_elevatorapartments',ax=ax1)
sales_data[sales_data.building_class_category=='13condos_elevatorapartments'].plot.scatter(x='gross_square', y='price',c='cyan',label='13condos_elevatorapartments',ax=ax1)
ax1.set_xlabel("Gross Square")
ax1.set_ylabel("Price")
ax1.set_ylim([.5,10**9])
ax1.set_xlim([-50,10**4.1])
ax1.set_yscale("log", nonposy='clip')

################I studied the borough categories, its relation with gross square and price.

plt.title(r'Borough %')
(sales_data['borough'].value_counts().head() / len(sales_data)).plot.bar()

#Manhattan #Bronx #Brooklyn
#Queens #State_Island=[]#5  

ax1=sales_data[sales_data.Manhattan==1].plot.scatter(x='gross_square', y='price',c='red',title='Relation price vs gross square per borough',label='Manhattan')
sales_data[sales_data.Bronx==1].plot.scatter(x='gross_square', y='price',c='black',label='Bronx',ax=ax1)
sales_data[sales_data.Brooklyn==1].plot.scatter(x='gross_square', y='price',c='blue',label='Brooklyn',ax=ax1)
sales_data[sales_data.Queens==1].plot.scatter(x='gross_square', y='price',c='green',label='State Island',ax=ax1)
sales_data[sales_data.State_Island==1].plot.scatter(x='gross_square', y='price',c='cyan',label='Queens',ax=ax1)
ax1.set_xlabel("Gross Square")
ax1.set_ylabel("Price")
ax1.set_ylim([.5,10**9])
ax1.set_xlim([-50,10**4.1])
ax1.set_yscale("log", nonposy='clip')
#ax1.set_xscale("log", nonposx='clip')

###I studied the tax class time categories at time of sale categories, its relation with gross square and price.
####I am not interested in the tax class at present time, that could cause at leakage of my regression.

plt.title(r'Tax Class at time of sale %')
(sales_data['tax_class_at_time_of_sale'].value_counts().head() / len(sales_data)).plot.bar()


ax1=sales_data[sales_data.taxclass1==1].plot.scatter(x='gross_square', y='price',c='red',title='Relation price vs gross square per tax class',label='Tax class1')
sales_data[sales_data.taxclass2==1].plot.scatter(x='gross_square', y='price',c='black',label='Tax class 2',ax=ax1)
sales_data[sales_data.taxclass4==1].plot.scatter(x='gross_square', y='price',c='blue',label='Tax Class 4',ax=ax1)
ax1.set_xlabel("Gross Square")
ax1.set_ylabel("Price")
ax1.set_ylim([.5,10**9])
ax1.set_xlim([-50,10**4.1])
ax1.set_yscale("log", nonposy='clip')
#ax1.set_xscale("log", nonposx='clip')

########3Istudied the sale prices. A lot of houses where sold by unreal prices ( 0−0− 10) , 
#######this means that the houses where not sold, they were transfer between owners. I used houses with prices over $100,000, because is a relistic price that wont mess my models.


plt.title(r'Price ')
plt.xscale('log')
plt.ylim((0,1050))
sales_data['price'].value_counts().sort_index().plot.line()

plt.title(r'Price: houses under $10000 ')
sales_data[sales_data['price'] < 10000]['price'].plot.hist()
plt.text(1500,20000,'mostly between \$0-\$100'
         'not really a sale and it will mess'
         'with my predictions',wrap=True)
:
plt.title(r'Price ')
plt.xscale('log')
plt.ylim((0,550))
sales_data[sales_data['price']>10000]['price'].value_counts().sort_index().plot.line()

plt.title(r' Year Built ')
plt.xlim((-10,2020.10))
#plt.ylim((0,1000.10))
plt.text(250,400,'uppss First human settlement 1609')
sales_data['year_built'].value_counts().sort_index().plot.line()

plt.title(r' Year Built ')
plt.xlim((1880,2020.10))
#plt.ylim((0,10.10))
sales_data[sales_data['year_built']>1880]['year_built'].value_counts().sort_index().plot.line()

ax1=sales_data[sales_data.Manhattan==1].plot.scatter(x='year_built', y='price',c='red',title='Relation price vs year built per borough',label='Manhattan')
sales_data[sales_data.Bronx==1].plot.scatter(x='year_built', y='price',c='black',label='Bronx',ax=ax1)
sales_data[sales_data.Brooklyn==1].plot.scatter(x='year_built', y='price',c='blue',label='Brooklyn',ax=ax1)
sales_data[sales_data.Queens==1].plot.scatter(x='year_built', y='price',c='green',label='State Island',ax=ax1)
sales_data[sales_data.State_Island==1].plot.scatter(x='year_built', y='price',c='cyan',label='Queens',ax=ax1)
ax1.set_xlabel("Year_built")
ax1.set_ylabel("Price")
ax1.set_ylim([.05,10**9.5])
ax1.set_xlim([1880,2050])
ax1.set_yscale("log", nonposy='clip')

#######33I changed the sale date to julian time and explored the data, I didnt see any pater in the sale date.

plt.title(r' Sale_date ')
#plt.xlim((-10,2020.10))
#plt.ylim((0,1000.10))
#plt.text(250,400,'uppss First human settlement 1609')
sales_data['sale_date'].value_counts().sort_index().plot.line()

####So finally, the features that I decided to use in my models: 'land_square' 'gross_square', 'year_built', 'taxclass1', 'taxclass2', 'taxclass4', 'Manhattan','Queens','Brooklyn','Bronx','State_Island', 'buildingclass1','buildingclass2','buildingclass3','buildingclass10', 'residential_units', 'commercial_units', 'total_units',

features=['land_square', 'gross_square', 'year_built',
          'taxclass1','taxclass2','taxclass4',
          'Manhattan','Queens','Brooklyn','Bronx','State_Island',
         'buildingclass1','buildingclass2','buildingclass3','buildingclass10',
          'residential_units', 'commercial_units', 'total_units',
       'price']
X=sales_data[features]
X=X[X.gross_square != 0]
X=X[X.land_square != 0]
X=X[X.price >100000]
X=X[X.year_built >1880]
X.describe()

##I transformed some data that was skewed to the right.

########I studied the correlations between the features and price:


######I will use four different methods for the regression: linear, lasso, ridge and random forest regression.


X['price']=np.log1p(X['price'])
X['land_square']=np.log1p(X['land_square'])
X['gross_square']=np.log1p(X['gross_square'])
X['year_built']=np.log1p(X['year_built'])

colormap = plt.cm.magma
plt.figure(figsize=(19,19))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
corr = X.corr()
sns.heatmap(corr,linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
corr['price'].sort_values(ascending=False)
