\# HTTPS and Secure Redirects Configuration



\## Django Settings Adjusted



\- `SECURE\_SSL\_REDIRECT = True`: Redirects all HTTP requests to HTTPS.

\- `SECURE\_HSTS\_SECONDS = 31536000`: Instructs browsers to enforce HTTPS for 1 year.

\- `SECURE\_HSTS\_INCLUDE\_SUBDOMAINS = True`: HSTS policy applies to all subdomains.

\- `SECURE\_HSTS\_PRELOAD = True`: Enables preloading of HSTS for major browsers.

\- `SESSION\_COOKIE\_SECURE = True`: Session cookies are only sent over HTTPS.

\- `CSRF\_COOKIE\_SECURE = True`: CSRF cookies are only sent over HTTPS.

\- `X\_FRAME\_OPTIONS = 'DENY'`: Prevents site from being embedded in iframes (clickjacking protection).

\- `SECURE\_CONTENT\_TYPE\_NOSNIFF = True`: Prevents MIME type sniffing.

\- `SECURE\_BROWSER\_XSS\_FILTER = True`: Enables XSS filtering in browsers.



\## Deployment Configuration



> Ensure SSL certificates (e.g., from Let's Encrypt) are correctly installed on the server.

> For Nginx, example config:



