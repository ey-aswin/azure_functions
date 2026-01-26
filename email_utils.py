
def generate_todo_ack_email(title: str, description: str) -> str:
    """
    Generates an HTML email acknowledging a submitted To‑Do item.

    Args:
        title (str): Title of the To‑Do item
        description (str): Description of the To‑Do item

    Returns:
        str: HTML email content
    """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To‑Do Submitted</title>
        <style>
            body {{
                font-family: Arial, Helvetica, sans-serif;
                background-color: #f5f7fa;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 40px auto;
                background-color: #ffffff;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            }}
            .header {{
                background-color: #4f46e5;
                color: #ffffff;
                padding: 20px;
                text-align: center;
            }}
            .content {{
                padding: 24px;
                color: #333333;
            }}
            .item-box {{
                background-color: #f1f5f9;
                padding: 16px;
                border-radius: 6px;
                margin-top: 12px;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #6b7280;
                padding: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>✅ To‑Do Submitted Successfully</h2>
            </div>

            <div class="content">
                <p>Hello,</p>
                <p>Your To‑Do item has been successfully submitted with the following details:</p>

                <div class="item-box">
                    <p><strong>Title:</strong> {title}</p>
                    <p><strong>Description:</strong></p>
                    <p>{description}</p>
                </div>

                <p style="margin-top: 20px;">
                    You can review or update this task anytime from your dashboard.
                </p>

                <p>Regards,<br><strong>Task Management Team</strong></p>
            </div>

            <div class="footer">
                © 2026 Task Management System. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """

    return html

def generate_todo_not_found_email() -> str:
    """
    Generates an HTML email indicating that the To‑Do item was not found
    or an error occurred.

    Returns:
        str: HTML email content
    """

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Something Went Wrong</title>
        <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
                background-color: #f5f7fa;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 40px auto;
                background-color: #ffffff;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            }
            .header {
                background-color: #dc2626;
                color: #ffffff;
                padding: 20px;
                text-align: center;
            }
            .content {
                padding: 24px;
                color: #333333;
                text-align: center;
            }
            .footer {
                text-align: center;
                font-size: 12px;
                color: #6b7280;
                padding: 16px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>⚠️ Something Went Wrong</h2>
            </div>

            <div class="content">
                <p>
                    We were unable to find the requested To‑Do item.
                </p>

                <p>
                    <strong>Please check the application logs</strong> for more details and try again.
                </p>

                <p style="margin-top: 20px;">
                    If the issue persists, contact the system administrator.
                </p>

                <p>
                    Regards,<br>
                    <strong>Task Management Team</strong>
                </p>
            </div>

            <div class="footer">
                © 2026 Task Management System. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """

    return html
