# Security Best Practices

## Secret Management

### ✅ DO:
- Store secrets in `.env` file (excluded from git via `.gitignore`)
- Use environment variables in production
- Use `.env.example` as a template for team setup
- Regenerate tokens immediately if compromised
- Use GitHub Secrets for CI/CD workflows

### ❌ DON'T:
- Commit `.env` files to git
- Hardcode API keys in source code
- Share secrets in documentation or comments
- Commit secrets to any branch (they remain in history)
- Use the same token in development and production

## Setup Instructions

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anishashinde2507/real-estate-chatbot.git
   cd real-estate-chatbot
   ```

2. **Create `.env` from template:**
   ```bash
   cp backend/.env.example backend/.env
   ```

3. **Add your HuggingFace API key:**
   ```
   HUGGINGFACE_API_KEY=your_actual_api_key_here
   ```

4. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

### Production (Render, Heroku, etc.)

1. **Do NOT use `.env` file in production**
2. **Set environment variables in your platform's dashboard:**
   - Render: Settings → Environment → Add Variable
   - Heroku: Settings → Config Vars → Add
   - AWS: Secrets Manager or Systems Manager Parameter Store

3. **Example environment variables:**
   ```
   HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxx
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

## Detecting Secrets

### Scan your repository:
```bash
python3 clean_secret.py
```

### Search for specific patterns:
```bash
# Find HuggingFace tokens
git log -p --all | grep -E "hf_[A-Za-z0-9]{20,}"

# Find API keys
git log -p --all | grep -iE "api.?key.*=.*[a-z0-9]{20,}"

# Find passwords
git log -p --all | grep -iE "password.*=.*[a-z0-9]{10,}"
```

## If You Accidentally Commit a Secret

### Immediate Steps:
1. **Regenerate the token immediately** (HuggingFace dashboard)
2. **Remove it from local files:**
   ```bash
   # Edit files to remove the secret
   git add -A
   git commit -m "chore: Remove exposed secrets"
   ```

3. **Clean from git history:**
   ```bash
   # Run the cleanup script
   ./clean-history.sh      # Linux/macOS
   clean-history.bat       # Windows
   ```

4. **Force push:**
   ```bash
   git push -f origin main
   ```

5. **Notify GitHub:**
   - Go to Settings → Code security & analysis → Secret scanning
   - Review and resolve any alerts

## GitHub Settings

### Enable Push Protection:
1. Go to Settings → Code security & analysis
2. Enable "Secret scanning for push protection"
3. This prevents accidental commits of secrets

### Add Branch Protection:
1. Go to Settings → Branches
2. Add protection rule for `main` branch
3. Require status checks to pass
4. Require secret scanning to pass

## Environment Variables Reference

### Backend (.env)
```
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxx
DEBUG=True/False
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Frontend (.env or .env.local)
```
REACT_APP_API_URL=http://localhost:8000
```

### Production
```
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxx
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
REACT_APP_API_URL=https://api.yourdomain.com
```

## Token Rotation

### When to rotate:
- After accidental exposure
- Quarterly security review
- When team member leaves
- After security incident

### How to rotate:
1. Generate new token in HuggingFace dashboard
2. Update `.env` locally
3. Test application works
4. Update production environment variables
5. Delete old token from HuggingFace

## Resources

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [HuggingFace API Security](https://huggingface.co/docs/hub/security)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
