async function sendMessage() {
    const input = document.getElementById("chatInput");
    const message = input.value.trim();
    if (!message) return;

    addMessage("You", message);

    // Send message to backend
    try {
        const res = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await res.json();

        // Show Jarvis reply
        addMessage("Jarvis", data.reply);
    } catch (err) {
        addMessage("Jarvis", "⚠️ Backend not connected.");
    }

    input.value = "";
}
