# Recruitment assistant
The app helps to identify potential matching profiles against a job for a recruiter or company.


`heroku create <app_name>`
`heroku addons:create heroku-postgresql:hobby-dev -a <app_name>`
`heroku git:remote -a <app_name>`
`heroku config:set DEBUG_COLLECTSTATIC=1`
`heroku config:set DISABLE_COLLECTSTATIC=1`
`git push heroku main`
`heroku run python manage.py migrate`
`heroku run python manage.py createsuperuser`