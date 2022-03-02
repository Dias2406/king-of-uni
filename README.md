# King of University (Prototype)

*King of University is a free web application developped in Django. Players compete to capture territories around campus to earn points and reach the top of the leaderboard.*

## Prerequisites:
The project work on Python3 programming language. You will need to install python3 interpreter. To install Python3 follow the link below:
https://www.python.org/downloads/

## Installations
In order to start using the project, you will need to activate virtual environment. Navigate to the king-of-uni folder using `cd` and activate virtual environment:

`source venv/bin/activate`
## Developper Manual:
Before running the project you need to start Cloud SQL Auth proxy, in seperate terminal run:

`./cloud_sql_proxy -instances="king-342719:europe-west2:game"=tcp:5432`

And set the Project ID locally:

`export GOOGLE_CLOUD_PROJECT=king-342719`
`export USE_CLOUD_SQL_AUTH_PROXY=true`

To run the app use:

`python manage.py runserver`

On a web browser head to http://localhost:8000 to view the website.
<br>

## Future Development:
- Implement Teams
- Improve the scoring sytem
- Add a team leaderboard 
- Add more capturable locations 
- Fine-tuning of capturable locations
<br>
<br>
___

**Authors: Group 18**
 
