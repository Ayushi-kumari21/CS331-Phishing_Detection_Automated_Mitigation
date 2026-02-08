// src/pages/Settings.jsx
import Header from '../components/Header';
import { useAuth } from '../context/AuthContext';

export default function Settings() {
  const { logout } = useAuth();

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <Header />
      <main className="p-6 max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold mb-8">Settings</h1>
        
        <div className="space-y-8">
          <section className="bg-gray-900/70 border border-gray-800 rounded-xl p-6">
            <h2 className="text-xl font-semibold mb-4">Connected Accounts</h2>
            <p className="text-gray-400">No email accounts connected yet.</p>
          </section>

          <section className="bg-gray-900/70 border border-gray-800 rounded-xl p-6">
            <h2 className="text-xl font-semibold mb-4">Account Actions</h2>
            <button 
              onClick={logout}
              className="px-6 py-3 bg-red-600/80 hover:bg-red-600 rounded-lg font-medium transition"
            >
              Log Out
            </button>
          </section>
        </div>
      </main>
    </div>
  );
}