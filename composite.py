

class Composite:
    
    def __init__(self):
        self.entries = {}
        
    def _delegate_method(self, method_name):
        def method(self, *args, **kwargs):
            results = {}
            for entry_name, entry in self.entries:
                entry_method = getattr(entry, method_name)
                results[entry_name] = entry_method(*args, **kwargs)
            return results
        setattr(self, method_name, method)
        
    def _delegate_method(self, method_names):
        for method_name in method_names:
            self._delegate_method(method_names)
        

