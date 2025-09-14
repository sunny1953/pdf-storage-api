# PDF Storage API - Deployment Guide

## 🚀 Deploy to Railway (Recommended - Free)

### Step 1: Prepare Your Code
1. Make sure all files are in your project folder
2. Your MongoDB connection string is already configured

### Step 2: Deploy to Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up/Login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Connect your GitHub account and select this repository
5. Railway will automatically detect it's a Python app

### Step 3: Set Environment Variables
In Railway dashboard:
1. Go to your project → Variables tab
2. Add this environment variable:
   - **Key**: `MONGODB_URI`
   - **Value**: `mongodb+srv://its4eminence1:Bharadwaj11042004@sunny.of8x3cx.mongodb.net/?retryWrites=true&w=majority&appName=Sunny&ssl=true&ssl_cert_reqs=CERT_NONE`

### Step 4: Deploy
1. Railway will automatically build and deploy
2. You'll get a URL like: `https://your-app-name.railway.app`
3. Your API will be available at this URL

## 🌐 API Endpoints

Once deployed, your friend can use these endpoints:

### Base URL: `https://your-app-name.railway.app`

- `GET /` - Web interface
- `GET /health` - Health check
- `GET /docs` - API documentation
- `POST /upload` - Upload PDF
- `GET /pdfs` - List all PDFs
- `GET /view/{pdf_id}` - View PDF
- `GET /download/{pdf_id}` - Download PDF
- `DELETE /pdf/{pdf_id}` - Delete PDF

## 📱 For Your Friend

Your friend can:
1. **Use the web interface**: Visit `https://your-app-name.railway.app`
2. **Use API directly**: Use the endpoints above
3. **View API docs**: Visit `https://your-app-name.railway.app/docs`

## 🔒 Security Notes

- The API has CORS enabled for cross-origin requests
- MongoDB connection is secured with environment variables
- All PDFs are stored in your MongoDB Atlas cloud

## 🆓 Free Tier Limits

Railway free tier includes:
- 500 hours of usage per month
- 1GB RAM
- 1GB storage
- Perfect for personal use!

## 🛠️ Alternative: Deploy to Render

If Railway doesn't work, you can also deploy to Render:
1. Go to [Render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repo
4. Use the same environment variables
5. Deploy!

## 📞 Support

If you need help with deployment, check:
- Railway documentation: https://docs.railway.app
- Render documentation: https://render.com/docs
