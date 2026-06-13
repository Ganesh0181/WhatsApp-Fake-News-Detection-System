import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [text, setText] = useState("");
  const [phone, setPhone] = useState("");
  const [prediction, setPrediction] = useState("");
  const [confidence, setConfidence] = useState("");
  const [loading, setLoading] = useState(false);

  const checkNews = async () => {

    if (!text || !phone) {

      alert("Enter news text and phone number");

      return;
    }

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        {
          text: text,
          phone: phone
        }
      );

      setPrediction(response.data.prediction);

      setConfidence(response.data.confidence);

    } catch (error) {

      console.log(error);

      alert("Server Error");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="main-container">

      <div className="card-box">

        <h1>
          Fake News Detector
        </h1>

        <textarea
          placeholder="Paste suspicious news here..."
          rows="10"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <input
          type="text"
          placeholder="Enter WhatsApp Number"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />

        <button onClick={checkNews}>

          {
            loading
            ?
            "Analyzing..."
            :
            "Check News"
          }

        </button>

        {

          prediction && (

            <div className="result-box">

              <h2>{prediction}</h2>

              <h3>
                Confidence: {confidence}%
              </h3>

            </div>
          )
        }

      </div>

    </div>
  );
}

export default App;