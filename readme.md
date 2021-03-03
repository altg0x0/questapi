This application requires django, django-rest-framework, and drf-nested-routers.
It was tested using python 3.9.1, django 3.1.7, and drf 3.12.2.

To test, clone this repo into workdir. Then from this directory:

`python manage.py makemigrations`

`python manage.py migrate`

Create admin user with

`python manage.py createsuperuser --email admin@example.com --username admin`

Finally, run the server using

`python manage.py runserver`
_________________
**Short API reference**
___
`/questionnaires`:

GET: get questionnaires. If the user is admin, receive all the questionnaires,
otherwise only those that are active right now (startTime < now < endTime).

POST: if the user is admin, add a new questionnaire. Otherwise, nothing.

`/questionnaires/id` where `id` is an integer :
GET questionnaire by the id. PUT, PATCH, DELETE to change the questionnaire if you are admin.

Example of parameters, common for last two endpoints:
`{"endDateTime": "2030-11-11T10:00:00",
"startDateTime": "2021-01-02T17:37:19.851979",
"title": "Title of questionnaire",
"description": "Simple questionnaire"}`

___
`questionnaires/id/questions/`:

GET questions belonging to the questionnaire, POST new questions.

`questionnaires/id/questions/questionId`:

Similarly, GET question info, PUT, PATCH, DELETE questions if you are admin.
Example of params: `        
{
"questionText": \"What is your name?\",
"questionType": \"TEXT_ANSWER\",
"orderNumber": 4,
"answer": "John"
}
`. `"answer"` is used as the default answer, `orderNumber` is used for sorting questions in questionnaires,
`questionType` is in `[TEXT_ANSWER, MULTIPLE_CHOICE, MULTIPLE_RESPONSE]`
___
`questionnaire_instances`:

POST to send a finished questionnaire. `userId` identifies the user, 0 is considered anonymous
(only admins can view anonymous responses).
GET with the query parameter `uid=4` (`questionnaire_instances/?uid=4`) to get questionnaires finished 
by the user with id=4.

Example of params: `        {
"answers": "{1: \"yes\", 2: \"no\"}",
"userId": 1,
"questionnaireId": 2
}
___
`api-auth/`:

Auth in app as admin (standard DRF auth)