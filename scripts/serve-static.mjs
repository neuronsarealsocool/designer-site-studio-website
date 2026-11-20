import http from "node:http";
import path from "node:path";
import { readFile, stat } from "node:fs/promises";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../out/", import.meta.url));
const port = Number(process.env.PORT || 3000);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("Invalid PORT");
const types = { ".html":"text/html; charset=utf-8", ".js":"text/javascript; charset=utf-8", ".css":"text/css; charset=utf-8", ".json":"application/json", ".txt":"text/plain; charset=utf-8", ".md":"text/markdown; charset=utf-8", ".svg":"image/svg+xml", ".webp":"image/webp", ".png":"image/png", ".jpg":"image/jpeg", ".zip":"application/zip", ".woff2":"font/woff2" };
await stat(path.join(root, "index.html")).catch(() => { throw new Error("Run npm run build first"); });
http.createServer(async (request, response) => {
  try {
    if (!["GET", "HEAD"].includes(request.method)) { response.writeHead(405).end(); return; }
    const url = new URL(request.url, "http://localhost");
    const file = path.resolve(root, "." + decodeURIComponent(url.pathname));
    const relative = path.relative(root, file);
    if (relative.startsWith("..") || path.isAbsolute(relative)) { response.writeHead(403).end(); return; }
    const resolved = (await stat(file)).isDirectory() ? path.join(file, "index.html") : file;
    const data = await readFile(resolved);
    response.writeHead(200, { "Content-Type": types[path.extname(resolved)] || "application/octet-stream", "Content-Length": data.length });
    response.end(request.method === "HEAD" ? undefined : data);
  } catch { response.writeHead(404).end("Not found"); }
}).listen(port, "127.0.0.1", () => console.log(`Designer Site Studio: http://127.0.0.1:${port}`));
