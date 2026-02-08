// src/pages/Alerts.jsx
import Header from '../components/Header';

export default function Alerts() {
  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <Header />
      
      <main className="p-6 max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold mb-8 bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
          Phishing Alerts
        </h1>
        
        <div className="bg-gray-900/70 border border-gray-800 rounded-xl p-6">
          <p className="text-gray-300">Alerts page coming soon...</p>
          <p className="text-sm text-gray-500 mt-2">
            (Table with sender, subject, risk score, status, actions will go here)
          </p>
        </div>
      </main>
    </div>
  );
}