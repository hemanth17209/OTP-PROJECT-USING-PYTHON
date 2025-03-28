# OTP Verification Script

This script generates a One-Time Password (OTP) and sends it via email for user verification. The user must enter the received OTP to complete the verification process.

## Prerequisites
- Python 3.x installed
- An active Gmail account
- `smtplib` and `email` modules (included in Python's standard library)

## How It Works
1. The script generates a random 4-digit OTP.
2. The OTP is sent via email to the recipient's email address.
3. The user inputs the OTP received in their email.
4. The script validates the OTP and confirms successful verification or failure.

## Installation & Setup
1. Ensure Python is installed on your system.
2. Enable **Less Secure Apps Access** in your Gmail account settings (if using a regular Gmail account).
3. Modify the sender email credentials in the script:
   ```python
   msg["From"] = "your_email@gmail.com"
   server.login("your_email@gmail.com", "your_app_password")
   ```
   **Note:** Instead of using your Gmail password directly, use an **App Password** for security.

## Usage
1. Run the script using:
   ```sh
   python otp_verification.py
   ```
2. Enter the recipient's email address when prompted.
3. Check the recipient's email inbox for the OTP.
4. Enter the received OTP when prompted.
5. The script will confirm if the OTP is correct.

## Security Warning
- Never hardcode your email password in the script. Use an **App Password** instead.
- Do not share your credentials with anyone.
- Consider using an environment variable or a configuration file for storing sensitive information.

## Example
```
Enter Email Id: user@example.com
enter OTP RECEIVED BY user@example.com: 1234
OTP Verification Success
```

## License
This script is provided as-is for educational purposes. Modify and use it at your own discretion.

