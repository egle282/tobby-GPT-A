```python
"""
mail_inbox.py
-------------
Подключается к IMAP-серверу и сообщает оператору бота о новых входящих письмах.
"""
import os, imapclient, pyzmail, time
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.yandex.ru")
IMAP_USER = os.getenv("IMAP_USER")
IMAP_PASS = os.getenv("IMAP_PASS")
IMAP_FOLDER = os.getenv("IMAP_FOLDER", "INBOX")
ADMIN_IDS = [int(s) for s in os.getenv("ADMIN_IDS", "123456789").split(",")]

class MailInbox:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn
        self.notified_uids = set()
      def check_mail(self):
        if not self.feature_on('mail_inbox'):
            return
        with imapclient.IMAPClient(IMAP_SERVER) as client:
            client.login(IMAP_USER, IMAP_PASS)
            client.select_folder(IMAP_FOLDER)
            messages = client.search('UNSEEN')
            for uid in messages:
                if uid not in self.notified_uids:
                    raw = client.fetch([uid], ['BODY[]', 'FLAGS'])
                    msg = pyzmail.PyzMessage.factory(raw[uid][b'BODY[]'])
                    subj = msg.get_subject()
                    text = msg.text_part.get_payload().decode(errors="ignore") if msg.text_part else ''
                    for a in ADMIN_IDS:
                        self.bot.send_message(a, f"New mail: {subj}\n{text[:1000]}")
                    self.notified_uids.add(uid)
            client.logout()

    def handle(self, msg):
        return False  # Только по расписанию
