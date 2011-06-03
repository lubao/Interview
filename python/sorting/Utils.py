#!/usr/bin/env python
class Tester:
    @staticmethod
    def _generate_test_list(rate=100):
        import random
        sample=[i for i in range(rate << 3)]
        return random.sample(sample, rate)

if __name__=="__main__":
    pass
