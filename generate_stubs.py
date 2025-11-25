generate_stubs.py
------------------
Автоматически создает пустые классы-модули с docstring для структуры supportbot/modules/.
Просто добавьте имена модулей в список module_names и запустите скрипт!
"""

import os

module_names = [
    "context_support", "file_module", "multilang", "personalized",
    "feedback_referral", "faq_search", "qr_scanner", "push_notify",
    "cross_platform", "mailing", "ai_handler"
]
dir_path = os.path.join(os.path.dirname(__file__), "modules")

stub_tpl = '''"""
{modulename}.py
--------------
[Описание модуля.]
"""
class {classname}:
    def __init__(self, bot, feature_on_fn):
        self.bot = bot
        self.feature_on = feature_on_fn

    def handle(self, msg):
        return False
'''

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

for mn in module_names:
    fname = os.path.join(dir_path, mn + ".py")
    classname = ''.join(word.capitalize() for word in mn.split('_'))
    if not os.path.exists(fname):
        with open(fname, "w", encoding="utf8") as f:
            f.write(stub_tpl.format(modulename=mn, classname=classname))
        print(f"  Created stub: {fname}")

print("[Done]")
