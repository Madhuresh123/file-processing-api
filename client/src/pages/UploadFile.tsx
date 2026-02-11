import { useState } from "react";
import "./UploadPage.css";
import { useNavigate } from "react-router-dom";


export default function UploadFile() {

  const navigate = useNavigate();
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://localhost:8000/files/process", {
        method: "POST",
        body: formData,
        redirect: "follow",
      });

      const data = await response.json();
      setResult(data);
      navigate(`/documents/${data.id}`);

    } catch (error) {
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>📂 File Processing System</h1>
      <p>Upload any file (PDF, Word, Excel, Image, HTML)</p>

      <div className="upload-box">
        <input
          type="file"
          onChange={(e) => {
            const files = e.target.files;
            if (!files || files.length === 0) return; 
            setFile(files[0]);
          }}
        />
        <button onClick={handleUpload} disabled={loading}>
          {loading ? "Processing..." : "Upload & Process"}
        </button>
      </div>

      {result && (
        <div className="result">
          <h3>Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
