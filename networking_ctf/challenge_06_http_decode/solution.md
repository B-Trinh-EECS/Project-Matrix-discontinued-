# HTTP Decode — Solution & Walkthrough

**Goal:** Decode header value to reveal the flag.

**Step-by-step:**
1. Open the headers:
   ```
   cat http/headers.txt
   ```
2. Note `X-Secret: ZmFjbG9ue2gzNGQzcl9tM2NzQGczfQ==`
3. Decode from Base64:
   ```
   echo 'ZmFjbG9ue2gzNGQzcl9tM2NzQGczfQ==' | base64 --decode
   ```
   Output:
   ```
   falcon{h34d3r_m3ss@g3}
   ```
**Flag:** `falcon{h34d3r_m3ss@g3}`
