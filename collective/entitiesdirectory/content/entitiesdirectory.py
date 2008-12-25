# CMF and Zope imports
from Products.CMFCore import permissions
from zope.interface import implements

# Archetypes imports
from Products.Archetypes import atapi

# Product imports
from collective.entitiesdirectory.config import PROJECTNAME
from collective.entitiesdirectory.interfaces import IEntitiesDirectory


# Schema definition
EntitiesDirectorySchema = atapi.BaseFolderSchema.copy()

class EntitiesDirectory(atapi.BaseFolder):
    """An Archetype for an EntitiesDirectory application
    """
    implements(IEntitiesDirectory)

    schema = EntitiesDirectorySchema

    _at_rename_after_creation = True

atapi.registerType(EntitiesDirectory, PROJECTNAME)
