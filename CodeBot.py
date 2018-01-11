import discord
import asyncio
import os
from subprocess import PIPE, Popen
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

                p1 = Popen("javac Solution.java", shell=True, stdout=PIPE, stderr=PIPE)
                stdout1, stderr1 = p1.communicate()

                p2 = Popen("java Solution", shell=True, stdout=PIPE, stderr=PIPE)
                stdout2, stderr2 = p2.communicate()

                os.remove('Solution.java')
                os.remove('javaInput.txt')

                if stderr1:
                    #stderr1 = stderr1.replace("\r\n","\n")
                    print(stderr1)
                    await client.send_message(message.channel, stderr1)
                    os.remove('javaInput.txt')
                    os.remove('Solution.java')
                    
                elif stderr2:
                    print("Err2")
                    await client.send_message(message.channel, stderr2)
                    os.remove('Solution.class')
                    
                elif stdout2:
                    print("good")
                    await client.send_message(message.channel, stdout2)
                    os.remove('Solution.class')
                else:
                    await client.send_message(message.channel, "Program produced no output")
                    os.remove('Solution.class')

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
