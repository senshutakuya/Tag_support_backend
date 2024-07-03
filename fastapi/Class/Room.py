from Player import Player


class Room:
    # //以降クラスの構造を書く

    rooms = [
        #   //このリスト型変数の中に↑でインスタンス化したルーム情報をルームの数分格納する
    ]

    # 初期値
    def __init__(self, id, name, max_members=None, members=None):
        # ルームID
        self.id = id
        # ルーム名
        self.name = name
        # 最大人数
        # max_members という引数が与えられていればその値を self.members に設定し、なければデフォルトで数値4を設定する
        self.max_members = max_members if max_members is not None else 4
        # メンバー数
        # members という引数が与えられていればその値を self.members に設定し、なければ新しいリストを作る
        self.members = members if members is not None else []

    # 部屋の作成

    @classmethod
    def create_room(cls, room_name, max_members=None):
        # cls.rooms はすべての部屋のリストで、その長さに1を足すことで、新しい部屋のIDを一意に設定します
        new_room = cls(len(cls.rooms) + 1, room_name, max_members)
        print(new_room)
        cls.rooms.append(new_room)
        print(
            f"Room名 '{room_name}' ルームIDは {new_room.id}  最大人数は{new_room.max_members}")
        return new_room

    # ルームを検索して参加する処理

    @classmethod
    def join_room(cls, player, room_name):
        # roomsのリストの回数分roomという変数に対象の値を割り当てfor文回す
        for room in cls.rooms:
            # もしルーム名と引数のルーム名が一致したら
            if room.name == room_name:

                # 自分が参加すると最大人数が上回る時
                if len(room.members) >= room.max_members:
                    print("人数が最大の為参加できません")
                    return False
                # 上回らない時
                else:

                    # プレイヤーを参加させる
                    room.join(player)
                    # プレイヤークラスにルームIDを追加する
                    print(f"ルームIDは{room.id}")
                    player.join_room(room.id)
                    return
        # 指定した名前のルームが存在しない場合はルームを作成し、プレイヤーを追加します
        new_room = cls.create_room(room_name)
        new_room.join(player)
        # プレイヤークラスにルームIDを追加する
        player.join_room(new_room.id)

    # 参加する処理

    def join(self, player):
        # メンバーにプレイヤーを追加する
        self.members.append(player)

        print(f"プレイヤー '{player}' が '{self.name}' に参加しました。")

    @classmethod
    def find_room_by_id(cls, room_id):
        # roomsのリストの回数分roomという変数に対象の値を割り当てfor文回す
        for room in cls.rooms:
            # もしルームIDが引数のIDと一致したら
            if room.id == room_id:
                # ルームを返す
                return room
        # 全て一致しなかったら
        return None

    def delete_room(self):
        Room.rooms.remove(self)
        print(f"Room '{self.name}' deleted.")

    @classmethod
    def leave_the_room(cls, player):
        try:
            print(f"デバックplayer変数の中身{player}")
            print(f"デバックplayer.room_id変数の中身{player.room_id}")
            # もしプレイヤーのルームIDがあり
            if player.room_id is not None:
                # 対象の部屋をpleyerのroom.idから取得する
                room = cls.find_room_by_id(player.room_id)
                # roomのメンバーにplayerがいた場合
                if room is not None and player in room.members:
                    # 対象のユーザを部屋から削除する
                    room.members.remove(player)
                    # プレイヤーのルームIDをNoneに設定
                    player.room_id = None
                    print(f"Player '{player.name}' left '{room.name}'.")
                    # 対象ルームに居る人数が空なら
                    if not room.members:
                        # 部屋を削除する関数呼び出し
                        cls.delete_room(room)
                    # 対象ルームに人が居るなら
                    else:
                        exit
                # roomのメンバーにplayerが居ない場合
                else:
                    print(f"プレイヤー '{player.name}' は部屋に属していないか、指定された部屋に存在しません。")
            # もしプレイヤーのルームIDがなかったら
            else:
                print("プレイヤーのルームIDがないか対象の部屋にあなたがいません")
        # エラー時の対応
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return False


# #テスト用の実行コード
# if __name__ == "__main__":
#     # 新しいユーザーを作成
#     # Player.py をインポートして Player クラスを利用する
#     player_a = Player(uuid="1", name="Player A", image=b"")
#     player_b = Player(uuid="2", name="Player B", image=b"")
#     player_c = Player(uuid="3", name="Player C", image=b"")
#     player_d = Player(uuid="4", name="Player D", image=b"")  # 追加のプレイヤー
#     player_e = Player(uuid="5", name="Player E", image=b"")  # 追加のプレイヤー

#     # 新しい部屋を作成してテスト
#     room1 = Room.create_room("Room 1", max_members=3)
#     room2 = Room.create_room("Room 2")

#     # プレイヤーが部屋に参加する例
#     Room.join_room(player_a, "Room 1")
#     Room.join_room(player_b, "Room 1")
#     Room.join_room(player_c, "Room 1")
#     # こいつは参加できないはず
#     Room.join_room(player_d, "Room 1")
#     Room.join_room(player_e, "Room 2")

#     # 部屋のメンバーを表示してテスト
#     for room in Room.rooms:
#         print(
#             f"Room '{room.name}' メンバー一覧: {[player.name for player in room.members]} 最大人数: {room.max_members}")

#     # プレイヤーが部屋から退出する例
#     Room.leave_the_room(player_a)
#     Room.leave_the_room(player_e)

#     # 退出した部屋の状態を表示してテスト
#     for room in Room.rooms:
#         print(
#             f"中間結果:Room '{room.name}' メンバー一覧: {[player.name for player in room.members]} 最大人数: {room.max_members}")

#     # 再度入室
#     Room.join_room(player_d, "Room 1")

#     # 再度入室した部屋の状態を表示してテスト
#     for room in Room.rooms:
#         print(
#             f"最終結果:Room '{room.name}' メンバー一覧: {[player.name for player in room.members]} 最大人数: {room.max_members}")
