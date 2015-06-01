# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

# BBB, can be removed latest in Plone 6
deprecated(
    "Import from 'Products.CMFPlone.pas.groups' instead",
    NotSupported='Products.CMFPlone.pas.groups:NotSupported',
    GroupsTool='Products.CMFPlone.pas.groups:GroupsTool'
)
