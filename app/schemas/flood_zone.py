class FloodZoneSchema(object):

    @classmethod
    def dump(cls, obj, many=False):
        if many:
            return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj)

    @classmethod
    def _serialize_collection(cls, pagination):
        return {
            "zonas": [
                cls._serialize(item)
                for item in pagination.items
            ],
            "total": pagination.pages,
            "pagina": pagination.page
        }

    @classmethod
    def _serialize(cls, obj):
        return { 
            (
                attr.name if attr.name != "color_id"
                else "color"
            ) : (
                getattr(obj, attr.name) if attr.name != "color_id"
                else getattr(obj, "color").value
            )
            for attr in obj.__table__.columns
            if attr.name not in ["state", "id"] 
        }