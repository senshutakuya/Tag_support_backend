class Room:

    # 初期値
    # fix: 初期値の設定は 変数 = 初期値 でできる。
    def __init__(self, id: str, name: str, max_members: int): 

        # ルームID
        self.id = id
        # ルーム名
        self.name = name
        # 最大人数
        self.max_members = max_members
        # members
        self.members = []

    def join(self, member) -> bool:
        if len(self.members) >= self.max_members:
            return False
        self.members.append(member)
        member.room = self
        return True

    def quit(self, member) -> bool:
        self.members.remove(member)
        member.room = None
        return True
