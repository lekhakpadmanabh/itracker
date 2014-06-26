"""
# Programattically set up permissions:
# Not needed right now, but might need to add form
# if offering this app as a service


from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, User, Permission

itmod_ct = ContentType.objects.get(app_label='issuetracker', model='issuemoderation')
can_view = Permission(name='Can View', codename='can_view_itmod', content_type=itmod_ct)
can_view.save()
can_modify = Permission(name='Can Modify', codename='can_modify_itmod', content_type=itmod_ct)
can_modify.save()
g.permissions = [can_view, can_modify]
g.user_set.all()
# For example[<User: alice>, <User: bodhi>]
alice.has_perm('issuetracker.can_view_itmod')
# True
bodhi.has_perm('issuetracker.can_view_itmod')
# True
bob.has_perm('issuetracker.can_view_itmod')
# False

"""
