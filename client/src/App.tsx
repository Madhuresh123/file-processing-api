import { Routes, Route } from "react-router-dom";
import UploadPage from "./pages/UploadFile";
import ExtractedFile from "./pages/ExtractedFile";

function App() {
  return (
    <Routes>
      <Route path="/" element={<UploadPage />} />
      <Route path="/documents/:id" element={<ExtractedFile />} />
    </Routes>
  );
}

export default App;
