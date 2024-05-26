from unittest import TestCase
from src import ProxyPool as PP, ProxyPool as PE
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


class TestProxy(TestCase):

    def test_use(self):
        POOL = PP.ProxyPool(test_proxies[:3], max_uses=1)

        ProxRef1 = POOL.Proxy()
        ProxRef2 = POOL.Proxy()
        ProxRef3 = POOL.Proxy()

        self.assertEqual(ProxRef1.assigned_proxy, ProxRef2.assigned_proxy)
        self.assertEqual(ProxRef2.assigned_proxy, ProxRef3.assigned_proxy)

        prox1 = ProxRef1.use()

        self.assertEqual(prox1, test_proxies[0])

        self.assertEqual(POOL[prox1].used_counter, 1)
        self.assertEqual(POOL[prox1].given_out_counter, 3)

        self.assertFalse(POOL.proxy_valid_to_use(prox1))

        prox2 = ProxRef2.use()

        self.assertNotEqual(prox1, prox2)

        self.assertEqual(POOL[prox1].used_counter, 1)
        self.assertEqual(POOL[prox1].given_out_counter, 2)
        self.assertEqual(POOL[prox2].used_counter, 1)
        self.assertEqual(POOL[prox2].given_out_counter, 1)

        prox3 = ProxRef3.use()

        self.assertNotEqual(prox3, prox2)

        self.assertEqual(POOL[prox1].used_counter, 1)
        self.assertEqual(POOL[prox1].given_out_counter, 1)
        self.assertEqual(POOL[prox2].used_counter, 1)
        self.assertEqual(POOL[prox2].given_out_counter, 1)
        self.assertEqual(POOL[prox3].used_counter, 1)
        self.assertEqual(POOL[prox3].given_out_counter, 1)

        self.assertRaises(PE.NoValidProxies, ProxRef1.use)

    def test_timeout(self):
        POOL = PP.ProxyPool(test_proxies[:3])

        ProxRef1 = POOL.Proxy()
        ProxRef2 = POOL.Proxy()
        ProxRef3 = POOL.Proxy()

        self.assertEqual(ProxRef1.assigned_proxy, ProxRef2.assigned_proxy)
        self.assertEqual(ProxRef2.assigned_proxy, ProxRef3.assigned_proxy)

        ProxRef1.timeout(4)

        prox2 = ProxRef2.use()

        prox3 = ProxRef3.use()

        self.assertEqual(ProxRef2.assigned_proxy, ProxRef3.assigned_proxy)
        self.assertFalse(ProxRef1._is_valid())

        ProxRef2.ban()
        prox3 = ProxRef3.use()
        ProxRef3.ban()

        try:
            prox1 = ProxRef1.use()
            self.fail("Did not raise exception")
        except PE.ProxiesTimeout as timeout_error:
            time.sleep(timeout_error.timeout - time.time() + 1)

        prox1 = ProxRef1.use()

        self.assertEqual(prox1, test_proxies[0])
