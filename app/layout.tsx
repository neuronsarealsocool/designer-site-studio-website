import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || "http://localhost:3000"),
  title: "Designer Site Studio — Website prompts, assets & inspiration",
  description: "An open library of high-end website prompts, design assets and references. Find your direction and build with Codex, Claude or your coding agent.",
  openGraph: {title: "Designer Site Studio", siteName: "Designer Site Studio", description: "High-end website prompts, design assets and inspiration. Copy a prompt, adapt a reference, or make the whole website your own.", type: "website"},
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
