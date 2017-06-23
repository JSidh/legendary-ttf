import quandl as q
import datetime
q.ApiConfig.api_key = 'xxxxxxxxxxxxxxxxxxxx' #specify API key

#1st function with API for Quandl
# A commodity energy trading company sales person would like to retrieve the ICE Endex Dutch
# TTF Gas Base Load Future prices starting from 2017-31-05.

print("Below is the ICE Endex Dutch TTF Gas Base Load Futures, Continuous Contract settle price (TFM2)")

def get_daily_settle_price(data):
    data = q.get(["CHRIS/ICE_TFM2.4"], start_date="2017-05-31")
    return data
print(get_daily_settle_price(float))

#2nd function with API for Quandl
# The sales person would like to compute a daily calculation on the ICE Endex Dutch TTF Gas
# Base Load Futures. This is what has been agreed with the counterparty 'XXXX'
print("Below is the result of the calculaton for the 'XXXX' settlement using TFM2 prices above - to the power of 1.0256")

def pricing_with_XXXX(x):
     return x**1.0256
print(pricing_with_XXXX(get_daily_settle_price(float)))

#3rd function with API for Quandl
#The salesperson would also like to receive the last settle prices of the month for ICE Endex Dutch
#TTF Base Load Futures, starting from 2017-02-28. This is for forseeable structured products with counterparties.

print("Below is the ICE Endex Dutch TTF Gas Base Load Futures, Continuous Contract settle monthly settle price (TFM2)")

def get_monthly_settle_price(price):
    price = q.get("CHRIS/ICE_TFM2.4", collapse="monthly", start_date="2017-02-28")
    return price
print(get_monthly_settle_price(float))


