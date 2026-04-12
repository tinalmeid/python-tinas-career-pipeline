"""
@file src/utils/feature_toggles.py
@description Implementação de feature toggles (Padrão Singleton) para gerenciamento de chaves de funcionalidades.

@author Tina de Almeida
@date Abril de 2026
@version 1.0.0
"""
import os


class FeatureToggles:
    """
    Implementação Singleton para garantir consistência nas flags do sistema.
    """
    _instance = None
    _toggles: dict = {}  # Armazena o estado das features

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FeatureToggles, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Inicializa os toggles apenas se ainda não tiverem sido carregados."""
        if not self._toggles:
            self._load_toggles()

    def _load_toggles(self):
        """Carrega flags das variáveis de ambiente ou valores default."""
        self._toggles = {
            "FEATURE_MOCK_API": os.getenv("FEATURE_MOCK_API", "true").lower() == "true",
            "FEATURE_NLP_PROCESSOR": os.getenv("FEATURE_NLP_PROCESSOR", "false").lower() == "true",
        }

    def is_enabled(self, feature_name: str) -> bool:
        """Verifica se uma feature específica está ativa."""
        return self._toggles.get(feature_name, False)

# @file Fim do arquivo src/utils/feature_toggles.py
