from collections.abc import Iterable


class DataContainer:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, DataContainer.__encode_data(value))

    @staticmethod
    def __encode_data(data):
        if isinstance(data, dict):
            if 'self' in data:
                data['self_'] = data.pop('self')
            return DataContainer(**data)
        if isinstance(data, Iterable) and not isinstance(data, str):
            return [DataContainer.__encode_data(item) for item in data]
        return data

    def keys(self):
        return [key for key in dir(self) if not key.startswith('_')]

    def values(self):
        return [getattr(self, key) for key in self.keys()]

    def __repr__(self):
        attributes = {}
        for key in dir(self):
            value = getattr(self, key)
            if not key.startswith('_') and not callable(value):
                attributes[key] = value
        return f'{type(self).__name__}(**{attributes.__str__()})'
