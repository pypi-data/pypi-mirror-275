from unittest import TestCase
from src import ProxyPool as PP
import time

test_proxies = [
    "https://proxy1",
    "https://proxy2",
    "https://proxy3",
    "https://proxy4",
    "https://proxy5",
    "https://proxy6",
    "https://proxy7",
]

class TestProxyPool(TestCase):

    def test_init(self):
        POOL = PP.ProxyPool(test_proxies)

        for p in test_proxies:
            self.assertTrue(POOL.proxy_valid_to_use(p))
            self.assertTrue(POOL.proxy_valid_to_give(p))

    def test_proxy(self):
        POOL = PP.ProxyPool(test_proxies)

        proxy1 = POOL.Proxy()

        self.assertIs(proxy1.proxy_pool, POOL)

    def test_get_proxy(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_give_outs=1)

        prox1 = POOL.get_proxy()

        self.assertEqual(POOL[prox1].given_out_counter, 1)

        prox2 = POOL.get_proxy()

        self.assertNotEqual(prox1, prox2)
        self.assertEqual(POOL[prox2].given_out_counter, 1)

        prox3 = POOL.get_proxy(prox2)

        self.assertNotEqual(prox2, prox3)
        self.assertEqual(POOL[prox2].given_out_counter, 0)
        self.assertEqual(POOL[prox3].given_out_counter, 1)

    def test_proxy_valid_to_give(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_give_outs=1)

        prox1 = POOL.get_proxy()

        POOL.timeout_proxy(prox1, 10000)

        self.assertFalse(POOL.proxy_valid_to_give(prox1))

    def test_proxy_valid_to_use(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_give_outs=1)

        prox1 = POOL.get_proxy()

        POOL.timeout_proxy(prox1, 10000)

        self.assertFalse(POOL.proxy_valid_to_use(prox1))

    def test_timeout_proxy(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_give_outs=1)

        prox1 = POOL.get_proxy()

        POOL.timeout_proxy(prox1, 10000)

        self.assertEqual(POOL[prox1].timed_out_counter, 1)
        self.assertGreater(POOL[prox1].timeout, time.time())

    def test_ban_proxy(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_give_outs=1)

        prox1 = POOL.get_proxy()

        POOL.ban_proxy(prox1)

        self.assertTrue(POOL[prox1].banned)

    def test_unban_proxy(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_give_outs=1)

        prox1 = POOL.get_proxy()

        POOL.ban_proxy(prox1)
        POOL.unban_proxy(prox1)

        self.assertFalse(POOL[prox1].banned)
