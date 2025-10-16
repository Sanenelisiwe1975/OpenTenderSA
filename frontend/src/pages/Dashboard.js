import React, { useState } from 'react';

export default function Dashboard() {
  const [searchTerm, setSearchTerm] = useState('');
  const [provinceFilter, setProvinceFilter] = useState('all');

  const tenders = [
    { id: 1, title: 'Road Construction', department: 'Transport', province: 'Gauteng', status: 'open', deadline: '2024-08-15' },
    { id: 2, title: 'School Supplies', department: 'Education', province: 'Western Cape', status: 'awarded', deadline: '2024-07-20' },
    { id: 3, title: 'Hospital Equipment', department: 'Health', province: 'KwaZulu-Natal', status: 'open', deadline: '2024-09-01' },
    { id: 4, title: 'IT Services', department: 'Finance', province: 'Gauteng', status: 'closed', deadline: '2024-06-30' },
  ];

  const filteredTenders = tenders
    .filter(t => provinceFilter === 'all' || t.province === provinceFilter)
    .filter(t => t.title.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="bg-gray-50 min-h-screen">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold leading-tight text-gray-900">Tender Dashboard</h1>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="mb-6 flex justify-between items-center">
          <div className="w-1/2">
            <input
              type="text"
              placeholder="Search tenders..."
              className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              onChange={e => setSearchTerm(e.target.value)}
            />
          </div>
          <div>
            <select
              className="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              onChange={e => setProvinceFilter(e.target.value)}
            >
              <option value="all">All Provinces</option>
              {[...new Set(tenders.map(t => t.province))].map(p => <option key={p} value={p}>{p}</option>)}
            </select>
          </div>
        </div>
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filteredTenders.map(tender => (
            <div key={tender.id} className="bg-white shadow-lg rounded-lg overflow-hidden transform hover:-translate-y-1 transition-transform duration-300">
              <div className="p-6">
                <div className="flex justify-between items-start">
                  <h3 className="text-xl font-semibold text-gray-800 mb-2">{tender.title}</h3>
                  <span className={`px-3 py-1 text-sm font-semibold rounded-full ${tender.status === 'open' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                    {tender.status}
                  </span>
                </div>
                <p className="text-gray-600 text-sm mb-1">{tender.department}</p>
                <p className="text-gray-600 text-sm mb-4">{tender.province}</p>
                <div className="text-sm text-gray-500">
                  <span>Deadline: {tender.deadline}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}