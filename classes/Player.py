class Player:
    def __init__(self,uuid: str, name: str, image: bytes) -> None:
        self.uuid = uuid
        self.name = name
        self.image = image
        self.pos = None
        self.room_id = None
        self.caught = False
        self.playing = False
        
    def join_room(id: int) -> bool:
        pass