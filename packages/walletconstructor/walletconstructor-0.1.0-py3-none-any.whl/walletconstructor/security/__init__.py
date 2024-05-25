import walletconstructor.security.security as _security


security = _security.Security

def security_init(**kwargs) -> _security.Security:
    return _security.Security(**kwargs)

