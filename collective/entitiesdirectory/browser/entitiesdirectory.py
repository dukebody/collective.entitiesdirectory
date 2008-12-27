from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class EntitiesDirectoryView(BrowserView):
    template = ViewPageTemplateFile("entitiesdirectory_view.pt")

    __call__ = template

    def getEntities(self):
        """Return entities matching the filters selected in the form.
        """
        context = self.context
        form = self.request.form
        submitted = form.get('search') is not None

        if not submitted:
            return self.context.getFolderContents()
        else:  # the form has been submitted
            catalog = getToolByName(context, 'portal_catalog')
            cur_path = '/'.join(context.getPhysicalPath())
            path = {'query':cur_path, 'depth':1}
            results = catalog(portal_type='Entity', path=path,
                SearchableText=form['searchText'])
            return results
