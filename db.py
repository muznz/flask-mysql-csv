from main import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Moncks@224'
app.config['MYSQL_DATABASE_DB'] = 'books_collection'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)