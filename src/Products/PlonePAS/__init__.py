# -*- coding: utf-8 -*-
from AccessControl.Permissions import add_user_folders
from Products.CMFCore.utils import ToolInit
from Products.PlonePAS.pas import patch_pas
from Products.PlonePAS.plugins import autogroup
from Products.PlonePAS.plugins import cookie_handler
from Products.PlonePAS.plugins import crumbler
from Products.PlonePAS.plugins import group
from Products.PlonePAS.plugins import local_role
from Products.PlonePAS.plugins import passwordpolicy
from Products.PlonePAS.plugins import property
from Products.PlonePAS.plugins import role
from Products.PlonePAS.plugins import ufactory
from Products.PlonePAS.plugins import user
from Products.PluggableAuthService import registerMultiPlugin
from zope.deferredimport import deprecated

########################################
# BBB, can be removed latest in Plone 6
deprecated(
    "Import from 'Products.CMFPlone.pas.groupdata' instead",
    GroupsDataTool='Products.CMFPlone.pas.groupdata:GroupDataTool'
)
deprecated(
    "Import from 'Products.CMFPlone.pas.groups' instead",
    GroupsTool='Products.CMFPlone.pas.groups:GroupsTool'
)
deprecated(
    "Import from 'Products.CMFPlone.pas.memberdata' instead",
    MemberDataTool='Products.CMFPlone.pas.groups:MemberDataTool',
)
deprecated(
    "Import from 'Products.CMFPlone.pas.membership' instead",
    MembershipTool='Products.CMFPlone.pas.membership:MembershipTool',
)


####################################
# monkey patch pas, the evil happens
patch_pas()

#################################
# new groups tool

#################################
# register plugins with pas
try:
    registerMultiPlugin(user.UserManager.meta_type)
    registerMultiPlugin(group.GroupManager.meta_type)
    registerMultiPlugin(role.GroupAwareRoleManager.meta_type)
    registerMultiPlugin(local_role.LocalRolesManager.meta_type)
    registerMultiPlugin(ufactory.PloneUserFactory.meta_type)
    registerMultiPlugin(property.ZODBMutablePropertyProvider.meta_type)
    registerMultiPlugin(crumbler.CookieCrumblingPlugin.meta_type)
    registerMultiPlugin(cookie_handler.ExtendedCookieAuthHelper.meta_type)
    registerMultiPlugin(autogroup.AutoGroup.meta_type)
    registerMultiPlugin(passwordpolicy.PasswordPolicyPlugin.meta_type)
except RuntimeError:
    # make refresh users happy
    pass


def initialize(context):

    context.registerClass(
        role.GroupAwareRoleManager,
        permission=add_user_folders,
        constructors=(
            role.manage_addGroupAwareRoleManagerForm,
            role.manage_addGroupAwareRoleManager),
        visibility=None
    )

    context.registerClass(
        user.UserManager,
        permission=add_user_folders,
        constructors=(
            user.manage_addUserManagerForm,
            user.manage_addUserManager),
        visibility=None
    )

    context.registerClass(
        group.GroupManager,
        permission=add_user_folders,
        constructors=(
            group.manage_addGroupManagerForm,
            group.manage_addGroupManager
        ),
        visibility=None
    )

    context.registerClass(
        ufactory.PloneUserFactory,
        permission=add_user_folders,
        constructors=(
            ufactory.manage_addPloneUserFactoryForm,
            ufactory.manage_addPloneUserFactory),
        visibility=None
    )

    context.registerClass(
        local_role.LocalRolesManager,
        permission=add_user_folders,
        constructors=(
            local_role.manage_addLocalRolesManagerForm,
            local_role.manage_addLocalRolesManager),
        visibility=None
    )

    context.registerClass(
        property.ZODBMutablePropertyProvider,
        permission=add_user_folders,
        constructors=(
            property.manage_addZODBMutablePropertyProviderForm,
            property.manage_addZODBMutablePropertyProvider),
        visibility=None
    )

    context.registerClass(
        crumbler.CookieCrumblingPlugin,
        permission=add_user_folders,
        constructors=(
            crumbler.manage_addCookieCrumblingPluginForm,
            crumbler.manage_addCookieCrumblingPlugin),
        visibility=None
    )

    context.registerClass(
        cookie_handler.ExtendedCookieAuthHelper,
        permission=add_user_folders,
        constructors=(
            cookie_handler.manage_addExtendedCookieAuthHelperForm,
            cookie_handler.manage_addExtendedCookieAuthHelper),
        visibility=None
    )

    context.registerClass(
        autogroup.AutoGroup,
        permission=add_user_folders,
        constructors=(
            autogroup.manage_addAutoGroupForm,
            autogroup.manage_addAutoGroup),
        visibility=None
    )

    context.registerClass(
        passwordpolicy.PasswordPolicyPlugin,
        permission=add_user_folders,
        constructors=(
            passwordpolicy.manage_addPasswordPolicyForm,
            passwordpolicy.manage_addPasswordPolicyPlugin
        ),
        visibility=None
    )
