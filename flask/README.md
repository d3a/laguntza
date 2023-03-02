# flask

## Dependencias
### Obligatorias
- Werkzeug implements WSGI, the standard Python interface between applications and servers.
- Jinja is a template language that renders the pages your application serves.
- MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
- ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
- Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

### Opcionales
- Blinker provides support for Signals.
- python-dotenv enables support for Environment Variables From dotenv when running flask commands.
- Watchdog provides a faster, more efficient reloader for the development server.
- gevent o eventlet
  - greenlet 1.0+
  - PyPy 7.3.7+

## Referencias
- [Flask Documentation (2.2.x)](https://flask.palletsprojects.com/en/2.2.x/)