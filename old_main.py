import discord
import pickledb
import commands as com
import config

db = pickledb.load('snippets.db', False)
code_keys = db.getall()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # this won't work if someone wants to at someone and post a snippet
    # if (client.user in message.mentions and len(message.mentions) > 1) or \
    #     (len(message.mentions) == 1 and not client.user in message.mentions):
    #     return

    # if bot is the only user mentioned give access to tools
    if client.user in message.mentions and len(message.mentions) == 1:
        helpful = True if 'helpful' in [str(role) for role in message.author.roles] else False
        msg = message.content.split(' ', 1)[1]

        if msg == 'list':
            await message.channel.send(f'`{" ".join(code_keys)}`')

        elif msg == 'commands' or msg == 'help':
            await message.channel.send(com.commands)

        elif msg.startswith("add") and helpful:            
            try:
                words = msg.split('```')
                key = words[0].split()[1]
                value = words[1]
                value = '```'+ value + '```'                
                db.set(key, value)
                db.dump()
                await message.channel.send(key + " added")
            except Exception:
                await message.channel.send("bad input, try again")
        
        elif msg.startswith("add") and not helpful:
            await message.channel.send("add only available to helpful role")
            
        elif msg.startswith("rem") and helpful:
            words = msg.split()
            if words[1] in code_keys:
                db.rem(words[1])
                db.dump()
                await message.channel.send(words[1] + " removed")
            else:
                await message.channel.send("key not found, nothing removed")            

        elif msg.startswith("rem") and not helpful:
            await message.channel.send("rem only available to helpful role")

        else:
            await message.channel.send(
                f'Bot only accepts the folowing one word commands \n'
                f'`{" ".join(com.com_list)}`\n'
                f'to print a snippet prepend it with $ like $random'
                )
    else:        
        msgs = message.content.split()
        keys = [msg[1:] for msg in msgs if msg[0] == "$"]
        for key in keys:        
            if key in code_keys:        
                await message.channel.send(db.get(key))
            else:
                await message.channel.send("key not found")


client.run(config.TOKEN)
