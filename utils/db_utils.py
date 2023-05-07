from sqlalchemy import create_engine

def make_db_conn():
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'rohit'
    db = 'LSM'
    # url ='mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}?unix_socket=/var/run/mysqld/mysqld.sock'.format(user=user, password=password, host=host, port=port, db=db)
    url ="mysql+mysqlconnector://root:rohit@localhost:3306/LSM?unix_socket=/var/run/mysqld/mysqld.sock"

    return url

engine = create_engine(make_db_conn(),pool_size=10,max_overflow=20)
print("engine: ", engine)