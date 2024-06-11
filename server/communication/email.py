from pydantic import EmailStr
from email.mime.text import MIMEText
from aiosmtplib import SMTP

from server.services.authentication import *

email_router = APIRouter()


class EmailSchema(BaseModel):

    email: EmailStr
    subject: str
    body: str
    sender:str

@email_router.post("/send-email/")
async def send_email(email: EmailSchema):
    print(f'sending {email.sender}')
    message = MIMEText(email.body)
    message["From"] = email.sender
    message["To"] = email.email
    message["Subject"] = email.subject

    try:
        await send_email_async(message)
        return {"message": "Email has been sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

async def send_email_async(message):
    smtp = SMTP(hostname="smtp.gmail.com", port=587, start_tls=True)
    await smtp.connect()
    # await smtp.starttls()
    await smtp.login("alain.verhoeven1@gmail.com", "gobrpsuqbglhwodn")
    await smtp.send_message(message)
    await smtp.quit()