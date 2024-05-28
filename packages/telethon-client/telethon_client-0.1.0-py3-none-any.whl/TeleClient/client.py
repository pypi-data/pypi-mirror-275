from telethon import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from .env import OWNERS

class MyClient(TelegramClient):
    def __init__(self, session, api_id, api_hash):
        super().__init__(session, api_id, api_hash)
        self.me = None

    async def getMe(self):
        if not self.me:
            self.me = await self.get_me()
        return self.me
    
    async def saveAllGroups(self):
        dialogs = await self.get_dialogs()
        groups = []
        for dialog in dialogs:
            try:
                if dialog.is_group:
                    if dialog.entity.username:
                        groups.append(f"@{dialog.entity.username}")
                    else:
                        full_chat = await self(GetFullChannelRequest(dialog.id))
                        if full_chat.full_chat.exported_invite:
                            groups.append(full_chat.full_chat.exported_invite.link)
            except Exception as e:
                print(e)
                continue
        return groups
    
    async def checkCancel(self, event):
        if event.text == "/cancel":
            await event.respond("Cancelled The Command.")
            return True
        else:
            return False

    def checkOwner(self, event):
        if event.sender_id in OWNERS:
            return True
        else:
            return False

