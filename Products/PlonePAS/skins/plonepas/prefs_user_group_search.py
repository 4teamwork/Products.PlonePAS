## Script (Python) "prefs_valid_search_restriction.py"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=searchstring, restrict, return_form=None
##title=Valid Search Resriction
##
#MembershipTool.searchForMembers

# PAS does not currently implement a list-all feature
# for no searchstring, return empty list.

if not searchstring:
    return []


groups_tool = context.portal_groups
members_tool = context.portal_membership
retlist = []

if restrict != "groups":
    retlist = retlist + members_tool.searchForMembers(REQUEST=None, name=searchstring)
if restrict != "users":
    retlist = retlist + groups_tool.searchForGroups(REQUEST=None, name=searchstring)

# reorder retlist?
if return_form:
    context.REQUEST.RESPONSE.redirect( context.absolute_url() + '/' + return_form )
return retlist
