import discord
import asyncio
import os
#import time
#from subprocess import call

client = discord.Client()

@client.event
async def on_ready():
    print("Bot online")
    print(client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith("```"):
        mes = message.content.split("```")
        
        if len(mes) == 5:
            tmpCode = mes[1]
            tmpInp = mes[3]
            print(tmpCode)
            print(tmpInp)

            # Fix issue with class and filenames
            if tmpCode.startswith("java\n"):
                code = tmpCode.split("java\n",1)[1]
                print(code)

                with open('Solution.java', 'w+') as f:
                    f.write(code)

                inp = tmpInp.split("\n",1)[1]
                with open('javaInput.txt', 'w+') as f:
                    f.write(inp)

                exce = os.popen("javac Solution.java").read()
                output = os.popen("java Solution < javaInput.txt").read()

                await client.send_message(message.channel, exce + output)

            if tmpCode.startswith("c\n"):
                code = tmpCode.split("c\n",1)[1]

                with open('tmp.c', 'w+') as f:
                    f.write(code)

                inp = tmpInp.split("\n",1)[1]
                with open('cInput.txt', 'w+') as f:
                    f.write(inp)
                

                exce = os.popen("gcc tmp.c -o Ctmp").read()
                # Make a different isolated folder for this
                output = os.popen("C:\\Users\\Nick\\Desktop\\CodeBot\\Ctmp.exe < cInput.txt").read()
                    
                

                await client.send_message(message.channel, output)

        
        
        

client.run('MzkzOTk1MjI3Mjk3MzQ5NjMy.DR-o8g.gZGzYtSlnS6TatK-wMZHhuzkJzw')
