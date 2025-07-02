MISSING = object()

class Base(object):
    def __init__(self, cls, fields):
        self.cls = cls
        self._fields = fields

    def read_attr(self, fieldname):
        result = self._read_dict(fieldname)
        if result is not MISSING:
            return result
        result = self.cls._read_from_class(fieldname)
        if result is not MISSING:
            if _is_bindable(result):
                return _make_boundmethod(result, self)
            return result
        fallback = self.cls._read_from_class("__getattr__")
        if fallback is not MISSING:
            return fallback(self, fieldname)
        raise AttributeError(fieldname)

    def write_attr(self, fieldname, value):
        setter = self.cls._read_from_class("__setattr__")
        if setter is not MISSING:
            return setter(self, fieldname, value)
        return self._write_dict(fieldname, value)

    def callmethod(self, methname, *args):
        meth = self.read_attr(methname)
        return meth(*args)

    def isinstance(self, cls):
        return self.cls.issubclass(cls)

    def _read_dict(self, fieldname):
        return self._fields.get(fieldname, MISSING)

    def _write_dict(self, fieldname, value):
        self._fields[fieldname] = value

def _is_bindable(meth):
    return hasattr(meth, "__get__")

def _make_boundmethod(meth, self):
    return meth.__get__(self, None)
