# config.py
DATABASES = {
    'postgresql': {
        'host': 'db_postgres',
        'port': 5432,
        'user': 'postgres',
        'password': 'postgres',
        'database': 'app_db'
    },

    'mysql': {
        'host': 'db_mysql',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'app_db'
    },

    'redis': {
        'host': 'redis',
        'port': 6379,
        'db': 0
    }
}
