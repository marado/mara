"""
Talker service
"""
import cletus
service = cletus.Service('talker')

# Add user to client events
from cletus import events
from cletus.contrib.commands import CommandEvent
from cletus.contrib.users import event_add_user
service.listen(events.Connect, event_add_user)
service.listen(events.Disconnect, event_add_user)
service.listen(events.Receive, event_add_user)
service.listen(CommandEvent, event_add_user)



# Set up a filter for write_all to filter to users who have logged in,
# otherwise they'll see things on the login prompt
def filter_to_users(service, clients, **kwargs):
    return (c for c in clients if getattr(c, 'user', None))
service.filter_all = filter_to_users