class RequestContext:
    def __init__(self):
        self.model = None
        self.cache = {}
    
    def setup(self):
        self.model = load_model()
    
    def teardown(self):
        self.model.cleanup()

ctx = RequestContext()
ctx.setup()
try:
    result = ctx.model.predict(X)
finally:
    ctx.teardown()