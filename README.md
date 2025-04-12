# keep-render-awake

A Python script to prevent a Render-hosted backend API from sleeping due to inactivity by sending periodic requests. Designed for deployment on AWS Lambda or a server. It also sends a weekly reminder email to confirm the script is running.

## 🛠️ Features

- Sends HTTP requests every 5 minutes to keep a specified URL active
- Optional email notification once per week
- Easy to deploy on AWS Lambda or any server with Python

## 📦 Requirements

- Python 3
- `requests`
- `schedule`
- `python-dotenv`
- `smtplib` (built-in)
- `beautifulsoup4` (used in the current script, though not essential)

## 📦 Dependencies

Install required Python packages with:

```bash
pip install requests beautifulsoup4 schedule python-dotenv
```
# 🔧 Setup

1. Clone this repo.

2. Create a `.env` file in the root with:

    ```env
    EMAIL=your-email@gmail.com  
    PASSWORD=your-app-password
    ```

    💡 *Use an App Password if you're using Gmail.*

3. Modify the script:

    - `URL` – the endpoint to keep alive (e.g., your Render backend)
    - `TO_EMAIL` – the recipient of weekly status emails

---

# 🚀 Deployment Options

- ✅ **EC2 Instance** (Used in this setup):  
  Keep the script running in the background using `nohup` or `screen`.

    ```bash
    nohup python script.py &
    ```

- **AWS Lambda** + **EventBridge**:  
  Schedule it to run every 5 minutes as a serverless function.

- **Docker Container**:  
  Build and run the script as a containerized app.
---

# 🧠 Notes

- `check_page()` currently does not perform any check logic; you can add that if needed.  
- Email functionality is optional and runs weekly.

---

# 📫 Contact

Feel free to open an issue or PR if you'd like to improve the script.

---

# 📄 License

MIT
