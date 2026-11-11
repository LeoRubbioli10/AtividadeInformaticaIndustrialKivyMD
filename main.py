import sys
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock

# Adiciona o diretório atual ao path para importar a pasta cliente
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from cliente.clientemodbus import ClienteMODBUS

class ModbusApp(MDApp):
    def build(self):
        self.cliente_modbus = None
        self.evento_leitura = None
        # Carrega o arquivo separado
        return Builder.load_file('interface.kv')
    
    def conectar(self):
        ip = self.root.ids.input_ip.text
        porta = int(self.root.ids.input_porta.text)
        
        if not self.cliente_modbus:
            self.cliente_modbus = ClienteMODBUS(server_ip=ip, porta=porta)
        
        if self.cliente_modbus.conectar():
            self.root.ids.label_status.text = f"Status: Conectado a {ip}:{porta}"
            self.root.ids.btn_conectar.disabled = True
        else:
            self.root.ids.label_status.text = "Status: Falha ao conectar"