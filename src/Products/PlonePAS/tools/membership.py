# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

# BBB, can be removed latest in Plone 6
deprecated(
    "Import from 'Products.CMFPlone.pas.membership' instead",
    MembershipTool='Products.CMFPlone.pas.membership:MembershipTool',
    default_portrait='Products.CMFPlone.pas.membership:default_portrait',
)
