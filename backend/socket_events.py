from flask_socketio import emit, join_room
import redis
import os

r = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, decode_responses=True)

def register_socket_events(socketio):
    @socketio.on('join_hall')
    def handle_join(data):
        hall_id = data['hall_id']
        join_room(f"hall_{hall_id}")

    @socketio.on('lock_seat')
    def handle_lock(data):
        seat_id = data['seat_id']
        hall_id = data['hall_id']
        user_id = data['user_id']
        lock_key = f"lock:{hall_id}:{seat_id}"
        if not r.get(lock_key):
            r.set(lock_key, user_id, ex=120)
            emit('seat_locked', {'seat_id': seat_id}, room=f"hall_{hall_id}")
        else:
            emit('lock_failed', {'seat_id': seat_id})
