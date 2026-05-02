import { useState } from "react";
import axios from "axios";

function App() {
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runAgent = async () => {
    if (!goal) return;

    setLoading(true);
    setResult(null);

    try {
      const res = await axios.post("http://127.0.0.1:8000/run-agent", {
        goal: goal,
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ error: "Failed to connect to backend" });
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 40, fontFamily: "Arial" }}>
      <h2>Nexus AI Agent</h2>

      <input
        type="text"
        placeholder="Enter your goal..."
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
        style={{ width: 350, padding: 10 }}
      />

      <br /><br />

      <button onClick={runAgent} disabled={loading}>
        {loading ? "Running..." : "Run Agent"}
      </button>

      <div style={{ marginTop: 20 }}>
        <strong>Output:</strong>
        <pre style={{ background: "#f4f4f4", padding: 10 }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      </div>
    </div>
  );
}

export default App;