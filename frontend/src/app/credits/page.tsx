"use client";

import { useEffect, useState } from "react";
import AuthGuard from "@/components/AuthGuard";
import { useApp } from "@/lib/store";

interface Transaction {
  id: number;
  amount: number;
  balance_after: number;
  description: string;
  job_id: string | null;
  created_at: string;
}

interface TransactionList {
  transactions: Transaction[];
  total: number;
  page: number;
  page_size: number;
}

async function fetchBalance(token: string) {
  const res = await fetch("/api/credits/balance", {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Failed to fetch balance");
  return res.json();
}

async function fetchTransactions(token: string, page = 1): Promise<TransactionList> {
  const res = await fetch(`/api/credits/transactions?page=${page}&page_size=20`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Failed to fetch transactions");
  return res.json();
}

function CreditsContent() {
  const { user } = useApp();
  const [balance, setBalance] = useState<number | null>(null);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [totalTx, setTotalTx] = useState(0);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("auth_token");
    if (!token) return;

    setLoading(true);
    Promise.all([fetchBalance(token), fetchTransactions(token, page)])
      .then(([bal, txList]) => {
        setBalance(bal.credits);
        setTransactions(txList.transactions);
        setTotalTx(txList.total);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [page]);

  const totalPages = Math.ceil(totalTx / 20);

  const formatDate = (iso: string) => {
    const d = new Date(iso);
    return `${d.getFullYear()}/${String(d.getMonth() + 1).padStart(2, "0")}/${String(d.getDate()).padStart(2, "0")} ${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="flex items-center gap-3 text-gray-400">
          <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
          </svg>
          <span className="text-sm">載入中...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6 max-w-2xl mx-auto">
      {/* Balance card */}
      <div className="bg-gradient-to-br from-amber-50 to-orange-50 rounded-2xl border border-amber-200/60 p-6 shadow-sm">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm text-amber-600 font-medium">目前餘額</p>
            <p className="text-4xl font-bold text-amber-700 mt-1">
              {balance ?? 0}
              <span className="text-lg font-medium ml-1">點</span>
            </p>
          </div>
          <div className="w-14 h-14 bg-amber-100 rounded-2xl flex items-center justify-center">
            <svg className="w-7 h-7 text-amber-500" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.736 6.979C9.208 6.193 9.696 6 10 6c.304 0 .792.193 1.264.979a1 1 0 001.715-1.029C12.279 4.784 11.232 4 10 4s-2.279.784-2.979 1.95c-.285.475-.507 1-.67 1.55H6a1 1 0 000 2h.013a9.358 9.358 0 000 1H6a1 1 0 100 2h.351c.163.55.385 1.075.67 1.55C7.721 15.216 8.768 16 10 16s2.279-.784 2.979-1.95a1 1 0 10-1.715-1.029c-.472.786-.96.979-1.264.979-.304 0-.792-.193-1.264-.979a5.95 5.95 0 01-.4-.821h2.564a1 1 0 000-2H8.057a7.224 7.224 0 010-1h3.843a1 1 0 000-2H8.336c.12-.292.264-.569.4-.821z" />
            </svg>
          </div>
        </div>
        <div className="mt-4 flex items-center gap-4 text-xs text-amber-600/80">
          <span>1 點 = 1 張圖片</span>
          <span>·</span>
          <span>重新生成 = 1 點</span>
          <span>·</span>
          <span>變體 = 4 點</span>
        </div>
      </div>

      {/* Transactions */}
      <div className="bg-white rounded-2xl border border-gray-200/80 shadow-sm overflow-hidden">
        <div className="px-5 py-4 border-b border-gray-100">
          <h2 className="text-base font-semibold text-gray-800">交易明細</h2>
          <p className="text-xs text-gray-400 mt-0.5">共 {totalTx} 筆記錄</p>
        </div>

        {transactions.length === 0 ? (
          <div className="px-5 py-12 text-center text-gray-400 text-sm">
            尚無交易記錄
          </div>
        ) : (
          <div className="divide-y divide-gray-50">
            {transactions.map((tx) => (
              <div key={tx.id} className="px-5 py-3 flex items-center justify-between hover:bg-gray-50/50 transition-colors">
                <div className="flex-1 min-w-0">
                  <p className="text-sm text-gray-700 truncate">{tx.description}</p>
                  <p className="text-[11px] text-gray-400 mt-0.5">{formatDate(tx.created_at)}</p>
                </div>
                <div className="flex items-center gap-3 ml-4">
                  <span
                    className={`text-sm font-semibold tabular-nums ${
                      tx.amount > 0 ? "text-green-600" : "text-red-500"
                    }`}
                  >
                    {tx.amount > 0 ? "+" : ""}{tx.amount}
                  </span>
                  <span className="text-[11px] text-gray-400 w-12 text-right tabular-nums">
                    餘 {tx.balance_after}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Pagination */}
        {totalPages > 1 && (
          <div className="px-5 py-3 border-t border-gray-100 flex items-center justify-between">
            <button
              onClick={() => setPage((p) => Math.max(1, p - 1))}
              disabled={page <= 1}
              className="text-xs px-3 py-1.5 rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
            >
              上一頁
            </button>
            <span className="text-xs text-gray-400">
              {page} / {totalPages}
            </span>
            <button
              onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
              disabled={page >= totalPages}
              className="text-xs px-3 py-1.5 rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
            >
              下一頁
            </button>
          </div>
        )}
      </div>

      {/* Back link */}
      <div className="text-center">
        <a href="/" className="text-sm text-gray-400 hover:text-blue-500 transition-colors">
          ← 返回首頁
        </a>
      </div>
    </div>
  );
}

export default function CreditsPage() {
  return (
    <AuthGuard required>
      <CreditsContent />
    </AuthGuard>
  );
}
