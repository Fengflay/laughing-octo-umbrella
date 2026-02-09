/**
 * Client-side authentication utilities.
 *
 * Stores JWT token and user info in localStorage.
 * Provides helpers for login/register/logout/getMe.
 */

const TOKEN_KEY = "auth_token";
const USER_KEY = "auth_user";

export interface AuthUser {
  user_id: string;
  email: string;
  display_name: string;
  credits: number;
}

export interface AuthResponse extends AuthUser {
  token: string;
}

// ---------------------------------------------------------------------------
// Token management
// ---------------------------------------------------------------------------

export function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string): void {
  localStorage.setItem(TOKEN_KEY, token);
}

export function clearAuth(): void {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
}

export function getStoredUser(): AuthUser | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem(USER_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

export function setStoredUser(user: AuthUser): void {
  localStorage.setItem(USER_KEY, JSON.stringify(user));
}

export function isLoggedIn(): boolean {
  return !!getToken();
}

// ---------------------------------------------------------------------------
// Auth headers helper
// ---------------------------------------------------------------------------

export function authHeaders(): Record<string, string> {
  const token = getToken();
  if (!token) return {};
  return { Authorization: `Bearer ${token}` };
}

// ---------------------------------------------------------------------------
// API calls
// ---------------------------------------------------------------------------

const API_BASE = "/api/auth";

export async function login(email: string, password: string): Promise<AuthResponse> {
  const res = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(data.detail || "登入失敗");
  }

  const data: AuthResponse = await res.json();
  setToken(data.token);
  setStoredUser({
    user_id: data.user_id,
    email: data.email,
    display_name: data.display_name,
    credits: data.credits,
  });
  return data;
}

export async function register(
  email: string,
  password: string,
  displayName: string = "",
): Promise<AuthResponse> {
  const res = await fetch(`${API_BASE}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, display_name: displayName }),
  });

  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(data.detail || "註冊失敗");
  }

  const data: AuthResponse = await res.json();
  setToken(data.token);
  setStoredUser({
    user_id: data.user_id,
    email: data.email,
    display_name: data.display_name,
    credits: data.credits,
  });
  return data;
}

export async function getMe(): Promise<AuthUser | null> {
  const token = getToken();
  if (!token) return null;

  const res = await fetch(`${API_BASE}/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });

  if (!res.ok) {
    if (res.status === 401) {
      clearAuth();
    }
    return null;
  }

  const data = await res.json();
  const user: AuthUser = {
    user_id: data.user_id,
    email: data.email,
    display_name: data.display_name,
    credits: data.credits,
  };
  setStoredUser(user);
  return user;
}

export function logout(): void {
  clearAuth();
  // Redirect to home page
  if (typeof window !== "undefined") {
    window.location.href = "/";
  }
}
