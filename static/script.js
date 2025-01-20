const chatInput = document.getElementById('chatInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.querySelector('.chat-messages');

sendButton.addEventListener('click', sendMessage);

function sendMessage() {
    const messageText = chatInput.value.trim();
    if (messageText) {
        // Add user message
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user');
        userMessage.innerHTML = `<span class="text">${messageText}</span>`;
        chatMessages.appendChild(userMessage);

        // Scroll to the bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Clear input
        chatInput.value = '';

        // Simulate bot response
        setTimeout(() => {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot');
            botMessage.innerHTML = `<span class="text">Got it! Here's my response to: "${messageText}"</span>`;
            chatMessages.appendChild(botMessage);

            // Scroll to the bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 1000);
    }
}
