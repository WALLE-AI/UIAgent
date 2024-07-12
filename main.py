from agent.chorme_agent import test_chorme_selenuim_search


def test_chorme_search():
    text = "2017《海南省安装工程综合定额》"
    test_chorme_selenuim_search(text)



if __name__ == "__main__":
    print("hello world")
    test_chorme_search()