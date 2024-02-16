from PyQt6.QtCore import QSettings, QPoint

settings = QSettings('foo', 'foo')

settings.setValue('int_value', 42)
settings.setValue('list_value', [1, 2, 3])
settings.setValue('dict_value', {'one': 1, 'two': 2})
settings.setValue('point_value', QPoint(10, 12))

# This will write the setting to the platform specific storage.
del settings

settings = QSettings('foo', 'foo')

int_value = settings.value('int_value', type=int)
print("int_value: %s" % repr(int_value))

list_value = settings.value('list_value', type=int)
print("list_value: %s" % repr(list_value))

dict_value = settings.value('dict_value', type=int)
print("dict_value: %s" % repr(dict_value))

point_value = settings.value('point_value', type=QPoint)
print("point_value: %s" % repr(point_value))




