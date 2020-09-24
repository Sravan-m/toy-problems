from lru import lru

class lruTEST:
    def __init__(self):
        pass

    def testcases(self):
        a=lru(3)
        a.put("getbootstrap")
        assert a.get("getbootstrap")!=None,"testcase 1 failed"
        print("testcase 1 passed")
        a.put("github")
        assert a.get("github")!=None,"testcase 2 failed"
        print("testcase 2 passed")
        a.put("gmail")
        assert a.get("gmail")!=None,"testcase 3 failed"
        print("testcase 3 passed")
        print("All testcases passed!")
        lst = a.get_cache()
        for i in lst:
            print(i)

if __name__ == "__main__":
    a = lruTEST()
    a.testcases()