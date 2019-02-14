## Goal of this page
- to extend the user model
- to have email as login
- to have email confirm

## AWS Cognito

At this point in time with 1.11 LTS there is 
- (unmaintained?) https://github.com/metametricsinc/django-warrant
- an non django python library callel https://github.com/capless/warrant

With 2.2 LTS to released in 2019 it might be best to wait

## Combining techniques from blog posts

- https://wsvincent.com/django-custom-user-model-tutorial/

- https://wsvincent.com/django-login-with-email-not-username/<br/>
  This one repeats the above tutorial so just scroll down to 'log out' and continue from there

https://pypi.org/project/django-simple-email-confirmation/

## DRF Needs

- Login - endpoint
- Logout - forget the token
- Reset - can survive with serverside form
- Signup - form that I must convert to an endpoint

