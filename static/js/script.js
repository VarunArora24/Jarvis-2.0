document.addEventListener('DOMContentLoaded', () => {

    // ---------------- Left sidebar toggle logic ----------------
    const tools = document.querySelectorAll('.tool-item');
    const contents = document.querySelectorAll('.content_block');

    const contentClasses = [
        'dashboard_content',
        'todo_content',
        'clock_content',
        'text_content',
        'settings_content' // removed calculator from JS handling
    ];

    if(tools[0]) tools[0].classList.add('active');
    if(contents[0]) contents[0].classList.add('active');

    tools.forEach((tool, index) => {
        tool.addEventListener('click', () => {
            tools.forEach(t => t.classList.remove('active'));
            tool.classList.add('active');

            contents.forEach(c => c.classList.remove('active'));
            const contentToShow = document.querySelector(`.${contentClasses[index]}`);
            if(contentToShow) contentToShow.classList.add('active');
        });
    });

    // ---------------- Right sidebar Jarvis chat ----------------
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");

    if (sendBtn && userInput && chatMessages) {
        sendBtn.addEventListener("click", sendMessage);
        userInput.addEventListener("keypress", function(e) {
            if (e.key === "Enter") sendMessage();
        });

        function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;

            // user message
            const userDiv = document.createElement("div");
            userDiv.classList.add("chat-message", "user-msg");
            userDiv.textContent = message;
            chatMessages.appendChild(userDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            userInput.value = "";

            // fetch from Flask
            fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message })
            })
            .then(res => res.json())
            .then(data => {
                const jarvisDiv = document.createElement("div");
                jarvisDiv.classList.add("chat-message", "jarvis-msg");
                jarvisDiv.textContent = data.response;
                chatMessages.appendChild(jarvisDiv);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            });
        }
    }

});
