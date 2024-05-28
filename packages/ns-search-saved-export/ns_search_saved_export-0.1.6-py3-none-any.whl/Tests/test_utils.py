import unittest
import oauth2 as oauth
from ns_search_saved_export.utils import SignatureMethod_HMAC_SHA256

class TestSignatureMethod_HMAC_SHA256(unittest.TestCase):
    
    def setUp(self):
        self.consumer = oauth.Consumer(key='consumer_key', secret='consumer_secret')
        self.token = oauth.Token(key='token_key', secret='token_secret')
        self.signature_method = SignatureMethod_HMAC_SHA256()
        self.request = oauth.Request(method='POST', url='https://example.com', parameters={})

    def test_signing_base(self):
        key, raw = self.signature_method.signing_base(self.request, self.consumer, self.token)
        self.assertIsInstance(key, bytes)
        self.assertIsInstance(raw, bytes)

    def test_sign(self):
        self.signature_method.sign(self.request, self.consumer, self.token)
        self.assertIn('oauth_signature', self.request)

if __name__ == '__main__':
    unittest.main()
