const API_URL = "http://127.0.0.1:8000";

const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const chatBox = document.getElementById("chat-box");
const emptyState = document.getElementById("empty-state");

const newChatButton = document.getElementById("new-chat");

const startScreen = document.getElementById("start-screen");
const startButton = document.getElementById("start-button");


/* =========================================================
   START SCREEN
   ========================================================= */

if (startButton && startScreen) {

    startButton.addEventListener("click", () => {

        startScreen.style.opacity = "0";

        setTimeout(() => {
            startScreen.style.display = "none";
        }, 300);

        messageInput.focus();

    });

}


/* =========================================================
   ADD MESSAGE
   ========================================================= */

function addMessage(text, sender, meme = null) {

    const message = document.createElement("div");

    message.classList.add("message");

    if (sender === "user") {
        message.classList.add("user-message");
    } else {
        message.classList.add("bot-message");
    }


    const content = document.createElement("div");

    content.classList.add("message-content");


    /* ---------------------------------------------------------
       TEXT RESPONSE
       --------------------------------------------------------- */

    if (text) {

        const textElement = document.createElement("div");

        textElement.textContent = text;

        content.appendChild(textElement);

    }


    /* ---------------------------------------------------------
       MEME RESPONSE
       --------------------------------------------------------- */

    if (meme) {

        const memeImage = document.createElement("img");

        memeImage.classList.add("message-meme");

        memeImage.src = meme;

        memeImage.alt = "Bot reaction meme";

        memeImage.loading = "lazy";

        content.appendChild(memeImage);

    }


    message.appendChild(content);

    chatBox.appendChild(message);


    /* ---------------------------------------------------------
       HIDE EMPTY STATE
       --------------------------------------------------------- */

    emptyState.style.display = "none";


    /* ---------------------------------------------------------
       SCROLL TO NEWEST MESSAGE
       --------------------------------------------------------- */

    requestAnimationFrame(() => {

        const chatArea = document.getElementById("chat-area");

        chatArea.scrollTop = chatArea.scrollHeight;

    });

}


/* =========================================================
   SEND MESSAGE TO BACKEND
   ========================================================= */

async function sendMessage(message) {

    try {

        const response = await fetch(`${API_URL}/api/chat`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }


        const data = await response.json();

        return data;

    }

    catch (error) {

        console.error("Chat error:", error);

        return {
            text: "I couldn't connect to the AI server.",
            emotion: "error",
            meme: null
        };

    }

}


/* =========================================================
   FORM SUBMISSION
   ========================================================= */

chatForm.addEventListener("submit", async (event) => {

    event.preventDefault();


    const message = messageInput.value.trim();


    if (!message) {
        return;
    }


    /* ---------------------------------------------------------
       SHOW USER MESSAGE
       --------------------------------------------------------- */

    addMessage(message, "user");


    /* ---------------------------------------------------------
       CLEAR INPUT
       --------------------------------------------------------- */

    messageInput.value = "";


    /* ---------------------------------------------------------
       DISABLE INPUT WHILE WAITING
       --------------------------------------------------------- */

    messageInput.disabled = true;


    const response = await sendMessage(message);


    /* ---------------------------------------------------------
       SHOW BOT RESPONSE
       --------------------------------------------------------- */

    addMessage(
        response.text || "",
        "bot",
        response.meme || null
    );


    /* ---------------------------------------------------------
       ENABLE INPUT
       --------------------------------------------------------- */

    messageInput.disabled = false;

    messageInput.focus();

});


/* =========================================================
   NEW CHAT
   ========================================================= */

newChatButton.addEventListener("click", () => {

    chatBox.innerHTML = "";

    emptyState.style.display = "block";

    messageInput.value = "";

    messageInput.disabled = false;

    messageInput.focus();

});