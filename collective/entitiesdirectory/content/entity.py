# CMF and Zope imports
from Products.CMFCore import permissions
from zope.interface import implements

# Archetypes imports
from Products.Archetypes import atapi

# Product imports
from collective.entitiesdirectory.config import PROJECTNAME
from collective.entitiesdirectory.interfaces import IEntity


# Schema definition
EntitySchema = atapi.BaseSchema.copy() +  atapi.Schema((

    atapi.TextField('slogan',
              searchable = 1,
              required = 1,
              storage = atapi.AttributeStorage(),
              widget=atapi.TextAreaWidget(description="Slogan", label="Slogan"),
              #storage = atapi.AnnotationStorage(), # PREGUNTAR
              ),
    atapi.ImageField('image',
              max_size = (768,768),
              languageIndependent = True,
              storage = atapi.AttributeStorage(),
              #storage = atapi.AnnotationStorage(),
              sizes= {'large'   : (768, 768),
                'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (128, 128),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
               },
              ),
    atapi.TextField('text',
              searchable = 1,
              required = 1,
              #storage = AnnotationStorage(), # PREGUNTAR
              validators = ('isTidyHtmlWithCleanup',),
              allowable_content_types = ('text/plain',
                                       'text/structured',
                                       'text/html',),
              default_output_type = 'text/x-html-safe',
              widget = atapi.RichWidget(label = 'Text'),
              ),
    atapi.StringField('webSite',
              validators = ('isURL',),
              ),
    atapi.StringField('email',
                validators = ('isEmail',),
                ),
    atapi.StringField('phone',
              maxlength = 20,
              size = 20,
              ),
    atapi.StringField('mobile',
              maxlength = 20,
              size = 20,
              ),
    atapi.StringField('fax',
              maxlength = 20,
              size = 20,
              ),
    atapi.StringField('address',
              required = True,
              ),
    atapi.StringField('zip',
              maxlength = 9,
              size = 9,
              ),
    atapi.StringField('city',
              searchable = 1,
              required = 1,
              ),
    atapi.StringField('province',
              searchable = 1,
              required = 1,
              ),
    atapi.StringField('country',
              searchable = 1,
              required = 1,
              ),
    atapi.StringField('territorialScope',
              searchable = 1,
              required = 1,
              ),
    atapi.StringField('topics',
              searchable = 1,
              required = 1,
              ),
    # NameError: name 'ReferenceBrowserWidget' is not defined
    #atapi.ReferenceField('references',
    #          widget = atapi.ReferenceBrowserWidget(),
    #          multiValued = True,
    #          ),
    ))


class Entity(atapi.BaseContent):
    """An Archetype for an EntitiesDirectory application
    """
    implements(IEntity)

    schema = EntitySchema

    _at_rename_after_creation = True  # ??? isn't this the default?

    def getObfuscatedEmail(self):
        """Get a modified version of email so spambots can't read it.
        """
        email = self.getEmail()
        obfuscated_email = email.replace('@', '-antispam-')
        return obfuscated_email + '@$%&.com'

    def tag(self, **kwargs):
        return self.getField('image').tag(self, **kwargs)

atapi.registerType(Entity, PROJECTNAME)
