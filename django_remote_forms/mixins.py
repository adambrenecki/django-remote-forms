class ExtraAttributesMixin:
    """Adds extra attributes to a forms fields

    Value in the ``extra_attributes`` property will be added to the corresponding Key in fields dictionary
    property
    """
    extra_attributes = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.extra_attributes.items():
            field = self.fields.get(key)
            field.extras = value