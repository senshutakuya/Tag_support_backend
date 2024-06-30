from Player import Player

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
        # roomsのリストの回数分roomという変数に対象の値を割り当てfor文回す
        for room in cls.rooms:
            # もしルーム名と引数のルーム名が一致したら
            if room.name == room_name:
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
            # もしルームIDが一致したら
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
        
    


# テスト用の実行コード
if __name__ == "__main__":
    # 新しいユーザーを作成
    # Player.py をインポートして Player クラスを利用する
    player_a = Player(uuid="1", name="Player A", image=b"")
    player_b = Player(uuid="2", name="Player B", image=b"")
    player_c = Player(uuid="3", name="Player C", image=b"")

    # 新しい部屋を作成してテスト
    room1 = Room.create_room("Room 1")
    room2 = Room.create_room("Room 2")

    # プレイヤーが部屋に参加する例
    Room.join_room(player_a, "Room 1")
    Room.join_room(player_b, "Room 2")
    Room.join_room(player_c, "Room 1")

    # 部屋のメンバーを表示してテスト
    for room in Room.rooms:
        print(f"Room '{room.name}' メンバー一覧: {[player.name for player in room.members]}")

    # プレイヤーが部屋から退出する例
    Room.leave_the_room(player_a)
    Room.leave_the_room(player_b)

    # 最終的な部屋の状態を表示してテスト
    for room in Room.rooms:
        print(f"最終結果:Room '{room.name}' メンバー一覧: {[player.name for player in room.members]}")
