Read in the CSV and bring it into a PD DataFrame

inspect the value_counts of each column

REPLACE ? WITH NAN
sqft_basement should not have: 
?
replace ? with np.nan


DROP NA ROWS
investigate isna.sum() for each column to discover any rogue values.

dropna for sqft_basement and view


REMOVE COLUMNS
Because waterfront has less than 1% true. Lets just drop the waterfront column since it doesn't really present any analytical weight. 

year.renovated.isna.sum = 3742.
removing these rows would result in ~18% of the data lost.
~81% of the data shows houses have NOT BEEN RENOVATED. 
So dropping this column has little affect on the estimation of the sales price. 

So lets drop waterfront and renovated.


CHECK DUPLICATES
Now we should check for duplicates.
There are no duplicates.