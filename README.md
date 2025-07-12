# Vote Count - Blockchain Voting System

A Django-based voting application that uses blockchain technology to ensure secure and transparent voting.

## Features

- Create and manage candidates
- Cast votes with blockchain verification
- View blockchain data for transparency
- Secure voting system

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment Options

### Railway (Recommended for beginners)

1. Sign up at [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway will automatically detect Django and deploy
4. Add environment variables in Railway dashboard:
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: Set to `False`
   - `ALLOWED_HOSTS`: Add your Railway domain

### Render

1. Sign up at [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn blockchain_django.wsgi:application`
5. Add environment variables in Render dashboard

### Heroku

1. Sign up at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Run these commands:
   ```bash
   heroku create your-app-name
   heroku addons:create heroku-postgresql:mini
   git push heroku main
   heroku run python manage.py migrate
   ```

## Environment Variables

Create a `.env` file for local development:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

For production, set these environment variables on your hosting platform:
- `SECRET_KEY`: A secure random string
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Your domain name
- `DATABASE_URL`: Database connection string (auto-provided by most platforms)

## Project Structure

```
Vote Count/
├── blockchain_django/     # Django project settings
├── voting/               # Main voting app
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── blockchain.py    # Blockchain implementation
│   └── templates/       # HTML templates
├── requirements.txt      # Python dependencies
├── Procfile            # Deployment configuration
└── runtime.txt         # Python version
```

## Security Notes

- Never commit your `.env` file
- Use strong secret keys in production
- Enable HTTPS in production
- Regularly update dependencies 