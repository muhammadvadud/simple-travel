from core.services.email_send_code import SMTPEmailService
service = SMTPEmailService()
res = service.send_email("gmuhammadvadud@gmail.com", "Tasdiqlash kodi", "Sizning kod: 1234")
print(res)


