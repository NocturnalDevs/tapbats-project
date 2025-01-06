const socket = new WebSocket('ws://localhost:8000/ws');

socket.onopen = () => {
    console.log('WebSocket connection established');
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('WebSocket message received:', data);
    // Handle real-time updates (e.g., update gem count)
};

export default socket;