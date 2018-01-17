import discord
import asyncio
import os
from subprocess import PIPE, Popen
import shutil
import sys


path = os.path.dirname(os.path.realpath(__file__))
os.chroot(path)
