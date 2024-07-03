class Player:
    def __init__(self,uuid: str, name: str, image: bytes) -> None:
        self.uuid = uuid
        self.name = name
        self.image = image
        self.pos = None
        self.room_id = None
        self.caught = False
        self.playing = False

    # 部屋に入った時に部屋のIDを取得する
    def join_room(self, id: int) -> bool:
        self.room_id = id
        return True