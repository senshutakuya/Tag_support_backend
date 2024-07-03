from .room import Room

class Player:
    def __init__(self, id: str, name: str, image: bytes = None) -> None:
        self.id = id
        self.name = name
        self.image = image
        self.pos = None
        self.room = None
        self.caught = False
        self.playing = False

    def join_room(self, room: Room) -> bool:
        if self.room is not None:
            return False
        if len(room.members) >= room.max_members:
            return False
        room.members.append(self)
        self.room = room
        return True

    def quit_room(self) -> bool:
        if self.room is None:
            return False
        self.room.members.remove(self)
        self.room = None
        return True
