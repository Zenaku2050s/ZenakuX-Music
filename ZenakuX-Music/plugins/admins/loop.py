from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from ZenakuX-Music import app
from ZenakuX-Music.utils.database import get_loop, set_loop
from ZenakuX-Music.utils.decorators import AdminRightsCheck
from ZenakuX-Music.utils.inline import close_markup


@app.on_message(filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    usage = _["admin_17"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    if state.isnumeric():
        state = int(state)
        if 1 <= state <= 10:
            got = await get_loop(chat_id)
            if got != 0:
                state = got + state
            if int(state) > 10:
                state = 10
            await set_loop(chat_id, state)
            return await message.reply_text(
                text=_["admin_18"].format(state, message.from_user.mention),
                reply_markup=close_markup(_),
            )
        else:
            return await message.reply_text(_["admin_17"])
    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            text=_["admin_18"].format(state, message.from_user.mention),
            reply_markup=close_markup(_),
        )
    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(
            _["admin_19"].format(message.from_user.mention),
            reply_markup=close_markup(_),
        )
    else:
        return await message.reply_text(usage)


__MODULE__ = "Repeat Song"
__HELP__ = """
**Loop/Repeat Control**

This module allows administrators to control the loop playback in the group.

Commands:
- /loop <count>: Enable loop playback for the specified count (1-10).
- /cloop <count>: Enable loop playback for the specified count (1-10).
- /loop enable: Enable loop playback indefinitely (loop count set to 10).
- /cloop enable: Enable loop playback indefinitely (loop count set to 10).
- /loop disable: Disable loop playback.
- /cloop disable: Disable loop playback.

Note:
- Only administrators can use these commands.
- Loop count must be between 1 and 10.
"""
