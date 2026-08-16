import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

# قناة الترحيب
WELCOME_CHANNEL_ID = 1537211424449888408

# صورة الترحيب
WELCOME_IMAGE = "https://cdn.discordapp.com/attachments/1537220493424201769/1537496379285315666/EECB23EF-1DB0-4384-92EC-1A2FFBEED7D8.png?ex=6a7f4096&is=6a7def16&hm=6064f365c7560bc5658a11f9cbfc77903a7d189c0863c362329a27b00778c95f&"


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    # رد النقاط
    if content in [".", "..", "...", "....", "....."]:
        await message.channel.send("من العسل اللي قاعد ينقط 🤤🍯")
        return

    # ردودك الأساسية
    if content in ["السلام عليكم", "سلام عليكم"]:
        await message.channel.send("وعليكم السلام منوّرنا! 🌟")

    if content in ["صباح الخير", "صباح النور"]:
        await message.channel.send("صباح النور يا الغالي! ☀️")

    if content in ["مساء الخير", "مساء النور"]:
        await message.channel.send("مساء النور يا بعد قلبي! 🌙")

    if content in ["كيف حالك", "كيف حالكم", "وش الأخبار"]:
        await message.channel.send("تمام الحمدلله، بشرني عنك؟ 😄")

    if content in ["الو", "الووو", "الوو"]:
        await message.channel.send("هلا والله منوّر 🤍")


# ترحيب دخول عضو
@client.event
async def on_member_join(member):

    welcome_channel = client.get_channel(WELCOME_CHANNEL_ID)
    if welcome_channel:
        # إرسال الصورة
        await welcome_channel.send(WELCOME_IMAGE)

        # الترحيب داخل السيرفر
        await welcome_channel.send(
            f"# هلا والله {member.mention} 🤍✨\n"
            "***نورت السيرفر!***\n"
            "***قبل ما تبدأ، تأكد تقرأ القوانين وتتعرّف على القنوات المهمة.***\n"
            f"https://discord.com/channels/1445710183245414442/1445739153814847563\n"
            f"https://discord.com/channels/1445710183245414442/1445739161951797299\n"
            "***نتمنى لك وقت ممتع معنا ❤️***"
        )

    # الترحيب بالخاص
    try:
        await member.send(WELCOME_IMAGE)
        await member.send(
            "# مرحباً بك! 🤍\n\n"
            "***سعيدين بانضمامك معنا في السيرفر.***\n"
            "***هذي أهم الأشياء اللي تساعدك تبدأ:***\n"
            "***• اقرأ القوانين أولاً.***\n"
            "***• شاركنا في العام.***\n"
            "***• إذا احتجت مساعدة، الإداريين موجودين دائمًا.***\n\n"
            "***نتمنى لك تجربة جميلة معنا ✨***"
        )
    except:
        pass


import os
client.run(os.getenv("TOKEN"))


















