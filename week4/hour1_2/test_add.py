def test_add():                                                              # テストadd関数の定義
    assert add_multiple(1, 2) == 3                                           # - 1と2を足して3になることをアサート
    assert add_multiple(0, 0) == 0                                           # - 0と0を足して0になることをアサート
    assert add_multiple(-1, 1) == 0                                          # - -1と1を足して0になることをアサート
    assert add_multiple(1, 2, 3) == 6                                        # - 1, 2, 3を足して6になることをアサート
    assert add_multiple() == 0                                               # - 引数なしで呼び出した場合、0を返すことをアサート
    assert add_multiple(-1, -2, -3) == -6                                    # - 負の数を足した場合、負の数になることをアサート
    assert add_multiple(1.5, 2.5) == 4                                       # - 小数を足した場合、小数になることをアサート
    assert add_multiple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55                 # - 10個の数字を足した場合、55になることをアサート
    assert add_multiple(100000000000000, 100000000000000) == 200000000000000 # - 大きな数字を足した場合、正しく計算できることをアサート

def add_multiple(*args):
    """任意個数の整数を受け取り、その和を返す関数です。

    Args:
        *args (int): 足し合わせる整数

    Returns:
        int: 引数の和
    """
    return sum(args)
