import numpy as np
import pandas as pd


df=pd.read_csv("c:/Users/dell/OneDrive/Documents/Data science projects/E-commerce data/ecommerce_dirty_dataset.csv")
com=df.copy()
#print(com.isnull().sum())


#cleaning order_id , customer_id and customer _name
com[com.select_dtypes(include='object').columns] = \
com.select_dtypes(include='object').astype('string')

cols1=['order_id','customer_id','customer_name']
for cols in cols1:
    com[cols]=com[cols].fillna(com[cols].mode()[0])

#print(com.isnull().sum())

#cleaning age coloum (keeping age between 1 to 100)
# com['age']=com['age'].astype('string')

com= com[(com['age'] >= 1) & (com['age'] <= 100)]
com['age']=com['age'].fillna(com['age'].median())        
#print(com['age'].to_string())
#print(com['age'].isnull().sum())


#cleaning Gender

com['gender'] = com['gender'].str.upper()

com['gender'] = com['gender'].replace({
    'F': 'FEMALE',
    'M': 'MALE',
    'UNKNOWN': com['gender'].mode()[0],
    'ERROR': com['gender'].mode()[0]
})

com['gender'] = com['gender'].fillna(com['gender'].mode()[0])

#cleaning email

com['email']=com['email'].fillna("noemail@example.com")
com.loc[com['email']=='none','email']='noemail@example.com'
#print(com['email'].isnull().sum())


#cleaning phone

#com['phone']=pd.to_numeric(com['phone'],errors='coerce')
com['phone'] = com['phone'].str.replace('-', '', regex=False)
com['phone']=com['phone'].fillna("9999911111")
com.loc[com['phone'].astype(str).str.len() < 10, 'phone'] = '9999911111'
com.loc[com['phone'].astype(str).str.len() > 10, 'phone'] = '9999911111'
com['phone']=com['phone'].replace({'0000000000':'9999911111'})

# for i in com['phone']:
#     print(i)

# print(com['phone'].isnull().sum())
# print(com['phone'].head(30))

# city cleaning

com['city']=com['city'].str.strip().str.lower().fillna(com['city'].mode()[0])
com.loc[com['city'] == 'Jaipur', 'city'] = 'jaipur'

com.loc[com['state'] == 'florida', 'city'] = 'florida'
com.loc[com['state'] == 'california', 'city'] = 'california'
com.loc[com['state'] == 'punjab', 'city'] = 'punjab'
com.loc[com['state'] == 'victoria', 'city'] = 'victoria'
com.loc[com['state'] == 'texas', 'city'] = 'texas'


# print(com['city'].unique())
# print(com['city'].value_counts())
# print(com['city'].isnull().sum())




# state
com['state']=com['state'].str.strip().str.lower().fillna(com['state'].mode()[0])
com.loc[com['city'] == 'sydney', 'state'] = 'nsw'
com.loc[com['city'] == 'london', 'state'] = 'london'
com.loc[com['city'] == 'tokoyo', 'state'] = 'tokoyo'
com.loc[com['city'] == 'lagos', 'state'] = 'lagos state'
com.loc[com['city'] == 'singapore', 'state'] = 'singapore'
com.loc[com['city'] == 'new york', 'state'] = 'new york'
com.loc[com['city'] == 'toronto', 'state'] = 'ontario'
com.loc[com['city'] == 'dubai', 'state'] = 'dubai'
com.loc[com['city'] == 'berlin', 'state'] = 'germany'
com.loc[com['city'] == 'paris', 'state'] = 'ile-de-france'

# indian cities

com.loc[com['city'] == 'kolkata', 'state'] = 'west bengal'
com.loc[com['city'] == 'hyderabad', 'state'] = 'telangana'
com.loc[com['city'] == 'lucknow', 'state'] = 'uttar pradesh'
com.loc[com['city'] == 'chennai', 'state'] = 'tamil nadu'
com.loc[com['city'] == 'ahemdabad', 'state'] = 'gujrat'
com.loc[com['city'] == 'mumbai', 'state'] = 'maharashtra'
com.loc[com['city'] == 'pune', 'state'] = 'gujrat'
com.loc[com['city'] == 'jaipur', 'state'] = 'rajasthan'
com.loc[com['city'] == 'banglore', 'state'] = 'karnataka'
com.loc[com['city'] == 'delhi', 'state'] = 'delhi'



com.loc[com['state'] == 'Uttar Pradesh', 'state']='uttar pradesh'
# print(com['state'].unique())
# print(com['state'].value_counts())
# print(com['state'].isnull().sum())

# state=pd.DataFrame(com['state'])
# city=pd.DataFrame(com['city'])
# addr=state.join(city)
# print(addr.to_string())

#  country cleaning

com['country']=com['country'].str.strip().str.lower().fillna(com['country'].mode()[0])
com.loc[com['country'] == 'u.s.a','country']='usa'
com.loc[com['country'] == 'us','country']='usa'
com.loc[com['country'] == 'united states', 'country']='usa'
com.loc[com['country']== 'in','country']='india'
com.loc[com['country']== 'India','country']='india'

# dividing countries

com.loc[com['state']  == 'florida', 'country']='australia'
com.loc[com['state'] == 'california', 'country']='usa'
com.loc[com['state'] == 'punjab', 'country']='india'
com.loc[com['state']  == 'victoria', 'country']='australia'
com.loc[com['state']  == 'texas', 'country']='usa'
com.loc[com['state'] == 'west bengal', 'country']='india'
com.loc[com['state'] == 'telangana', 'country']='india'
com.loc[com['state'] == 'tamil nadu', 'country']='india'
com.loc[com['state'] == 'rajasthan', 'country']='india'
com.loc[com['state'] == 'maharashtra', 'country']='india'
com.loc[com['state'] == 'gujrat', 'country']='india'
com.loc[com['state'] == 'new york', 'country']='usa'
com.loc[com['state'] == 'lagos state', 'country']='nigeria'
com.loc[com['state'] == 'uttar pradesh', 'country']='india'
com.loc[com['state'] == 'tokoyo', 'country']='japan'
com.loc[com['state'] == 'ile-de-france', 'country']='france'
com.loc[com['state'] == 'karnataka', 'country']='india'
com.loc[com['state'] == 'delhi', 'country']='india'
com.loc[com['state'] == 'ontario', 'country']='india'
com.loc[com['state'] == 'germany','country']='germany'
com.loc[com['state'] == 'dubai', 'country']='uae'
com.loc[com['state'] == 'singapore', 'country']='singapore'
com.loc[com['state'] == 'west bengal', 'country']='india'
com.loc[com['state'] == 'nsw', 'country']='australia'
com.loc[com['state'] == 'uk', 'state']='uk'

# print(com['country'].unique())
# print(com['country'].value_counts())
# print(com['country'].isnull().sum())

# cleaning pincode

com['pincode']=com['pincode'].fillna(com['pincode'].mode()[0])
com['pincode']=com['pincode'].replace({0.0:123456})
# print(com['pincode'].isnull().sum())
# print(com['pincode'].head(10))



# cleaning product name and category

value=['product_name','category']
for val in value:
    com[val]=com[val].fillna(com[val].mode()[0])
# print(com['category'].isnull().sum())
# print(com['product_name'].isnull().sum())

# cleaning quantity,unit_price_inr,discount_price

com['quantity'] = com['quantity'].fillna(com['quantity'].mode()[0]).astype(int)

com['unit_price_inr'] = com['unit_price_inr'].fillna(com['unit_price_inr'].mode()[0]).astype(int)

com['discount_percent'] = com['discount_percent'].fillna(com['discount_percent'].mode()[0]).astype(int)

com['total_price_inr'] = com['total_price_inr'].fillna(
    com['quantity'] * com['unit_price_inr'] *
    (1 - com['discount_percent'] / 100)      
)

com.loc[com['total_price_inr'] <= 0, 'total_price_inr'] = np.nan
com['total_price_inr'] = com['total_price_inr'].fillna(com['total_price_inr'].mode()[0])
com['total_price_inr'] = com['total_price_inr'].astype(int)


# print(com['discount_percent'].isnull().sum())
# print(com['unit_price_inr'].isnull().sum())
# print(com['quantity'].isnull().sum())
# print(com['quantity'].dtype)


# cleaning dates

com['order_date']=pd.to_datetime(com["order_date"], errors="coerce")
com["order_date"]=com["order_date"].fillna(com['order_date'].mode()[0])
com["order_date"]=com["order_date"].dt.strftime("%d-%m-%Y")

com['delivery_date']=pd.to_datetime(com["delivery_date"], errors="coerce")
com['delivery_date']=com["delivery_date"].fillna(com["delivery_date"].mode()[0])
com['delivery_date']=com['delivery_date'].dt.strftime("%d-%m-%Y")

# cleaning payment_method

com['payment_method']=com['payment_method'].str.lower().fillna(com['payment_method'].mode()[0])
com.loc[com['payment_method']=='Debit Card','payment_method']='debit card'
# print(com['payment_method'].value_counts())


# cleaning order_status

com['order_status']=com['order_status'].str.lower().str.strip().fillna(com['order_status'].mode()[0])
com.loc[com['order_status']=='Returned','order_status']='returned'
com.loc[com['order_status']=='canceled','order_status']='cancelled'
com.loc[com['order_status']=='processing','order_status']='processing'
# print(com['order_status'].unique()) 

# print(com['order_status'].value_counts())

# cleaning seller,rating,review_text,return_requested,loyalty_points

data=['seller','rating','review_text','return_requested','loyalty_points']
for n in data:
    com[n]=com[n].fillna(com[n].mode()[0])
com['seller']=com['seller'].str.strip()
com.loc[com['seller']=='FASHION HUB','seller']='FashionHub'  
com.loc[com['seller']=='techmart','seller']='TechMart' 
com.loc[com['seller']=='Book World','seller']='BookWorld' 

com['review_text']=com['review_text'].str.strip()
com.loc[com['review_text']=='na','review_text']='Average quality'
com.loc[com['review_text']=='.','review_text']='Average quality'

com['return_requested']=com['return_requested'].str.strip()
com.loc[com['return_requested']=='NO','return_requested']='No'
com.loc[com['return_requested']=='yes','return_requested']='Yes'

com.loc[com['loyalty_points']<0,'loyalty_points']=np.nan
com['loyalty_points']=com['loyalty_points'].fillna(com['loyalty_points'].mean())

# print(com['return_requested'].unique())  
# print(com['return_requested'].value_counts())    

# com.to_csv("c:/Users/dell/OneDrive/Documents/Data science projects/E-commerce data/ecommerce_dirty_dataset_cleaned.csv", index=False) 
# print(com.isnull().sum())