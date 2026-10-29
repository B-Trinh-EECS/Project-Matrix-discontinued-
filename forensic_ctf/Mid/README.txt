Mid challenge — JPEG with embedded comment
Files:
- photo_with_comment.jpg : JPEG image that contains a JPEG COM (comment) segment with the flag.
Goal: extract the flag hidden in JPEG metadata / comment segments.
Hints:
- Look for JPEG markers (0xFF 0xFE) or use 'exiftool', 'strings', or a hex editor.
- The flag format is FLAG{...}.