# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

# BBB, can be removed latest in Plone 6
deprecated(
    "Import from 'Products.CMFPlone.pas.memberdata' instead",
    MemberDataTool='Products.CMFPlone.pas.memberdata:MemberDataTool',
    MemberData='Products.CMFPlone.pas.memberdata:MemberData'
)
