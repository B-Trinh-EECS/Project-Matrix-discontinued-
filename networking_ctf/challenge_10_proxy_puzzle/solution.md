# Proxy Puzzle — Solution & Walkthrough

**Goal:** Decode the tunneled payload to reveal the flag.

**Step-by-step:**
1. Open the proxy log:
   ```
   cat proxy/proxy_log.txt
   ```
2. Copy the Base64-looking string and decode:
   ```
   echo 'cGluZ3M6IGZhbGNvbntwcjB4eV9kM2MwZDX9' | base64 --decode
   ```
3. The decoded output (simulated) contains the flag:
   ```
   pings: falcon{pr0xy_d3c0d3}
   ```
**Flag:** `falcon{pr0xy_d3c0d3}`
