# (c) @UniBorg
#
import asyncio
from collections import deque

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.1fys", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("ــــــہہـ٨ـــــــ𝙁𝘼𝙔𝘼𝙎𝙃ـہہـ٨ـــــ♥️ــــ٨ـ"))
    for _ in range(98):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(98)


@borg.on(events.NewMessage(pattern=r"\.2fys", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("𝙁𝘼𝙔𝘼𝙎𝙃🆆🅴🅸🆁🅳🅾️ǟɮɳ๏尺ϻყ"))
    for _ in range(99):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(99)
