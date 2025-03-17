import React, { useState } from "react";

const API_URL = "https://your-api-id.execute-api.us-east-1.amazonaws.com/default/Magic8BallFunction";

export default function Magic8Ball() {
    const [answer, setAnswer] = useState("Ask me anything...");
    const [newAnswer, setNewAnswer] = useState("");

    const getAnswer = async () => {
        const response = await fetch(API_URL);
        const data = await response.json();
        setAnswer(data.answer);
    };

    const addAnswer = async () => {
        if (newAnswer.trim()) {
            await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ answer: newAnswer })
            });
            setNewAnswer("");
            alert("Custom answer added!");
        }
    };

    return (
        <div className="container">
            <h1>🎱 Magic 8-Ball</h1>
            <p>{answer}</p>
            <button onClick={getAnswer}>Ask Again</button>

            <h2>Add Your Own Answer:</h2>
            <input
                value={newAnswer}
                onChange={(e) => setNewAnswer(e.target.value)}
                placeholder="Type your answer here"
            />
            <button onClick={addAnswer}>Submit</button>
        </div>
    );
}

