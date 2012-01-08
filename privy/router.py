# This allows the use of the 'connection_name' field inside models to specify
# which database they correspond to.
class dashboard_router(object):
    """
    Allows models to define the database connection they
    want to use.
    """
    def db_for_read(self, model, **hints):
        if hasattr(model, 'connection_name'):
            return model.connection_name
        return None

    def db_for_write(self, model, **hints):
        if hasattr(model, 'connection_name'):
            return model.connection_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        if hasattr(model, 'connection_name'):
            return db == model.connection_name
        return db == 'default'

