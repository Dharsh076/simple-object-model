
import pytest
from src.class_model import Class
from src.instance import Instance
from src.base import MISSING

def OBJECT__setattr__(self, fieldname, value):
    self._write_dict(fieldname, value)

OBJECT = Class("object", None, {"__setattr__": OBJECT__setattr__}, None)
TYPE = Class("type", OBJECT, {}, None)
TYPE.cls = TYPE
OBJECT.cls = TYPE

def test_read_write_field():
    A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("a", 1)
    assert obj.read_attr("a") == 1
    obj.write_attr("b", 5)
    assert obj.read_attr("b") == 5
    obj.write_attr("a", 2)
    assert obj.read_attr("a") == 2

def test_method_override():
    def f_A(self):
        return self.read_attr("x") + 1

    A = Class(name="A", base_class=OBJECT, fields={"f": f_A}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("x", 1)
    assert obj.callmethod("f") == 2

    def f_B(self):
        return self.read_attr("x") + 2

    B = Class(name="B", base_class=A, fields={"f": f_B}, metaclass=TYPE)
    obj = Instance(B)
    obj.write_attr("x", 3)
    assert obj.callmethod("f") == 5

def test_getattr_setattr():
    def __getattr__(self, name):
        if name == "fahrenheit":
            return self.read_attr("celsius") * 9. / 5. + 32
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == "fahrenheit":
            self.write_attr("celsius", (value - 32) * 5. / 9.)
        else:
            OBJECT.read_attr("__setattr__")(self, name, value)

    A = Class(name="A", base_class=OBJECT,
              fields={"__getattr__": __getattr__, "__setattr__": __setattr__},
              metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("celsius", 30)
    assert obj.read_attr("fahrenheit") == 86
    obj.write_attr("fahrenheit", 86)
    assert obj.read_attr("celsius") == 30

def test_maps():
    Point = Class(name="Point", base_class=OBJECT, fields={}, metaclass=TYPE)
    p1 = Instance(Point)
    p1.write_attr("x", 1)
    p1.write_attr("y", 2)
    assert p1.storage == [1, 2]
    assert p1.map.attrs == {"x": 0, "y": 1}

    p2 = Instance(Point)
    p2.write_attr("x", 5)
    p2.write_attr("y", 6)
    assert p1.map is p2.map
    assert p2.storage == [5, 6]

    p3 = Instance(Point)
    p3.write_attr("x", 100)
    p3.write_attr("z", -343)
    assert p3.map is not p1.map
    assert p3.map.attrs == {"x": 0, "z": 1}
