## Script (Python) "prefs_group_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=addname=None, groupname=None
##title=Edit user
##

# Changes:
#  remove empty-string argument from addGroup.

from Products.PythonScripts.standard import url_quote

REQUEST=context.REQUEST

if addname:
    context.portal_groups.addGroup(addname,(),())
    group=context.portal_groups.getGroupById(addname)
else:
    group=context.portal_groups.getGroupById(groupname)

processed={}
for id, property in context.portal_groupdata.propertyItems():
    processed[id]=REQUEST.get(id, None)

msg = 'Changes made.'

if group:
    # for what reason ever, the very first group created does not exist
    group.setGroupProperties(processed)
else:
    msg = 'No Changes made.'

url='%s?%s=%s' % (context.prefs_groups_overview.absolute_url(),
    url_quote('portal_status_message'),
    url_quote(msg))

return REQUEST.RESPONSE.redirect(url)
