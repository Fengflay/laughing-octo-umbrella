"use client";

import { useCallback, useEffect, useState } from "react";
import AuthGuard from "@/components/AuthGuard";

interface ProjectItem {
  id: string;
  name: string;
  description: string;
  brand_color: string | null;
  default_product_type: string | null;
  default_style: string | null;
  is_archived: boolean;
  created_at: string;
  updated_at: string;
}

const PRODUCT_TYPE_NAMES: Record<string, string> = {
  bags: "包包", jewelry: "飾品", clothing: "服飾", shoes: "鞋子",
  electronics: "3C 電子", beauty: "美妝", home: "居家", toys: "玩具",
  sports: "運動", food: "食品", stationery: "文具", pets: "寵物",
  automotive: "汽車", phones: "手機", travel: "旅行", fashion_acc: "配飾",
  kitchenware: "廚房", health: "保健", hobbies: "興趣", motorcycle: "機車",
};

function ProjectsContent() {
  const [projects, setProjects] = useState<ProjectItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreate, setShowCreate] = useState(false);
  const [newName, setNewName] = useState("");
  const [newDesc, setNewDesc] = useState("");
  const [newType, setNewType] = useState("");
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const token = typeof window !== "undefined" ? localStorage.getItem("auth_token") : null;

  const loadProjects = useCallback(async () => {
    try {
      const res = await fetch("/api/projects", {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) {
        const data = await res.json();
        setProjects(data.projects);
      }
    } catch {
      // ignore
    } finally {
      setLoading(false);
    }
  }, [token]);

  useEffect(() => {
    loadProjects();
  }, [loadProjects]);

  const handleCreate = async () => {
    if (!newName.trim()) return;
    setCreating(true);
    setError(null);

    try {
      const res = await fetch("/api/projects", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          name: newName.trim(),
          description: newDesc,
          default_product_type: newType || null,
        }),
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.detail || "建立失敗");
      }

      setNewName("");
      setNewDesc("");
      setNewType("");
      setShowCreate(false);
      loadProjects();
    } catch (err) {
      setError(err instanceof Error ? err.message : "建立失敗");
    } finally {
      setCreating(false);
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm("確定要刪除此專案嗎？")) return;

    try {
      await fetch(`/api/projects/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });
      loadProjects();
    } catch {
      // ignore
    }
  };

  const formatDate = (iso: string) => {
    const d = new Date(iso);
    return `${d.getFullYear()}/${d.getMonth() + 1}/${d.getDate()}`;
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64 text-gray-400 text-sm">
        載入中...
      </div>
    );
  }

  return (
    <div className="space-y-6 max-w-3xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-gray-800">專案管理</h1>
          <p className="text-sm text-gray-400 mt-1">管理你的產品專案，設定預設品類和風格</p>
        </div>
        <div className="flex items-center gap-2">
          <a href="/" className="text-sm text-gray-400 hover:text-blue-500 transition-colors">← 返回</a>
          <button
            onClick={() => setShowCreate(!showCreate)}
            className="px-4 py-2 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 transition-colors"
          >
            + 新專案
          </button>
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded-xl text-sm">
          {error}
        </div>
      )}

      {/* Create form */}
      {showCreate && (
        <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm space-y-4 animate-slide-up">
          <h2 className="text-base font-semibold text-gray-800">建立新專案</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs text-gray-500 mb-1">專案名稱 *</label>
              <input
                value={newName}
                onChange={(e) => setNewName(e.target.value)}
                placeholder="例如：2024 春季新品"
                className="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/30 focus:border-blue-400"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-500 mb-1">預設品類</label>
              <select
                value={newType}
                onChange={(e) => setNewType(e.target.value)}
                className="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/30 focus:border-blue-400"
              >
                <option value="">不指定</option>
                {Object.entries(PRODUCT_TYPE_NAMES).map(([id, name]) => (
                  <option key={id} value={id}>{name}</option>
                ))}
              </select>
            </div>
          </div>
          <div>
            <label className="block text-xs text-gray-500 mb-1">描述</label>
            <textarea
              value={newDesc}
              onChange={(e) => setNewDesc(e.target.value)}
              placeholder="簡短描述此專案..."
              rows={2}
              className="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/30 focus:border-blue-400 resize-none"
            />
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handleCreate}
              disabled={creating || !newName.trim()}
              className="px-6 py-2 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 disabled:opacity-50 transition-colors"
            >
              {creating ? "建立中..." : "建立"}
            </button>
            <button
              onClick={() => setShowCreate(false)}
              className="px-6 py-2 bg-gray-100 text-gray-600 text-sm rounded-xl hover:bg-gray-200 transition-colors"
            >
              取消
            </button>
          </div>
        </div>
      )}

      {/* Projects list */}
      {projects.length === 0 ? (
        <div className="bg-white rounded-2xl border border-gray-200/80 p-12 shadow-sm text-center">
          <div className="w-16 h-16 bg-gray-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
            <svg className="w-8 h-8 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
            </svg>
          </div>
          <p className="text-gray-500 text-sm">尚無專案，點擊「+ 新專案」開始</p>
        </div>
      ) : (
        <div className="grid gap-4">
          {projects.map((project) => (
            <div
              key={project.id}
              className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm hover:border-blue-200 transition-colors"
            >
              <div className="flex items-start justify-between">
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <h3 className="text-base font-semibold text-gray-800 truncate">{project.name}</h3>
                    {project.brand_color && (
                      <div
                        className="w-4 h-4 rounded-full border border-gray-200"
                        style={{ backgroundColor: project.brand_color }}
                      />
                    )}
                  </div>
                  {project.description && (
                    <p className="text-sm text-gray-400 mt-1 truncate">{project.description}</p>
                  )}
                  <div className="flex items-center gap-3 mt-2 text-xs text-gray-400">
                    {project.default_product_type && (
                      <span className="bg-gray-100 px-2 py-0.5 rounded-full">
                        {PRODUCT_TYPE_NAMES[project.default_product_type] || project.default_product_type}
                      </span>
                    )}
                    {project.default_style && (
                      <span className="bg-purple-50 text-purple-500 px-2 py-0.5 rounded-full">
                        {project.default_style}
                      </span>
                    )}
                    <span>建立於 {formatDate(project.created_at)}</span>
                  </div>
                </div>
                <button
                  onClick={() => handleDelete(project.id)}
                  className="text-gray-300 hover:text-red-500 transition-colors ml-3"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default function ProjectsPage() {
  return (
    <AuthGuard required>
      <ProjectsContent />
    </AuthGuard>
  );
}
