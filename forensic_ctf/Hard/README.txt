Hard challenge — JPEG with appended ZIP archive
Files:
- photo_with_append.jpg : A valid JPEG image; a ZIP archive is appended to the end of the file containing a file 'secret.txt' with the flag.
Goal: recover the appended ZIP and extract the secret file containing the flag.
Hints:
- Try 'binwalk', 'foremost', or simply 'strings'/'tail' and 'unzip' on the file.
- A common trick: 'unzip photo_with_append.jpg' often extracts the appended archive, or use 'zip -FF' / '7z' which can find ZIP EOCD.