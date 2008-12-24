from zope.interface import Interface

class IEntity(Interface):
    """An entry in a entities directory. Can be a ONG, a students' group or whatever
    """

class IEntitiesDirectory(Interface):
    """A directory grouping one or more entities.
    """
