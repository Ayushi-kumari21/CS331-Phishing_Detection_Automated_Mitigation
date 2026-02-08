// src/pages/Dashboard.jsx (main dashboard)
import Header from '../components/Header';
import { Mail, ShieldAlert, Ban, CheckCircle2 } from 'lucide-react';

const mockStats = [
  { title: 'Emails Scanned', value: '0', icon: Mail, color: 'blue' },
  { title: 'Phishing Detected', value: '0', icon: ShieldAlert, color: 'red' },
  { title: 'Senders Blocked', value: '0', icon: Ban, color: 'purple' },
  { title: 'Mitigation Rate', value: '0', icon: CheckCircle2, color: 'green' },
];

const mockActivity = [
  { time: '0 min ago', sender: '', subject: '', risk: '', action: '' },
  { time: '0 min ago', sender: '', subject: '', risk: '', action: '' },
  { time: '0 min ago', sender: '', subject: '', risk: '', action: '' },
];

export default function Dashboard() {
  const isConnected = false; 

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <Header />

      <main className="p-6 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
          {mockStats.map((stat, i) => (
            <div
              key={i}
              className="bg-gray-900/70 border border-gray-800 rounded-xl p-6 hover:border-gray-700 transition"
            >
              <div className="flex items-center justify-between mb-4">
                <stat.icon className={`text-${stat.color}-500`} size={28} />
                <span className="text-3xl font-bold">{stat.value}</span>
              </div>
              <div className="text-gray-400 text-sm">{stat.title}</div>
            </div>
          ))}
        </div>

        {!isConnected && (
          <div className="bg-gradient-to-r from-blue-950/40 to-purple-950/30 border border-blue-900/50 rounded-xl p-8 mb-8 text-center">
            <h2 className="text-2xl font-semibold mb-3">Get Protected Now</h2>
            <p className="text-gray-300 mb-6">
              Connect your email account to start real-time phishing detection
            </p>
            <button className="px-8 py-4 bg-blue-600 hover:bg-blue-500 rounded-lg font-medium text-lg transition">
              Connect Gmail
            </button>
            <p className="text-sm text-gray-500 mt-4">
              Uses secure OAuth 2.0 • We never store your password
            </p>
          </div>
        )}

        <div className="bg-gray-900/70 border border-gray-800 rounded-xl overflow-hidden">
          <div className="p-5 border-b border-gray-800 flex justify-between items-center">
            <h2 className="text-lg font-semibold">Recent Activity</h2>
            <a href="/alerts" className="text-blue-400 hover:text-blue-300 text-sm">
              View All Alerts →
            </a>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="bg-gray-800/50">
                <tr>
                  <th className="px-6 py-4 text-left">Time</th>
                  <th className="px-6 py-4 text-left">Sender</th>
                  <th className="px-6 py-4 text-left">Subject</th>
                  <th className="px-6 py-4 text-left">Risk</th>
                  <th className="px-6 py-4 text-left">Action</th>
                </tr>
              </thead>
              <tbody>
                {mockActivity.map((item, i) => (
                  <tr key={i} className="border-t border-gray-800 hover:bg-gray-800/40 transition">
                    <td className="px-6 py-4 text-gray-400">{item.time}</td>
                    <td className="px-6 py-4">{item.sender}</td>
                    <td className="px-6 py-4 truncate max-w-xs">{item.subject}</td>
                    <td className="px-6 py-4">
                      <span
                        className={`inline-block px-3 py-1 rounded-full text-xs font-medium ${
                          item.risk === 'High'
                            ? 'bg-red-950/60 text-red-400 border border-red-800/50'
                            : 'bg-amber-950/60 text-amber-400 border border-amber-800/50'
                        }`}
                      >
                        {item.risk}
                      </span>
                    </td>
                    <td className="px-6 py-4">
                      <span className="text-green-400">{item.action}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}