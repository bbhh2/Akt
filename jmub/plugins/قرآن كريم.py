#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣


#صدقـة جـاريـه لـروح المرحومـة أمـي وروح المرحومـة أم مـلاذ


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@jmub.ar(admin_cmd(pattern="قرآن ?(.*)"))
@jmub.ar(sudo_cmd(pattern="قرآن ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ .بـاضافة اسـم القارئ + || + اسم السورة للامـر للبحث مثـال :  .السديس || الكوثر .. القراء هم عبدالصمد - الشاطري - المنشاوي - المعيقلي - الكوشي - الغامدي - الدوسري - الدوكالي - العجمي - العباد𓅫╰**"
        )
    chat = "@BBBllbot"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل السـورة ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2125397049)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @BBBllbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "قرآن كريم": "**اسم الاضافـه : **`قرآن كريم`\
    \n\n**╮•❐ الامـر ⦂ **`.قرآن` + اسم القارئ + || + اسم السورة \
    \n**الشـرح •• **تحميل سـور القـرآن الكـريم بصـوت 13 قارئ للتعليمات ارسل .قرآن"
    }
)
