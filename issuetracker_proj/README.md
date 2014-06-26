###Issue Tracking webapp in Django

##Thoughts and ToDos: 

Working on:

1. add user
2. add permissions
3. template filters and such
4. pagination


Full list of ToDos..

* switch to class based views instead
* add pagination
* add search
* add superuser-group or moderator
* add subscriptions and notifications (in-site + email)
* search can be ajax enabled. good choice?
* simple aggregrate analytics
* use github's hooks to automatically log commits
* can use some model managers for the filters, but most of these should be done on the client side to save server resources

##Features: 

1. A user can submit an issue/bug/complaint
2. The issue has a 
   - title 
   - description
   - date
   - author 
   - status
   - priority
3. Each issue should be assigned to a person/team by a moderator

## Modifications to integrate into Meri Nagari's trunk

- add GIS metadata to model
- enable images
- celery for twitter bot integration
