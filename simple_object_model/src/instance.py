
from .base import Base
from .maps import EMPTY_MAP

class Instance(Base):
    def __init__(self, cls):
        from .class_model import Class
        assert isinstance(cls, Class)
        Base.__init__(self, cls, None)
        self.map = EMPTY_MAP
        self.storage = []

    def _read_dict(self, fieldname):
        index = self.map.get_index(fieldname)
        if index == -1:
            return self._fields  # Could return MISSING, added fallback
        return self.storage[index]

    def _write_dict(self, fieldname, value):
        index = self.map.get_index(fieldname)
        if index != -1:
            self.storage[index] = value
        else:
            self.map = self.map.next_map(fieldname)
            self.storage.append(value)
