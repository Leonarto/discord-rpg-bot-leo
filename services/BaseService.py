from db_engine import session


class BaseService:
    def __init__(self, *args, **kwargs):
        self.session = session
