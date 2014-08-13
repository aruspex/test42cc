PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=fortytwo_test_task.settings django-admin.py models_count 2> $(date +"%d_%m_%Y").dat
