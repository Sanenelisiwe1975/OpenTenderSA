import React from 'react';
import { useParams } from 'react-router-dom';

export default function TenderDetails() {
  const { id } = useParams();

  // Placeholder data - in a real app, you'd fetch this based on the id
  const tender = {
    id: 1,
    title: 'Road Construction',
    department: 'Transport',
    province: 'Gauteng',
    status: 'open',
    deadline: '2024-08-15',
    description: 'Construction of a 10km stretch of road in a rural area.',
    events: [
      { date: '2024-07-01', event: 'Tender Published' },
      { date: '2024-07-15', event: 'Clarification Meeting' },
    ],
  };

  return (
    <div className="bg-gray-50 min-h-screen">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold leading-tight text-gray-900">{tender.title}</h1>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="bg-white shadow-lg rounded-lg overflow-hidden p-6">
          <div className="mb-4">
            <p className="text-gray-600"><span className="font-semibold">Department:</span> {tender.department}</p>
            <p className="text-gray-600"><span className="font-semibold">Province:</span> {tender.province}</p>
            <p className="text-gray-600"><span className="font-semibold">Status:</span> {tender.status}</p>
            <p className="text-gray-600"><span className="font-semibold">Deadline:</span> {tender.deadline}</p>
          </div>
          <div className="mb-6">
            <h2 className="text-xl font-semibold mb-2">Description</h2>
            <p className="text-gray-700">{tender.description}</p>
          </div>
          <div>
            <h2 className="text-xl font-semibold mb-2">Timeline</h2>
            <ul>
              {tender.events.map((e, index) => (
                <li key={index} className="border-l-4 border-blue-500 pl-4 mb-4">
                  <p className="font-semibold">{e.event}</p>
                  <p className="text-sm text-gray-500">{e.date}</p>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
}