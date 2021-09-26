import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    map_info = [1,0,0,0]
    data = {'map':map_info}
    sio.emit('my_response',data)


@sio.event
def my_message(data):
    print('message received with ', data)
    #sio.emit('my_response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:6000')
sio.wait()

