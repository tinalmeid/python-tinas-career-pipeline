"""
@file tests/test_utils/test_security.py
@description Testes unitários para arquivo utils/security.py,
focando na sanitização de logs e proteção de dados sensíveis.

@author Tina de Almeida
@date Abril de 2026
@version 1.0.0
"""

from src.utils.security import sanitize_log, LogSanitizer
from src.utils.feature_toggles import FeatureToggles

# Testes para LogSanitizer


def test_sanitize_log_masks_sensitive_info():
    """
    Garante que dados sensíveis sejam mascarados nos logs.
    """
    sensitive_data = "Tentativa de login com password=minha_senha_secreta e token: 'xyz123'"  # NOSONAR
    sanitized_data = sanitize_log(sensitive_data)

    assert "minha_senha_secreta" not in sanitized_data
    assert "xyz123" not in sanitized_data
    assert "password=***" in sanitized_data  # NOSONAR


def test_feature_toggles_is_singleton():
    """
    Valida o padrão singleton da classe FeatureToggles,
    garantindo que apenas uma instância seja criada.
    """
    toggles1 = FeatureToggles()
    toggles2 = FeatureToggles()

    assert toggles1 is toggles2


def test_feature_not_found_returns_false():
    """
    Verifica que uma feature não configurada retorna False.
    """
    toggles = FeatureToggles()
    assert not toggles.is_enabled("FEATURE_INEXISTENTE")


def test_sanitize_log_with_multiple_and_mixed_patterns():
    """
    Testa se o loop percorre todos os padrões definidos no LogSanitizers.
    """
    # Testando múltiplos padrões e diferentes separadores no mesmo log
    mixed_log = "Auth: 'token-123', secret=9999, non_sensitive=true"
    sanitized = sanitize_log(mixed_log)

    # Valida que o loop processou os padrões
    assert "token-123" not in sanitized
    assert "9999" not in sanitized
    assert "Auth:***" in sanitized
    assert "secret=***" in sanitized
    assert "non_sensitive=true" in sanitized  # Dado não sensível mantido


def test_sanitize_log_case_insensitivity():
    """
    Valida o modificador (?i) do regex na linha 60 de security.py.
    """
    # Testa se 'PASSWORD' (caps) é capturado pelo regex
    log_caps = "Tentativa com PASSWORD=SENSIVEL"  # NOSONAR
    assert "SENSIVEL" not in sanitize_log(log_caps)
    assert "PASSWORD=***" in sanitize_log(log_caps)  # NOSONAR


def test_log_sanitizer_class_directly():
    """Testa a classe LogSanitizer diretamente para garantir que o loop de padrões seja executado."""
    # Isso forçará o pytest a entrar no loop 'for' da classe
    raw = "secret=12345"
    result = LogSanitizer.mask_message(raw)
    assert "12345" not in result
    assert "secret=***" in result
