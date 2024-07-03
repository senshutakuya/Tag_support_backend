class Room:

    # 初期値
    # fix: 初期値の設定は 変数 = 初期値 でできる。
    def __init__(self, id: str, name: str, max_members: int = 4, members: list = []): 
        # ルームID
        self.id = id
        # ルーム名
        self.name = name
        # 最大人数
        self.max_members = max_members
        # members
        self.members = members
