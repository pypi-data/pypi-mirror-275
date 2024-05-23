from .app import TerminalsProxyExtensionApp


__version__ = "0.2.1"


def _jupyter_server_extension_points():  # pragma: no cover
    return [
        {
            "module": "jupyter_server_terminals_proxy.app",
            "app": TerminalsProxyExtensionApp,
        },
    ]
