# littlelemon
 
## Steps to run the app

### 1. Install `pipenv`

```bash
pip install pipenv
```

### 2. Create a `.env` file in the root folder

```bash
# .env
DATABASE = YOUR_MYSQL_DATABASE_NAME
USER     = YOUR_USERNAME            
PASSWORD = YOUR_MYSQL_PASSWORD
HOST     = localhost                 
PORT     = 3306
```

### 3. Install dependencies

```bash
pipenv install
```

### 4. Make migrations

```bash
python manage.py makemigrations
```

### 5. Migrate

```bash
python manage.py migrate
```

### 6. Run the app

```bash
python manage.py runserver
```

### 7. To create super user

```bash
python manage.py createsuperuser
```

### 8. To create menu items

```Inside the django-admin panel, create new menu items eg:- 
    [
    {
        "title": "Chocolate Coffee",
        "price": "5.75",
        "inventory": 10
    },
    {
        "title": "Tea",
        "price": "2.45",
        "inventory": 1
    },
    {
        "title": "Bread",
        "price": "3.50",
        "inventory": 20
    }
]
```

### API paths

```
/api/bookings
/api/menu
```

### To run tests

```bash
python manage.py test tests
```