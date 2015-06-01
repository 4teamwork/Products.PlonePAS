# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

# BBB, can be removed latest in Plone 6
deprecated(
    "Import from 'Products.CMFPlone.pas.groupdata' instead",
    GroupDataTool='Products.CMFPlone.pas.groupdata:GroupDataTool',
    GroupData='Products.CMFPlone.pas.groupdata:GroupData'
)
