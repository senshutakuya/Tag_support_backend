class Player:
    def __init__(self, id: str, name: str, image: bytes = None) -> None:
        self.id = id
        self.name = name
        self.image = image
        self.pos = None
        self.room = None
        self.caught = False
        self.playing = False

    def join_room(self, room) -> bool:
        if self.room is not None:
            return False
        return room.join(self)

    def quit_room(self) -> bool:
        if self.room is None:
            return False
        return self.room.quit(self)
