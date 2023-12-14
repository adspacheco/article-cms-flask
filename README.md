# Article CMS Flask

In this project, I focused primarily on deploying a Python web application using Flask, which serves as an Article Content Management System. Most of the application's code was pre-written, so my main challenge lay in the deployment process and ensuring everything functioned seamlessly in a live environment.

The application allows users to log in, create, and edit articles, with each article comprising a title, author, and body of text. My responsibilities included configuring the Azure SQL Server for data storage and setting up Azure Blob Storage for image handling. Additionally, I integrated OAuth2 for Microsoft sign-in using the msal library and implemented application logging.

## Log In Credentials

To access the app, the following credentials are pre-configured:

- **Username:** admin
- **Password:** pass

Also, the application comes with a built-in 'Sign in with Microsoft' button. I integrated OAuth2 authentication for this feature, allowing direct login into the admin account using Microsoft credentials.

## Getting Started

Here are the steps I followed to set up the project:

1. **Resource Group Creation:** I created a Resource Group in Azure.
2. **SQL Database Configuration:** I set up a user table and an article table in the Azure SQL Database, using provided scripts.
3. **Storage Container Setup:** I created a storage container named `images` in Azure for storing image files.
4. **Microsoft Sign-In Integration:** I implemented the 'Sign in with Microsoft' feature using the `msal` library and Azure Active Directory.
5. **Deployment Process:** Documented in `WRITEUP.md`. This involved making a choice between VM and App Service for deployment.
6. **Logging Implementation:** I developed a logging system to track both successful and unsuccessful login attempts.

## Dependencies

For this project, I used Python 3.7 or later. All necessary dependencies are listed in the `requirements.txt` file.

---

## Challenges and Solutions

### Implementing HTTPS

One of the key challenges I faced was implementing HTTPS for the web application. To achieve this, I generated an SSL certificate and key, then modified the Flask app's run command to use these files. This ensured that the app would run over HTTPS instead of HTTP. Here's the specific change I made in the Flask application:

```python
app.run(HOST, PORT, ssl_context=('cert.pem', 'key.pem'))
```

Along with this, I configured a reverse proxy using Nginx to redirect HTTP traffic to HTTPS, enhancing the security of the application. Here's the configuration I used in `/etc/nginx/sites-available/reverse-proxy.conf`:

```nginx
server {
    listen 80;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;

    ssl_certificate /home/user/article-cms-flask/cert.pem;
    ssl_certificate_key /home/user/article-cms-flask/key.pem;

    location / {
        proxy_pass https://localhost:5555;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection keep-alive;
        proxy_set_header Host $host;
        proxy_ssl_verify off;
        proxy_cache_bypass $http_upgrade;
    }
}
```

### Azure Blob Storage for Logging

Another challenge I tackled was setting up logging. Given that I chose a VM for deployment instead of a web app service, I needed a reliable way to handle logs. To this end, I implemented the `AzureBlobLoggingHandler` class. This custom logging handler allowed me to upload log files directly to Azure Blob Storage, ensuring that I had a robust and scalable logging solution. This approach not only secured the log data but also provided an efficient way to access and analyze logs when needed.

---

For more detailed information on setup and operation, please refer to the comprehensive project documentation or the issue tracker. Special thanks to Udacity for providing resources and additional materials, available at [Udacity's GitHub repository](https://github.com/udacity/cd1756-Azure-Applications-project).
