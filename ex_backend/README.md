# Webapp

A proof of concept for communicating between SolidWorks, a database, and a web browser.

## Architecture

// TODO



## Resources

Tutorial for configuring django-react: [Link](https://dev.to/nagatodev/how-to-connect-django-to-reactjs-1a71)

To develop you probably want to run both the django app and the react frontend:

* from `ex_backend/`: `python manage.py runserver`
* from `ex_backend/frontend/`: `npm run start`

> You do not _need_ to run `npm build` to see changes. If you run both servers; direct the browser at the port for the npm server and it should redirect the api requests to django automatically. Both dev-servers update automatically when the relevant files are updated.

