import discord, os, random 
from discord.ext import commands

token = 'Your-Token-Here'

flashcards = [
        'Write me a union based SQL Injection syntax',
        'What is the syntax for establishing a Null session with the net use command?',
        'What Select Based SQL command retrieves information from a database?',
        'Name two cases where memory allocation is insecure?',
        'Define me a function in python < for skids',
        'What is SSRS? (SQL Server Resolution Service)',
        'What is Stunnel?',
        'What are TCP Wrappers? < for skids lel',
        'What is the role of a RST packet in session hijacking?',
        'What are Null Sessions?',
        'What is a covert channel?',
        'What is a race condition exploit?',
        'What is a format string exploit?',
        'What is a heap overflow exploit?',
        'What is a stack overflow exploit?',
        'Whats the difference between LFI and Path Traversal Vulns?',
        'Explain a Regular Expression DOS',
        'What is the difference between DXSS and GXSS?',
        'What is an FTP Bounce scan?',
        'What is the IIS Metabase?',
        'What does a circuit-level gateway do',
        'What is the difference between ESP and the EIP?',
        'How does ADMutate alter a buffer overflow exploit?',
        'Why is strcpy() insecure?',
        '''Explain the code below or skid\n
        ```python
        import os, subprocess
        try:
            subprocess.call(["mdk3"])
            os.system("clear")
        except FileNotFoundError:
            os.system("clear")
            print("Please ensure you\'re running this program as sudo")
            mdk = "apt-get install mdk3"
            os.system(mdk)
            os.system("clear")
        ```
            '''
    ]

bot = discord.Client()
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    os.system('clear')
    print('FlashBot Ready | Waiting for skidz to flashcard...')


@bot.command()
async def flashcard(ctx):
    await ctx.message.delete()
    await ctx.send(random.choice(flashcards))

bot.run(token, bot=False)
