from app import create_app

if __name__ == "__main__":
    app = create_app()
    context = ('local.crt', 'local.key') # Certificate and key files
    app.run(debug=True, ssl_context=context)
