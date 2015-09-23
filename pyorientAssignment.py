import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "474F1CBE549F9E33FC8A0793C7819485072DAE07A4B704138010F28A28B69DF9")
db_name = "soufun"
db_username = "admin"
db_password = "admin"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit()

lat1 = 22.536870
lat2 = 22.553872

lng1 = 114.026551
lng2 = 114.060868

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'

# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.

for record in records:
	print record.price


s = 0
for record in records:
    s += record.price
    
    
miNum = 10000000   
for record in records:
    if record.price < miNum:
        miNum = record.price

maNum = 50
for record in records:
    if record.price > maNum:
        maNum = record.price      
    

# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: '+ str(miNum)
print 'max price: '+ str(maNum) 
print 'average price: '+ str(s/numListings)

client.db_close()