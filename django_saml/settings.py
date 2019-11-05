SAML_SP = None

SAML_IDP = None
SAML_IDP_FILE = None
SAML_IDP_URL = None
SAML_IDP_METADATA_TIMEOUT = 3600

SAML_SECURITY = {
    "nameIdEncrypted": False,
    "authnRequestsSigned": False,
    "logoutRequestSigned": False,
    "logoutResponseSigned": False,
    "signMetadata": False,
    "wantMessagesSigned": False,
    "wantAssertionsSigned": False,
    "wantNameId": True,
    "wantNameIdEncrypted": False,
    "wantAssertionsEncrypted": False,
    "signatureAlgorithm": "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
    "digestAlgorithm": "http://www.w3.org/2000/09/xmldsig#sha1"
}

SAML_CONTACT = None

SAML_ORGANIZATION = None

SAML_DEFAULT_REDIRECT = '/'
SAML_USERNAME_ATTR = 'uid'
SAML_ATTR_MAP = []

SAML_BASE_DIRECTORY = None
