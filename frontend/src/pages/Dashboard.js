import React from 'react';

export default function Dashboard() {
  // Placeholder data for demo
  const tenders = [
    { id: 1, title: 'Road Construction', department: 'Transport', province: 'Gauteng', status: 'open' },
    { id: 2, title: 'School Supplies', department: 'Education', province: 'Western Cape', status: 'awarded' },
  ];
  const flagged = [
    { id: 2, issue: 'Repeated vendor awards', tender: 'School Supplies' },
  ];
  const stats = {
    vendorDominance: 'Vendor A: 60%',
    avgDelay: '5 days',
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">OpenTender SA Dashboard</h1>
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Browse Tenders</h2>
        <table className="min-w-full bg-white border">
          <thead>
            <tr>
              <th className="py-2 px-4 border">Title</th>
              <th className="py-2 px-4 border">Department</th>
              <th className="py-2 px-4 border">Province</th>
              <th className="py-2 px-4 border">Status</th>
            </tr>
          </thead>
          <tbody>
            {tenders.map(t => (
              <tr key={t.id}>
                <td className="py-2 px-4 border">{t.title}</td>
                <td className="py-2 px-4 border">{t.department}</td>
                <td className="py-2 px-4 border">{t.province}</td>
                <td className="py-2 px-4 border">{t.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Flagged Irregularities</h2>
        <ul className="list-disc pl-6">
          {flagged.map(f => (
            <li key={f.id} className="text-red-600">{f.issue} in <strong>{f.tender}</strong></li>
          ))}
        </ul>
      </section>
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Statistics</h2>
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-gray-100 p-4 rounded">Vendor Dominance: {stats.vendorDominance}</div>
          <div className="bg-gray-100 p-4 rounded">Average Delay: {stats.avgDelay}</div>
        </div>
      </section>
    </div>
  );
}