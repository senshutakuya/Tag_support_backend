class Room:
    # //以降クラスの構造を書く

    rooms = [
        #   //このリスト型変数の中に↑でインスタンス化したルーム情報をルームの数分格納する
    ]

    # 初期値
    def __init__(self, id, name, members=None):
        # ルームID
        self.id = id
        # ルーム名
        self.name = name
        # メンバー数
        # members という引数が与えられていればその値を self.members に設定し、なければ新しいリストを作る
        self.members = members if members is not None else []

    # 部屋の作成

    @classmethod
    def create_room(cls, room_name):

        new_room = cls(len(cls.rooms) + 1, room_name)
        print(new_room)
        cls.rooms.append(new_room)
        print(f"Room '{room_name}' created with ID {new_room.id}")
        return new_room

    # ルームを検索して参加する処理

    @classmethod
    def join_room(cls, player, room_name):
        # roomsのリストの回数分for文回す
        for room in cls.rooms:
            # もしルーム名と引数のルーム名が一致したら
            if room.name == room_name:
                # プレイヤーを参加させる
                room.join(player)
                return
        # 指定した名前のルームが存在しない場合はルームを作成し、プレイヤーを追加します
        new_room = cls.create_room(room_name)
        new_room.join(player)

    # 参加する処理

    def join(self, player):
        # メンバーにプレイヤーを追加する
        self.members.append(player)

        print(f"プレイヤー '{player}' が '{self.name}' に参加しました。")

    def leave_the_room(player):
        # ルームに居る人数を把握
        # 対象のユーザを部屋から削除する
        # もしルームに居る人数が0人ならば
        # 部屋を削除する
        # それ以外なら
        exit


# テスト用の実行コード
if __name__ == "__main__":
    # 新しい部屋を作成してテスト
    room1 = Room.create_room("Room 1")
    room2 = Room.create_room("Room 2")

    # プレイヤーが部屋に参加する例
    Room.join_room("Player A", "Room 1")
    Room.join_room("Player B", "Room 2")
    Room.join_room("Player C", "Room 1")

    # 部屋のメンバーを表示してテスト
    for room in Room.rooms:
        print(f"Room '{room.name}' members: {room.members}")

    # プレイヤーが部屋から退出する例
    Room.rooms[0].leave_the_room("Player A")
    Room.rooms[1].leave_the_room("Player B")

    # 最終的な部屋の状態を表示してテスト
    for room in Room.rooms:
        print(f"Room '{room.name}' members: {room.members}")
