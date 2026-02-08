// src/pages/ConnectEmail.jsx
import Header from '../components/Header';

export default function ConnectEmail() {
  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      <Header />
      <main className="p-6 max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Connect Email Account</h1>
        <div className="bg-gray-900/70 border border-gray-800 rounded-xl p-8 text-center">
          <p className="text-xl mb-6">Securely connect your inbox</p>
          <button className="px-8 py-4 bg-blue-600 hover:bg-blue-500 rounded-lg font-medium">
            Connect Gmail
          </button>
          <p className="text-sm text-gray-500 mt-4">
            Uses OAuth 2.0 – We never store your password
          </p>
        </div>
      </main>
    </div>
  );
}