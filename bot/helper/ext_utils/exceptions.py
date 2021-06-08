class DirectDownloadLinkException(Exception):
    """Не найден метод для извлечения прямой ссылки для скачивания из http-ссылки"""
    pass


class NotSupportedExtractionArchive(Exception):
    """Формат архива, который используется для извлечения, не поддерживается"""
    pass
