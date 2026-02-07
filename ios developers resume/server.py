import http.server
import socketserver
import json
import os
import urllib.parse

PORT = 8000
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle API request for resume list
        if self.path == '/api/resumes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            files = []
            try:
                # List all files in current directory
                for filename in os.listdir(DIRECTORY):
                    # Filter for likely resume formats
                    if filename.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')) and filename != "index.html":
                         # Extract name from filename (remove extension and " IOS" suffix if present)
                        name = os.path.splitext(filename)[0]
                        name = name.replace(" IOS", "").replace("_", " ")
                        
                        files.append({
                            "file": filename,
                            "name": name
                        })
                
                # Sort alphabetically
                files.sort(key=lambda x: x['name'])
                
                self.wfile.write(json.dumps(files).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())
            return

        # Serve static files (index.html, PDFs, images)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

print(f"Server started at http://localhost:{PORT}")
print("Press Ctrl+C to stop")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
