# pyPayNowSg
[![Package Repository](https://img.shields.io/pypi/v/pyPayNowSg)](https://pypi.org/project/pyPayNowSg/)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyPayNowSg)
[![Test](https://github.com/daffodilistic/pyPayNowSg/actions/workflows/test.yml/badge.svg)](https://github.com/daffodilistic/pyPayNowSg/actions/workflows/test.yml) 
![Downloads per week](https://img.shields.io/pypi/dw/pyPayNowSg)
## Generate PayNow Singapore QR codes in Python
### Summary
What it says on the tin. This is mainly for frameworks/backends which rely on
generation of a PayNow QR code without the use of NodeJS/JavaScript,
such as sending e-mails or generating PDF files.
### Documentation
This library only generates the ASCII code to be embedded in a QR
code image generator. However, there is sample code to generate the QR code 
image using Pillow. See [`tests/test_payload.py`](https://github.com/daffodilistic/pyPayNowSg/blob/d24ca3f7791a51b4b370f0a005946ccb26bca596/tests/test_payload.py)
for an example.
### TODO
- Raise Exceptions when user-specified texts/parameters exceed character limits 
as per the EMVCO specifications
- Enforce QR code version (version 11?) to fix output image size
### References
- [EMVCO QR Code Specification](https://www.emvco.com/emv-technologies/qrcodes/)
### Social
Like my work? Buy me a coffee!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/L3L5YXX1)