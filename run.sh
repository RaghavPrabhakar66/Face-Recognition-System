cd facerec/frontend
npm run build

cd ..
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver 8080

cd ..
