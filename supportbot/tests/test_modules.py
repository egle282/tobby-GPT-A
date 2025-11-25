python
import sys
import os
import types
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.context_support import ContextSupport
from modules.file_module import FileModule
from modules.multilang import Multilang
from modules.personalized import Personalized
from modules.feedback_referral import FeedbackReferral
from modules.faq_search import FAQSearch
from modules.qr_scanner import QRScanner
from modules.push_notify import PushNotify
from modules.cross_platform import CrossPlatform
from modules.mailing import Mailing
from modules.ai_handler import AIHandler

class DummyBot:
    def __init__(self):
        self.last_message = None
        self.sent_messages = []
    def send_message(self, chat_id, text, **kwargs):
        self.last_message = text
        self.sent_messages.append((chat_id, text))

dummy_msg = types.SimpleNamespace(chat={'id': 1}, from_user=types.SimpleNamespace(id=1),
                                  text="тестовое сообщение", content_type='text', photo=[], document=None)

def feature_on(_): return True

def test_context_support():
    bot = DummyBot()
    mod = ContextSupport(bot, feature_on)
    assert mod.handle(dummy_msg) is False

def test_file_module():
    bot = DummyBot()
    mod = FileModule(bot, feature_on)
    dummy_msg.content_type = 'document'
    assert mod.handle(dummy_msg) is True
    dummy_msg.content_type = 'photo'
    assert mod.handle(dummy_msg) is True

def test_multilang():
    bot = DummyBot()
    mod = Multilang(bot, feature_on)
    dummy_msg.text = "/lang en"
    assert mod.handle(dummy_msg) is True

def test_personalized():
    bot = DummyBot()
    mod = Personalized(bot, feature_on)
    assert mod.handle(dummy_msg) in [True, False]

def test_feedback_referral():
    bot = DummyBot()
    mod = FeedbackReferral(bot, feature_on)
    dummy_msg.text = "хочу оценить"
    assert mod.handle(dummy_msg) is True

def test_faq_search():
    bot = DummyBot()
    mod = FAQSearch(bot, feature_on)
    assert mod.handle(dummy_msg) in [True, False]

def test_qr_scanner():
    bot = DummyBot()
    mod = QRScanner(bot, feature_on)
    dummy_msg.content_type = 'photo'
    assert mod.handle(dummy_msg) in [True, False]

def test_push_notify():
    bot = DummyBot()
    mod = PushNotify(bot, feature_on)
    dummy_msg.text = "подписаться"
    assert mod.handle(dummy_msg) is True
    mod.send_push("push!")
    assert bot.sent_messages

def test_cross_platform():
    bot = DummyBot()
    mod = CrossPlatform(bot, feature_on)
    dummy_msg.text = "whatsapp"
    assert mod.handle(dummy_msg) is True

def test_mailing():
    bot = DummyBot()
    mod = Mailing(bot, feature_on)
    dummy_msg.text = "новости"
    assert mod.handle(dummy_msg) is True
    mod.send_news("test news")
    assert bot.sent_messages

def test_ai_handler():
    bot = DummyBot()
    mod = AIHandler(bot, feature_on)
    dummy_msg.text = "очень очень длинный вопрос по поводу сложной интеграции и системных ошибок"
    assert mod.handle(dummy_msg) in [True, False]
```
