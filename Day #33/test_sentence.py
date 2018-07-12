import unittest
from sentence import solution

class SentenceTest(unittest.TestCase):

    def test_first(self):
        input = ["CodefightsIsAwesome"]
        output = "codefights is awesome"
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['vSKwWDjwIerQKMgVaAniorRJlerbKpDgvyKBLPNwSRWtylqKewNFtERNuUBBHAsGkTSSfdhQHJYvAighAdeG']
        output = 'v s kw w djw ier q k mg va anior r jlerb kp dgvy k b l p nw s r wtylq kew n ft e r nu u b b h as gk t s sfdh q h j yv aigh ade g'
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_third(self):
        input = ['VEOwBXWxDTfDTnQZRKdnrOqPBSGuioJYdmISCoIpgXCLXNgnHQnxSntODxGZtimkoOeYlAHUuAwwOhmMkmxeBqdsxRynA']
        output = 'v e ow b x wx d tf d tn q z r kdnr oq p b s guio j ydm i s co ipg x c l x ngn h qnx snt o dx g ztimko oe yl a h uu aww ohm mkmxe bqdsx ryn a'
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
