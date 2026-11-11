import sys
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock

# Adiciona o diretório atual ao path para importar a pasta cliente
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from cliente.clientemodbus import ClienteMODBUS