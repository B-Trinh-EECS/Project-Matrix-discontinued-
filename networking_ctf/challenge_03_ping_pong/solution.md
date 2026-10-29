# Ping Pong — Solution & Walkthrough

**Goal:** Find the flag encoded by ICMP sequence behavior.

**Step-by-step:**
1. Inspect the file:
   ```
   cat icmp/icmp_sequences.txt
   ```
2. Note the comment indicating a special response for `seq=5`.
3. That line includes the flag:
   ```
   seq=5 -> "falcon{1cmp_r3sp0ns3}"
   ```
**Flag:** `falcon{1cmp_r3sp0ns3}`
