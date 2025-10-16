import React, { useState } from 'react';

export default function Report() {
  const [desc, setDesc] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = e => {
    e.preventDefault();
    // TODO: Encrypt and send report to backend
    setSubmitted(true);
  };

  return (
    <div className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Anonymous Reporting</h1>
      {submitted ? (
        <div className="bg-green-100 p-4 rounded">Thank you for your report. It has been securely submitted.</div>
      ) : (
        <form onSubmit={handleSubmit} className="space-y-4">
          <textarea
            className="w-full border p-2 rounded"
            rows={6}
            placeholder="Describe the irregularity..."
            value={desc}
            onChange={e => setDesc(e.target.value)}
            required
          />
          <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Submit Report</button>
        </form>
      )}
    </div>
  );
}