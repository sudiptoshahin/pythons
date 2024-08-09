
"""
    -   All logic should be implement in the 
        private class.
    -   Here we will implement the functionaly
        of Logger.
"""

# class SingletonObject(object):
#     class __SingletonObject(object):
#         def __init__(self):
#             self.val = None

#         def __str__(self):
#             return "{0!r} {1}".format(self, self.val)

#         # Instance
#         instance = None

#         def __new__(cls):
#             print('hello')
#             if not SingletonObject.instance:
#                 print('[warn] Not Instance of singleton')
#                 SingletonObject.instance = SingletonObject.__SingletonObject()
#             else:
#                 print('[warn] Instance of singleton')
    
#             return SingletonObject.instance

#         def __getattribute__(self, name):
#             return getattr(self.instance, name)
        
#         def __setattribute__(self, name):
#             return setattr(self.instance, name)

class SingletonObject(object):
    class __SingletonObject():
        def __init__(self):
            self.val = None
        def __str__(self):
            return "{0!r} {1}".format(self, self.val)
        # the rest of the class definition will follow here, as per the previous logging script
        instance = None
        def __new__(cls):
            if not SingletonObject.instance:
                SingletonObject.instance = SingletonObject.__SingletonObject()
            return SingletonObject.instance
        def __getattr__(self, name):
            return getattr(self.instance, name)
        def __setattr__(self, name):
            return setattr(self.instance, name)