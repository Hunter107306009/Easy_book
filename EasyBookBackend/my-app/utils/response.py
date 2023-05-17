
class Response:
    @classmethod
    def Success(cls, data: any):
        return {"status": "success", "data": data}

    @classmethod
    def Error(cls, msg: str):
        return {"status": "error", "msg": msg}
