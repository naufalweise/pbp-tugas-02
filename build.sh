python manage.py migrate
python manage.py loaddata initial_catalog_data.json
python manage.py loaddata initial_mywatchlist_data.json
python manage.py loaddata init-todolist-user.json
python manage.py loaddata init-todolist-task.json
python manage.py collectstatic --noinput