# Deployment Guide

## Prerequisites

- GitHub account
- Render account (https://render.com)
- Vercel account (https://vercel.com)
- HuggingFace API key (https://huggingface.co/settings/tokens)

---

## Backend Deployment (Render)

### Step 1: Prepare Environment Variables

Create a `.env` file locally:

```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key
DEBUG=False
SECRET_KEY=generate-a-strong-secret-key
ALLOWED_HOSTS=your-backend-url.onrender.com
```

Generate a strong SECRET_KEY:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Step 2: Connect Render

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select branch `main`
5. Configure:
   - **Name**: `real-estate-backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r backend/requirements.txt && python backend/manage.py collectstatic --noinput`
   - **Start Command**: `bash backend/start.sh`
   - **Plan**: Free or Starter (as needed)

### Step 3: Set Environment Variables

In Render dashboard → Settings → Environment:

```
DJANGO_SETTINGS_MODULE=realestate_api.settings
DEBUG=False
HUGGINGFACE_API_KEY=<your_api_key>
SECRET_KEY=<generated_secret_key>
ALLOWED_HOSTS=real-estate-backend.onrender.com
FRONTEND_URL=https://your-frontend.vercel.app
```

### Step 4: Deploy

1. Push to main branch
2. Render auto-deploys
3. Monitor logs in Render dashboard

---

## Frontend Deployment (Vercel)

### Step 1: Prepare Environment Variables

Create `.env.production`:

```bash
REACT_APP_API_URL=https://real-estate-backend.onrender.com
```

### Step 2: Connect Vercel

1. Go to https://vercel.com
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Configure:
   - **Framework**: React
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

### Step 3: Set Environment Variables

In Vercel dashboard → Settings → Environment Variables:

```
REACT_APP_API_URL=https://real-estate-backend.onrender.com
```

### Step 4: Deploy

1. Deploy from main branch
2. Vercel auto-deploys on push
3. Visit your frontend URL

---

## GitHub Actions CI/CD

The workflow file `.github/workflows/deploy.yml` automates:

- Backend tests on every push
- Frontend tests on every push
- Docker build and push
- Auto-deploy to Render (optional)
- Auto-deploy to Vercel (optional)

### Setup Deploy Hooks

#### For Render:

1. Go to Render Dashboard → Your Service
2. Settings → Deploy Hook
3. Copy the webhook URL
4. Go to GitHub → Repository Settings → Secrets and variables → Actions
5. Add secret: `RENDER_DEPLOY_HOOK=<webhook_url>`

#### For Vercel:

1. Go to Vercel → Project Settings → Tokens
2. Create new token
3. Go to GitHub → Repository Settings → Secrets and variables → Actions
4. Add secret: `VERCEL_TOKEN=<token>`

---

## Manual Deployment Commands

### Backend (Render CLI)

```bash
# Install Render CLI
npm i -g @render-com/cli

# Login
render login

# Deploy
render deploy --service real-estate-backend
```

### Frontend (Vercel CLI)

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy to production
vercel --prod --cwd frontend
```

---

## Troubleshooting

### Backend Issues

#### 502 Bad Gateway
- Check logs: Render Dashboard → Logs
- Ensure `start.sh` has execute permissions
- Verify `HUGGINGFACE_API_KEY` is set

#### Static files not loading
- Run: `python manage.py collectstatic --noinput`
- Verify `STATIC_ROOT` and `STATIC_URL` in settings

#### Database errors
- Render provides SQLite by default
- For PostgreSQL, upgrade plan and add database

### Frontend Issues

#### API not connecting
- Check `REACT_APP_API_URL` environment variable
- Verify backend CORS settings
- Check browser console for errors

#### Build fails
- Clear `node_modules` and `package-lock.json`
- Reinstall: `npm install`
- Check `vercel.json` configuration

### Common Fixes

```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t my-app .

# Test locally before deploying
npm run build  # Frontend
python manage.py runserver  # Backend
```

---

## Production Checklist

- [ ] `.env` is in `.gitignore`
- [ ] `DEBUG=False` in production
- [ ] `SECRET_KEY` is strong and unique
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] `HUGGINGFACE_API_KEY` is set via environment variables
- [ ] Static files are collected (`collectstatic`)
- [ ] CORS origins include frontend URL
- [ ] SSL/HTTPS is enabled
- [ ] Database backups are configured
- [ ] Logs are monitored
- [ ] Tests pass locally
- [ ] `.env.example` is up to date
- [ ] Deployment documentation is complete

---

## Monitoring & Maintenance

### Render Dashboard
- Monitor CPU and memory usage
- View real-time logs
- Set up error alerts

### Vercel Dashboard
- Monitor build times
- Track deployment history
- Set up performance monitoring

### GitHub Actions
- Monitor workflow runs
- Check test coverage
- Review deployment logs

---

## Scaling

### Backend (Render)
- Upgrade plan from Free → Starter → Standard
- Increase worker count in `start.sh`
- Add caching layer (Redis)

### Frontend (Vercel)
- Automatic CDN scaling
- Edge functions for API routes
- Image optimization

---

## Security

- Rotate API keys quarterly
- Use GitHub branch protection
- Enable secret scanning
- Monitor dependencies: `npm audit`, `pip audit`
- Set up SAST (GitHub Code Scanning)

