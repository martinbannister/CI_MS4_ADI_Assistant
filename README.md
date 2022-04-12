# ADI Assistant

## Introduction
ADI Assistant is a web based app designed to help Approved Driving Instructors (ADIs) and Potential Driving Instructors (PDIs) run their business.  This initial release has basic features to store customer information and record income and expenses as "Transactions".

There is potential for many more features beyond this initial site.

## Code Institute Milestone 4 Project

[The Live Website](https://ci-ms4-adi-assistant.herokuapp.com/)

## Table of Contents

---

1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
   1. [Target Audience](#target-audience)
   2. [User Stories](#user-stories)
3. [Scope](#scope)
    1. [Design](#design)
    2. [Typography](#typeography)
5. [Features](#features)
6. [Technologies Used](#technologies-used)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)

## Project Goals
The main goeals of this project are:

### Site Owner
* To provide a valuable tool for Driving Instructors to run their business more easily.
* To provide the tool on a subscription basis to help fund it's further development.
### Site User
* To make storing and updating customer and financial information quick and easy.
* To be able to record information on the go without having to spend hours entering receipts.

    #### In Future
    * To integrate with feely available online calendering and contact services to leverage their capabilities without 'reinventing the wheel'.
    * To provide insight into pupils' performance based on their own progress record and test results.
    * Provide data based on the above that will highlight areas of developement for the ADI or PDI.
    * To provide a resource of publicly available information that ADI's and PDI's can contribute to based on their own experiences.

## Target Audience

* Approved Driving Instructors (ADIs)
* Potential Driving Instructors (PDIs)

## User Stories
As an ADI I want to be able to:

1. Easily sign up to the site so I can browse the features and decide if I want to subscribe.
2. Use my Google account to sign up to the site.
3. Add my customers(pupils) to the site.
4. Record financial transactions on the site and link them to a Customer where applicable.
5. Set my own accoutning code structure to record my transactions against for ease of producing financial records.

    In the future:
    * Import my contacts from Google Contacts
    * Download a list of my appointments(lessons) from Google Calendar, automatically link them to customers and add them to my Transactions as income.

As a PDI I want to be able to:

1. User all of the features of an ADI for free.

## Scope
### Design
#### Database
### Typography
## Features
## Technologies Used
## Testing

## Deployment

### Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
<br>![API keys](readme/misc/stripe_keys1.png)
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://ci-ms4-loverugby.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>![Webhook](readme/misc/stripe_keys2.png)
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting

There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

### Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "ci-ms4-rugby-shop"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
<br>![AWS Static](readme/misc/aws_static.png)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration
<br>![AWS CORS](readme/misc/aws_cors.png)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
<br>![AWS Bucket Policy](readme/misc/aws_bucket_policy.png)
8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "ci-ms4-rugby-shop"
12. Add the "AmazonS3FullAccess" policy permission for the user group
<br>![AWS Bucket Policy](readme/misc/aws_user_group.png)
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following
<br><code>"Resource": [</code>
<br><code>"arn:aws:s3:::ci-ms4-rugby-shop",</code>
<br><code>"arn:aws:s3:::ci-ms4-rugby-shop/*"</code>
<br><code>]</code>
16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
<br>![AWS Bucket Policy](readme/misc/aws_policy.png)
18. Go to Users and create a new user
19. Add the user to the user group ci-ms4-rugby-shop
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
22. The user is now created with the correct user group and policy
<br>![AWS Bucket Policy](readme/misc/aws_user.png)
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
<br>![AWS Settings](readme/misc/aws_settings.PNG)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 

### Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository pmeeny/CI-MS4-LoveRugby
3. Click the Code button and copy the HTTPS url, for example: https://github.com/pmeeny/CI-MS4-LoveRugby.git
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/pmeeny/CI-MS4-LoveRugby.git```
5. The repository will now be cloned in your workspace
6. Create an env.py file(do not commit this file to source control) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<br><code>import os</code>
<br><code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_PUBLIC_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_SECRET_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_WH_SECRET", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("AWS_ACCESS_KEY_ID", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("EMAIL_HOST_USER", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("EMAIL_HOST_PASS", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("USE_AWS", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("DATABASE_URL", TO BE ADDED BY USER)</code>
7. Some values for the environment variables above are described in different sections of this readme
8. Install the relevant packages as per the requirements.txt file
9. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
10. Ensure debug is set to true in the settings.py file for local development
11. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
12. Run "python3 manage.py showmigrations" to check the status of the migrations
13. Run "python3 manage.py migrate" to migrate the database
14. Run "python3 manage.py createsuperuser" to create a super/admin user
15. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
16. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
17. Run "python3 manage.py loaddata news.json" on the news file in news/fixtures to create the news items(optional)
18. Start the application by running <code>python3 manage.py runserver</code>
19. Open the application in a web browser, for example: http://127.0.0.1:8000/
## Heroku and Postgres Database
To deploy this application to Heroku, run the following steps.
1. Create an account at heroku.com
2. Create an app, give it a name for example ci-ms4-loverugby, and select a region
3. Under resources search for postgres, and add a Postgres database to the app
![Heroku Postgres](readme/misc/heroku_postgres.png)
    
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
5. Install the plugins dj-database-url and psycopg2-binary.
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn rugby_shop.wsgi:application for example
8. In the settings.py ensure the connection is to the Heroku postgres database
9. Ensure debug is set to false in the settings.py file
10. Add localhost/127.0.0.1, and ci-ms4-loverugby.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
15. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
16. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
17. From the CLI login to Heroku using the command heroku git:remote -a ci-ms4-loverugby
18. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-ms4-loverugby
19. Push the code to Heroku using the command git push heroku master
20. Ensure the following environment variables are set in Heroku
<br>![Heroku Env variables](readme/misc/heroku_env_variables.png)
21. Connect the app to GitHub, and enable automatic deploys from main
<br>![Heroku Postgres](readme/misc/heroku_deployment.png)
    
22. Click deploy to deploy your application to Heroku for the first time
23. Click on the link provided to access the application
24. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

## Credits
## Acknowledgements