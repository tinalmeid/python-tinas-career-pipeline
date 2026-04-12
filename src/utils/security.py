"""
@file src/utils/security.py
@description Utilitários de segurança para sanitização de dados sensíveis e proteção de logs

@author Tina de Almeida
@date Abril de 2026
@version 1.0.0
"""

import re
from typing import Any


class LogSanitizer:
    """
    Classe responsável por centralizar os padrões de sanitização.
    Segue o SRP (Responsabilidade Única) do SOLID.
    """
    # Regex blindado que captura:
    # 1.Chave,
    # 2.Separador,
    # 3.Valor
    SENSITIVE_PATTERNS = [
        r"(?i)(password|token|api_key|secret|auth)\s*([=:])\s*['\"]?([^'\"\s,]+)['\"]?",
    ]

    @staticmethod
    def mask_message(message: str) -> str:
        """
        Aplica os padrões de sanitização definidos em SENSITIVE_PATTERNS.
        O loop garante que todos os padrões sejam processados, mesmo que haja múltiplos no mesmo log.

        args:
            message (str): A mensagem de log a ser sanitizada.

        returns:
            str: A mensagem de log com dados sensíveis mascarados.
        """
        sanitized = message
        for pattern in LogSanitizer.SENSITIVE_PATTERNS:
            # Substitui o match inteiro (Chave + Separador + Valor) por Chave + Separador + ***
            sanitized = re.sub(pattern, r"\1\2***", sanitized)
        return sanitized


def sanitize_log(message: Any) -> str:
    """
    Função utilitária para sanitizar mensagens de log, garantindo que dados sensíveis sejam protegidos.

    args:
        message (Any): A mensagem de log a ser sanitizada. Pode ser de qualquer tipo
        (str, dict, etc.), mas será convertida para string antes da sanitização.

    returns:
        str: A mensagem de log com dados sensíveis mascarados.
    """
    return LogSanitizer.mask_message(str(message))

# @file Fim do arquivo src/utils/security.py
