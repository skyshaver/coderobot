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
    
    # if bot is the only user mentioned give access to tools
    if client.user in message.mentions and len(message.mentions) == 1:
        try:
            msg = message.content.split(' ', 1)[1]
        except Exception as e:
            print(e)
            await message.channel.send("nothing to say? for help use _-h_ or _help_")
            return

        helpful = True if 'helpful' in [str(role) for role in message.author.roles] else False
        author = str(message.author)
        time_stamp = str(message.created_at)

        if msg == 'list':
            if len(code_keys) < 1:
                await message.channel.send('list is empty')
            else:
                await message.channel.send(f'`{" ".join(code_keys)}`')

        elif msg in ['commands', 'help', '-h']:
            await message.channel.send(com.commands)
        
        elif message.content.startswith(("rem", "add","update", "blame")) and not helpful:        
            await message.channel.send("command only available to helpful role")

        elif msg.startswith(("add", "update")) and helpful:            
            try:
                words = msg.split('```')
                key = words[0].split()[1]
                value = words[1]
                value = '```'+ value + '```'
                if len(value) > 1000:
                    await message.channel.send("snippet is too long, 1000 chars max")
                    return                  
                db.set(key, {"body":value, "author":author, "time":time_stamp})
                db.dump()
                await message.channel.send(key + " added")
            except Exception as e:
                print(e)
                await message.channel.send("bad input, try again")
            
        elif msg.startswith("rem") and helpful:
            words = msg.split()
            try:
                if words[1] in code_keys:
                    db.rem(words[1])
                    db.dump()
                    await message.channel.send(words[1] + " removed")
                else:
                    await message.channel.send("key not found, nothing removed")
            except Exception as e:
                print(e)
                await message.channel.send("bad input, try again")            
        
        elif msg.startswith("blame"):
            words = msg.split()
            try:
                if words[1] in code_keys:
                    key = db.get(words[1])
                    await message.channel.send(key["author"] + " " + key["time"])
                else:
                    await message.channel.send("key not found, no one to blame")
            except Exception as e:
                print(e)
                await message.channel.send("bad input, try again")            

        else:
            await message.channel.send(
                f'Bot only accepts the folowing one word commands \n'
                f'`{" ".join(com.com_list)}`\n'
                f'to print a snippet prepend it with _$_ like _$random_'
                )
    else:        
        msgs = message.content.split()
        keys = [msg[1:] for msg in msgs if msg[0] == "$"]
        for key in keys:        
            if key in code_keys:        
                k = db.get(key)
                await message.channel.send(k["body"])
            else:
                await message.channel.send("key not found")

client.run(config.TOKEN)
