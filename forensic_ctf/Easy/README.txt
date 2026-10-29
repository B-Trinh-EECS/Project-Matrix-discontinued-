Easy challenge — LSB stego PNG
Files:
- lSB_stego.png : PNG image with a hidden message in the least-significant bit(s) of the pixels.
Goal: recover the hidden flag (format FLAG{...}).
Hints:
- Look at the LSB of one color channel across the pixels.
- Tools: any image viewer + a small script, or stegsolve, or use 'xxd'/'strings' on raw bytes after conversion.