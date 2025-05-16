import React, { useState } from 'react';
import ReportForm from './components/ReportForm';
import './style.css';

function App() {
  const [instruction, setInstruction] = useState('');
  const [aiComment, setAiComment] = useState('');
  const [pdfUrl, setPdfUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleInstructionChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInstruction(e.target.value);
  };

  const handleGenerateReport = async () => {
    if (!instruction.trim()) {
      alert('請輸入報表指令！');
      return;
    }

    setLoading(true);
    setAiComment('');
    setPdfUrl(null);

    try {
      const res = await fetch('http://127.0.0.1:5000/generate_report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ instruction }),
      });

      if (!res.ok) throw new Error('報表產生失敗');

      const { pdf_path, comment } = await res.json();

      setPdfUrl(`http://127.0.0.1:5000/${pdf_path}`);
      setAiComment(comment || '（AI 評語載入失敗）');
    } catch (err) {
      alert('錯誤：' + (err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>CPBL 報表產生器</h1>
      <ReportForm instruction={instruction} onChange={handleInstructionChange} />
      <button onClick={handleGenerateReport} disabled={loading}>
        {loading ? '產生中…' : '產生報表'}
      </button>

      {pdfUrl && (
        <div className="download-section">
          <a href={pdfUrl} download="report.pdf">📄 下載報表 PDF</a>
        </div>
      )}

      <div className="comment-section">
        <h2>AIgent 評語</h2>
        <p>{aiComment || '尚未產生評語。'}</p>
      </div>
    </div>
  );
}

export default App;

