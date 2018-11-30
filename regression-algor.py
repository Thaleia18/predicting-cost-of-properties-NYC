##########
####### LINEAR REGRESSION ####################################################################################################
########333

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error

#X= np.log1p(X)
y = X['price']
X2 = X.drop(['price'], axis=1).values 
train_X, val_X, train_y, val_y = train_test_split(X2, y, random_state = 0)

model = LinearRegression()
model.fit(train_X, train_y)
y_pred = model.predict(val_X) 

print('r2',model.score(val_X, val_y))####r2 score
print('rmse',(mean_squared_error(val_y, y_pred))**0.5)

##########
####### RIDGE REGRESSION ####################################################################################################
########333

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error

y = X['price']
X2 = X.drop(['price'], axis=1).values 
train_X, val_X, train_y, val_y = train_test_split(X2, y, random_state = 0)

alpha_ridge = [0.000001,0.0001,.001,1]
for item in alpha_ridge:
    modelt = Ridge(alpha=item,copy_X=True, fit_intercept=True, max_iter=None,
          normalize=False, random_state=None, solver='auto', tol=0.001)
    modelt.fit(train_X, train_y)
    y_predt = modelt.predict(val_X) 

   # print(item,'r2',modelt.score(val_X, val_y))####r2 score
    #print('rmse',(mean_squared_error(val_y, y_predt))**0.5)
   # print('explained variance',explained_variance_score(val_y,y_predt))
    
model2 = Ridge(alpha=0.000001,copy_X=True, fit_intercept=True, max_iter=None,
          normalize=False, random_state=None, solver='auto', tol=0.001)
model2.fit(train_X, train_y)
y_pred2 = model2.predict(val_X) 

print('r2',model2.score(val_X, val_y))####r2 score
print('rmse',(mean_squared_error(val_y, y_pred2))**0.5)

##########
####### LASSO REGRESSION ####################################################################################################
########333

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error

y = X['price']
X2 = X.drop(['price'], axis=1).values 
train_X, val_X, train_y, val_y = train_test_split(X2, y, random_state = 0)

alpha_ridge = [0.000001,0.0001,.001,1]
for item in alpha_ridge:
    modelt = linear_model.Lasso(alpha=item, copy_X=True, fit_intercept=True, max_iter=1000,
   normalize=False, positive=False, precompute=False, random_state=None,
   selection='cyclic', tol=0.0001, warm_start=False)
    modelt.fit(train_X, train_y)
    y_predt = modelt.predict(val_X) 

   # print(item,'r2',modelt.score(val_X, val_y))####r2 score
   # print('rmse',(mean_squared_error(val_y, y_predt))**0.5)
  #  print('explained variance',explained_variance_score(val_y,y_predt))
    
model3 = linear_model.Lasso(alpha=0.000005, copy_X=True, fit_intercept=True, max_iter=1000,
   normalize=False, positive=False, precompute=False, random_state=None,
   selection='cyclic', tol=0.0001, warm_start=False)
                            
model3.fit(train_X, train_y)
y_pred3 = model3.predict(val_X) 

print('r2',model3.score(val_X, val_y))####r2 score
print('rmse',(mean_squared_error(val_y, y_pred3))**0.5)

##########
####### RANDOM FOREST REGRESSION ####################################################################################################
########333

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error

y = X['price']
X2 = X.drop(['price'], axis=1).values 
train_X, val_X, train_y, val_y = train_test_split(X2, y, random_state = 0)


model4 = RandomForestRegressor()
model4.fit(train_X, train_y)
y_pred4 = model4.predict(val_X) 

print('r2',model4.score(val_X, val_y))####r2 score
print('rmse',(mean_squared_error(val_y, y_pred4))**0.5)


#########3
##########Results for the different regression:
########

linear: r2 0.6111805534821673 rmse 0.5340183237978753
Ridge: r2 0.6111805532023231 rmse 0.5340183239900492
lasso r2 0.6113140862445937 rmse 0.5339266166236538
Random forest regression: r2 0.625753188947449 rmse 0.5239154727330908
The best score is for the random forest.


##########
####### PLOTS RESULTS ####################################################################################################
########333
import matplotlib.pyplot as plt

# plot a line, a perfit predict would all fall on this line
ind = np.linspace(10,21,1000)
plt.xlabel('Test Data')
plt.ylabel('Predicted DataPrice') 
#plt.xlim(-100,10000000)
#plt.ylim(-100,10000000)
plt.plot(ind, ind,'-')
plt.plot(val_y, y_pred, '.',label='Linear Regression')
plt.plot(val_y, y_pred2, 'o',label='Ridge Regression')
plt.plot(val_y, y_pred3, '*',label='Lasso Regression')
plt.plot(val_y, y_pred4, '.',label='Random Forest Regression')
plt.legend(loc='lower right')
plt.show()

import matplotlib.pyplot as plt
import random
#select random data to show
i=random.randint(1,len(val_y)-101)
ind = np.linspace(0, 100,100)

plt.xlabel('Data index')
plt.ylabel('Price in thousands of $') 

plt.plot(ind, np.expm1(val_y[i:i+100])/1000,'-', linewidth=2.2,label='Test data' )
plt.plot(ind, np.expm1(y_pred[i:i+100])/1000, '--',linewidth=1.4,label='Linear Regression')
plt.plot(ind, np.expm1(y_pred2[i:i+100])/1000, '-.',linewidth=1.3,label='Ridge Regression')
plt.plot(ind, np.expm1(y_pred3[i:i+100])/1000, '--',linewidth=1.2,label='Lasso Regression')
plt.plot(ind, np.expm1(y_pred4[i:i+100])/1000, '-.',linewidth=1.2,label='Random Forest Regression')
plt.legend(loc='upper right')
plt.xlim(-2,112)
plt.show()
