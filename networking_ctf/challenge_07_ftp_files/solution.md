# FTP Files — Solution & Walkthrough

**Goal:** Retrieve the flag file from the FTP root.

**Step-by-step:**
1. List the FTP root (simulated here as `ftp/ftp_root`).
   ```
   ls -la ftp/ftp_root
   ```
2. Display the flag file:
   ```
   cat ftp/ftp_root/flag.txt
   ```
   Output:
   ```
   falcon{ftp_4cc3ss_gr@nt3d}
   ```
**Flag:** `falcon{ftp_4cc3ss_gr@nt3d}`
