import sendingEmail
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_KEY")
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_voice_state_update(member, before, after):
    number = "4025172332"
    provider = "Mint Mobile"
    email_address = "automatetextdisco@gmail.com"
    email_password = "tcpwkmewleohbdbd"
    sender_credentials = (email_address, email_password)

    if before.channel is None and after.channel is not None:
        message = "{} has joined".format(member.name)
        subject = "{} voice channel".format(after.channel.name)
        sendingEmail.send_sms_via_email(number, message, provider, sender_credentials, subject)

    # if before.channel is not None and after.channel is None:
    #     message = "{} has left".format(member.name)
    #     subject = "{} voice channel".format(before.channel.name)
    #     sendingEmail.send_sms_via_email(number, message, provider, sender_credentials, subject)


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
