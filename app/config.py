import json
import os

class Settings:
    _instance = None

    def __init__(self):
        self.config = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def load(self, path='settings.json'):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            print("⚠️ Aviso: settings.json não encontrado. Usando padrões.")
            self.config = {}

    def get(self, key, default=None):
        return self.config.get(key, default)