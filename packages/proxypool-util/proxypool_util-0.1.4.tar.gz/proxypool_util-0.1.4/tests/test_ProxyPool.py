from unittest import TestCase
from src import ProxyPool as PP
import time

from threading import Thread

test_proxies = [
    f"https://proxy{a}" for a in range(100)
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

    def test_replenish_proxy(self):

        thread_count = 50

        def replenishing(this_proxypool: PP.ProxyPool):
            print("replenishing")
            this_proxypool.add_proxies(test_proxies[thread_count : (thread_count * 2)])

        POOL = PP.ProxyPool(test_proxies[:thread_count], max_give_outs=1, replenish_proxies_func=replenishing)

        gotten_proxies = {}

        def thread_for_proxy(proxy_rep: PP.Proxy):

            first_proxy = proxy_rep.use()
            proxy_rep.ban()
            second_proxy = proxy_rep.use()

            gotten_proxies[second_proxy] = True
            gotten_proxies[first_proxy] = False

        threads = []

        for i in range(thread_count):
            threads.append(Thread(target=thread_for_proxy, args=[POOL.Proxy()], daemon=True))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        for p in test_proxies[:thread_count]:
            self.assertFalse(gotten_proxies[p])

        for p in test_proxies[thread_count:thread_count * 2]:
            self.assertTrue(gotten_proxies[p])

    def test_replenish_proxy_error(self):

        thread_count = 2

        def replenishing(this_proxypool: PP.ProxyPool):
            print("replenishing")
            raise Exception("expected")

        POOL = PP.ProxyPool(test_proxies[:thread_count], max_give_outs=1, replenish_proxies_func=replenishing)

        gotten_proxies = {}

        def thread_for_proxy(proxy_rep: PP.Proxy):

            first_proxy = proxy_rep.use()
            gotten_proxies[first_proxy] = False
            proxy_rep.ban()
            self.assertRaises(Exception, proxy_rep.use)
            # gotten_proxies[second_proxy] = True

        threads = []

        for i in range(thread_count):
            threads.append(Thread(target=thread_for_proxy, args=[POOL.Proxy()], daemon=True))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        for p in test_proxies[:thread_count]:
            self.assertFalse(gotten_proxies[p])

        for p in test_proxies[thread_count:thread_count * 2]:
            self.assertIs(gotten_proxies.get(p, None), None)
