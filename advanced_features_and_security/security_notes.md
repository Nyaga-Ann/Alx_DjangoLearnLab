\# Security Enhancements in LibraryProject



\## ✅ Settings Configured

\- `DEBUG = False`

\- `CSRF\_COOKIE\_SECURE = True`

\- `SESSION\_COOKIE\_SECURE = True`

\- `X\_FRAME\_OPTIONS = 'DENY'`

\- `SECURE\_BROWSER\_XSS\_FILTER = True`



\## ✅ Views Secured

\- Input handled via Django Forms

\- ORM used to prevent SQL injection



\## ✅ Templates

\- `{% csrf\_token %}` added in all POST forms



\## ✅ Middleware

\- `django-csp` installed and CSP headers added



\## ✅ Testing Notes

\- Checked CSRF protection in DevTools

\- Verified CSP blocking inline scripts



