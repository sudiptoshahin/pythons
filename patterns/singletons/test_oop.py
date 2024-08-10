

class TestBlueprint(object):
    instance = None
    class __TestBlueprint():
        def __init__(self):
            self.val = 'world'
            TestBlueprint.instance = None

        def __new__(cls):
            return TestBlueprint.instance = TestBlueprint.__TestBlueprint()


