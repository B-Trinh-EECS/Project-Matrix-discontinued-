# Packet Hunt — Solution & Walkthrough

**Goal:** Find the flag inside an HTTP request.

**Step-by-step:**
1. Open `captures/packet_hunt_http.txt` in a text editor or run:
   ```
   cat captures/packet_hunt_http.txt | less
   ```
2. Search for "falcon{" or suspicious GET requests:
   ```
   grep -n "falcon" -R .
   ```
3. You will see the second GET contains the flag:
   ```
   GET /secret/pa55w0rd/falcon{p@ck3t_sn1ff3r} HTTP/1.1
   ```
**Flag:** `falcon{p@ck3t_sn1ff3r}`
