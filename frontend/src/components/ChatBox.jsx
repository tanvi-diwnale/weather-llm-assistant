import { useState } from "react";
import { sendMessage } from "../services/api";

const ChatBox = () => {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const handleSend = async () => {
    if (!message.trim()) return;
    const data = await sendMessage(message);
    setReply(data.response);
  };

return (
  <div className="weather-card">
    <h2 style={{ color: "#1f2937" }}>
      The only Weather Forecast you need!!
    </h2>

{/* Weather Icons */}
<div className="weather-icons">
  <span className="material-symbols-outlined rain-icon" title="Rainy">
    rainy
  </span>

  <span className="material-symbols-outlined sun-icon" title="Sunny">
    sunny
  </span>
</div>

    <input
      type="text"
      placeholder="Ask weather of a city (e.g. Pune)"
      value={message}
      onChange={(e) => setMessage(e.target.value)}
    />

    <button onClick={handleSend}>Get Weather</button>

    {reply && (
      <div className="response">
        <b>Result:</b>
        <p>{reply}</p>
      </div>
    )}
  </div>
);
};

export default ChatBox;
