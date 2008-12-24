from base import EntitiesDirectoryTestCase

class TestProductInstall(EntitiesDirectoryTestCase):

    def afterSetUp(self):
        self.types = ('EntitiesDirectory', 'Entity',)

    def testTypesInstalled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)
                                    
    def testPortalFactoryEnabled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_factory.getFactoryTypes().keys(),
                            '%s content type not installed' % t)
                            
class TestInstantiation(EntitiesDirectoryTestCase):
    
    def testCreateEntitiesDirectory(self):
        self.folder.invokeFactory('EntitiesDirectory', 'im1')
        self.failUnless('im1' in self.folder.objectIds())

    def testEntityNotGloballyAllowed(self):
        self.assertRaises(ValueError, self.folder.invokeFactory, 'Entity', 'e1')

    def testCreateEntityInsideDirectory(self):
        self.folder.invokeFactory('EntitiesDirectory', 'im1')
        self.im1 = getattr(self.folder, 'im1')
        self.im1.invokeFactory('Entity', 'e1')
        self.failUnless('e1' in self.im1.objectIds())

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestInstantiation))
    return suite
