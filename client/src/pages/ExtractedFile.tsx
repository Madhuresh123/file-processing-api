import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./ExtractedFile.css";

export default function ExtractedFile() {
  const { id } = useParams();
  const [doc, setDoc] = useState<any>(null);
  const [editedText, setEditedText] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:8000/documents/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setDoc(data);
        setEditedText(data.raw_text);
      });
  }, [id]);

  const handleSave = async () => {
    setSaving(true);

    await fetch(`http://localhost:8000/documents/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        raw_text: editedText,
      }),
    });

    setSaving(false);
    alert("Saved successfully!");
  };

  if (!doc) return <div className="loading">Loading document...</div>;

  return (
    <div className="document-container">
      <div className="document-card">
        <div className="document-header">
          <div>
            <h1 className="document-title">{doc.filename}</h1>
            <p className="document-meta">
              <span className="badge">{doc.file_type}</span>
              <span className="doc-id">ID: {doc.id}</span>
            </p>
          </div>

          <button
            className="save-btn"
            onClick={handleSave}
            disabled={saving}
          >
            {saving ? "Saving..." : "Save Changes"}
          </button>
        </div>

        <div className="editor-section">
          <textarea
            className="editor"
            value={editedText}
            onChange={(e) => setEditedText(e.target.value)}
          />
        </div>
      </div>
    </div>
  );
}
