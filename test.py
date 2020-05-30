import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost', 
								user='root', 
								password='password',  
								database='noteappdb', 
								charset='utf8mb4', 
								cursorclass=pymysql.cursors.DictCursor)

