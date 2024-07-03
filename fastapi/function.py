import gc
import uuid
from classes.room import Room
from classes.player import Player

rooms = []

#テスト用プレイヤー作成
yoshida = Player(uuid.uuid4(), "Yoshida")

# 部屋の作成
def create_room(name: str, max_members: int = 4) -> Room:
    # fix: idは uuidでもいいかも。
    id = uuid.uuid4()
    room = Room(id, name, max_members)
    rooms.append(room)
    return room

# 部屋の削除
def delete_room(id: str) -> bool:
    room_obj = None
    for room in rooms:
        if room.id == id:
            room_obj = room
    if room_obj is None:
        return False
    for member in room_obj.members:
        member.room_id = None
    rooms.remove(room_obj)
    gc.collect()

def get_room_from_uuid(id: str) -> Room:
    res = None
    for room in rooms:
        if room.id == id:
            res = room
    return res

def get_room_from_name(name: str) -> Room:
    res = None
    for room in rooms:
        if room.name == name:
            res = room
    return res


# テスト用の実行コード
if __name__ == "__main__":
    # 新しいユーザーを作成
    # Player.py をインポートして Player クラスを利用する
    player_a = Player(id="1", name="Player A")
    player_b = Player(id="2", name="Player B")
    player_c = Player(id="3", name="Player C")
    player_d = Player(id="4", name="Player D")  # 追加のプレイヤー
    player_e = Player(id="5", name="Player E")  # 追加のプレイヤー

    # 新しい部屋を作成してテスト
    room1 = create_room("Room 1", max_members=3)
    room2 = create_room("Room 2")

    # プレイヤーが部屋に参加する例
    player_a.join_room(room1)
    player_b.join_room(room1)
    player_c.join_room(room1)

    # こいつは参加できないはず
    player_d.join_room(room1)
    player_e.join_room(room2)

    # 部屋のメンバーを表示してテスト
    for room in rooms:
        print(
            f"Room '{room.name}' メンバー一覧: {[player.name for player in room.members]} 最大人数: {room.max_members}")

    # プレイヤーが部屋から退出する例
    player_a.quit_room()
    player_e.quit_room()

    # 退出した部屋の状態を表示してテスト
    for room in rooms:
        print(
            f"中間結果:Room '{room.name}' メンバー一覧: {[player.name for player in room.members]} 最大人数: {room.max_members}")

    # 再度入室
    player_d.join_room(room1)

    # 再度入室した部屋の状態を表示してテスト
    for room in rooms:
        print(
            f"最終結果:Room '{room.name}' メンバー一覧: {[player.name for player in room.members]} 最大人数: {room.max_members}")
