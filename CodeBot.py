import discord
import asyncio
import os
from subprocess import PIPE, Popen
import shutil
import sys

client = discord.Client()

@client.event
async def on_ready():
    sys.stdout.write("Bot online")
    sys.stdout.write(client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith("```"):
        mes = message.content.split("```")
        
        if len(mes) == 5:
            path = os.path.dirname(os.path.realpath(__file__))
            
            tmpCode = mes[1]
            tmpInp = mes[3]
            sys.stdout.write(tmpCode)      # 4 testing
            sys.stdout.write(tmpInp)       # 4 testing

            #####################################
            # Java
            #####################################
            if tmpCode.startswith("java\n"):
                
                os.mkdir(path + "\\tmp") # Create a temp file to hold any ran program 
                os.chdir(path + "\\tmp") # TODO: Add isolation property.
                
                code = tmpCode.split("java\n",1)[1]
                sys.stdout.write(code)     # for testing

                # Writes the code to Solution.java
                with open('Solution.java', 'w+') as f:
                    f.write(code)

                # Writes the input to the file javaInput.txt
                inp = tmpInp.split("\n",1)[1]
                with open('javaInput.txt', 'w+') as f:
                    f.write(inp)
                
                # Compiles the  program, and puts stderr into the string compileErr
                p1 = Popen("javac Solution.java", shell=True, universal_newlines=True, stdout=PIPE, stderr=PIPE)
                dummy, compileErr = p1.communicate()

                # Runs the program, puts stdout into string stdout, and stderr into runErr
                p2 = Popen("java Solution < javaInput.txt", shell=True, universal_newlines=True, stdout=PIPE, stderr=PIPE)
                stdout, runErr = p2.communicate()

                # Removes the files that were definately created
                os.remove('Solution.java')
                os.remove('javaInput.txt')

                # Compile-time error occured
                if compileErr:
                    compileErr = "Compile-time error occured:\n```\n" + compileErr + "\n```"
                    await client.send_message(message.channel, compileErr)

                # Run-time error occured
                elif runErr:
                    runErr = "Run-time error occured:\n```\n" + runErr + "\n```"
                    await client.send_message(message.channel, runErr)
                    os.remove('Solution.class')

                # Program ran successfully
                else:
                    stdout = "Output:\n```\n" + stdout + "\n```"
                    await client.send_message(message.channel, stdout)
                    os.remove('Solution.class')

                # Remove file tree created in tmp
                os.chdir(path)
                shutil.rmtree(path + "\\tmp")
                
            #####################################
            # C
            #####################################
            if tmpCode.startswith("c\n"):

                os.mkdir(path + "\\tmp") # Create a temp file to hold any ran program 
                os.chdir(path + "\\tmp") # TODO: Add isolation property.
                
                code = tmpCode.split("c\n",1)[1]
                sys.stdout.write(code)     # for testing

                # Writes the code to Solution.c
                with open('Solution.c', 'w+') as f:
                    f.write(code)

                # Writes the input to the file cInput.txt
                inp = tmpInp.split("\n",1)[1]
                with open('cInput.txt', 'w+') as f:
                    f.write(inp)
                
                # Compiles the  program, and puts stderr into the string compileErr
                p1 = Popen("gcc Solution.c", shell=True, universal_newlines=True, stdout=PIPE, stderr=PIPE)
                dummy, compileErr = p1.communicate()

                # Runs the program, puts stdout into string stdout, and stderr into runErr
                p2 = Popen("a.exe < cInput.txt", shell=True, universal_newlines=True, stdout=PIPE, stderr=PIPE)
                stdout, runErr = p2.communicate()

                # Removes the files that were definately created
                os.remove('Solution.c')
                os.remove('cInput.txt')

                # Compile-time error occured
                if compileErr:
                    compileErr = "Compile-time error occured:\n```\n" + compileErr + "\n```"
                    await client.send_message(message.channel, compileErr)

                # Run-time error occured
                elif runErr:
                    runErr = "Run-time error occured:\n```\n" + runErr + "\n```"
                    await client.send_message(message.channel, runErr)
                    os.remove('a.exe')

                # Program ran successfully
                else:
                    stdout = "Output:\n```\n" + stdout + "\n```"
                    await client.send_message(message.channel, stdout)
                    os.remove('a.exe')

                # Remove file tree created in tmp
                os.chdir(path)
                shutil.rmtree(path + "\\tmp")
        
        
        

client.run('MzkzOTk1MjI3Mjk3MzQ5NjMy.DR-o8g.gZGzYtSlnS6TatK-wMZHhuzkJzw')
