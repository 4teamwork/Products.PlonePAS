# -*- coding: utf-8 -*-
from zope.deferredimport import deprecated

# BBB, can be removed latest in Plone 6
deprecated(
    "Import from 'Products.CMFPlone.interfaces.membership' instead",
    IMembershipTool='Products.CMFPlone.interfaces.membership:IMembershipTool',
)
