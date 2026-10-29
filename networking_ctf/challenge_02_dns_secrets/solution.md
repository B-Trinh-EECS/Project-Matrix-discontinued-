# DNS Secrets — Solution & Walkthrough

**Goal:** Extract flag from DNS zone file.

**Step-by-step:**
1. Open the zone file:
   ```
   cat dns/dns_zone.txt
   ```
2. Look for `TXT` records. The `flag` TXT entry contains the flag:
   ```
   flag    IN  TXT     "falcon{dn5_3xp10r3r}"
   ```
**Flag:** `falcon{dn5_3xp10r3r}`
