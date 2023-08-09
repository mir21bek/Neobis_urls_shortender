import { useState } from "react";

function App() {
    const [long_url, setLongurl] = useState("");
    const [short_url, setShorturl] = useState("");
    const [returnLongURL, setReturnLongURL] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch("http://127.0.0.1:8000/shorten/", {
            method: "POST",
            body: JSON.stringify({ long_url: long_url }),
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
                setShorturl(data.short_url);
                setReturnLongURL(data.long_url);
                setLongurl("");
            });
    };

    return (
        <div style={{ textAlign: "center" }}>
            <input
                type="text"
                name="longurl"
                value={long_url}
                onChange={(e) => setLongurl(e.target.value)}
            />
            <button
                type="submit"
                onClick={(e) => handleSubmit(e)}
                disabled={!long_url}
            >
                shorten
            </button>

            <div>
                <p>Long URL: {returnLongURL}</p>
                <p
                    style={{ cursor: "pointer" }}
                    onClick={() => window.open(returnLongURL)}
                >
                    Short URL: {short_url}
                </p>
            </div>
        </div>
    );
}

export default App;
