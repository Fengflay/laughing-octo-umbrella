import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Enable standalone output for Docker deployment
  output: "standalone",

  async rewrites() {
    // In Docker: backend service is reachable at http://backend:8000
    // In development: use localhost:8000
    const backendUrl =
      process.env.BACKEND_URL || "http://localhost:8000";

    return [
      {
        source: "/api/:path*",
        destination: `${backendUrl}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
