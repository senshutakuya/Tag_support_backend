class Player:

    def __init__(id, name, icon_id, gps) -> None:
        self.id = id
        self.name = name
        self.icon_id = icon_id
        self.gps = gps
        self.playing = False
        self.arrested = False

    def get_id() -> str:
        return self.id

    def get_name() -> str:
        return self.name

    def get_icon_id() -> int:
        return self.icon_id

    def get_gps() -> object:
        return self.gps

    def is_playing() -> bool:
        return self.playing

    def is_arrested() -> bool:
        return self.arrested
    
    def set_name