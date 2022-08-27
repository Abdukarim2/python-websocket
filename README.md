# python-websocket server
```
1 run python main.py
```
```
2 run python -m websockets ws://localhost:8000
```
## write something ...
```
< hello
> your message reversed from server hello
```
```
js
const socket = new WebSocket('ws://localhost:8000');
```