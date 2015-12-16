
from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from plone.supermodel import model
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.sgvizler import _


# Interface class; used to define content-type schema.

class ISPARQLViz(model.Schema, IImageScaleTraversable):
    """
    SPARQL Visualization
    """

    title = schema.TextLine(
        title=_(u'sgvizler_sparqlviz_title_title',
            default=u'Figure Title'),
        required=True,
    )

    description = schema.Text(
        title=_(u'sgvizler_sparqlviz_description_title',
            default=u'Description'),
        required=True,
    )

class SPARQLViz(Item):

    # Add your class methods and properties here
    pass


# View class
# The view is configured in configure.zcml. Edit there to change
# its public name. Unless changed, the view will be available
# TTW at content/@@sampleview

class SampleView(BrowserView):
    """ sample view class """

    index = ViewPageTemplateFile('sparql_viz_templates/sampleview.pt')

#    def __init__(context, request):
#        self.context = context
#        self.request = request

    def __call__(self):
        return self.render()

    def render(self):
        return self.index()
