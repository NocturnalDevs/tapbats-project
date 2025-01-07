from ..websocket_manager import websocket_manager

async def handle_quests_updates(telegramID: str, data: dict):
    message = {"telegramID": telegramID, "data": data}
    await websocket_manager.broadcast(json.dumps(message))