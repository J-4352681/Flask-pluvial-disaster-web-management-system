class ComplaintSchema(object):

    @classmethod
    def dump(cls, obj):
        return cls._serialize(obj)

    @classmethod
    def _serialize(cls, obj):
        return { 
            attr.name : getattr(obj, attr.name)
            for attr in obj.__table__.columns
            if attr.name not in ["state", "id", "assigned_user_id"] 
            and getattr(obj, attr.name) is not None 
        }
 