class Room:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.players = []
        self.playing = False
        self.time  = 600
        self.oni = []
        self.pos = None

    def join(self, player) -> bool:
        try:
            if player.room_id is None:
                self.players.append(player)
                player.room_id = self.id
                return True
            else:
                return False
        except:
            return False

    def quit(self, player) -> bool:
        try:
            if player.room_id is not None:
                self.players.append(player)
                player.room_id = self.id
                return True
            else:
                return False
        except:
            return False
