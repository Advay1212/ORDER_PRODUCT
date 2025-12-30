from server import app

print("Available routes:")
for route in app.routes:
    if hasattr(route, 'methods') and hasattr(route, 'path'):
        print(f"{route.methods} {route.path}")