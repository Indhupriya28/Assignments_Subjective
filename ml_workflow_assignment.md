TASK 1: 

Label: repeat_purchase_flag 
Leaky feature: discount_used_on_repeat_order

customer_id ==> This can be dropped, because it wont help in  prediction
order_count_last_90d	=> Feature , this gives the past purchase details which helps in prediction
avg_order_value	=> Feature , provide avaerage value of the purchased value
days_since_last_order	Days elapsed => Feature , time gap of the recent purchase till now
repeat_purchase_flag	=> Label , gives the result whether customer purchase /not
discount_used_on_repeat_orde => Leaky feature , because it depends on the predicted value. can't be used as feature

===============================================================================================================================

TASK 2:

1. Data Audit and analysis : Understanding the data , its pattern and data cleaning is needed before proceeding with model creation. Identifying the outliers/skewers and cleaning them.
2. Splitting of data : Splitting training data and test data necessary in building ML model. THis helps in prevents overfitting and false prediction,
                       which will helps in increase the performance.
