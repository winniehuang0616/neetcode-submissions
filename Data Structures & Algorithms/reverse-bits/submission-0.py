class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]      # 去掉 ob
        print(num)
        num = num.zfill(32)   # 補滿 32 位元
        print(num)
        temp = num[::-1]      # 反轉
        print(temp)
        return int(temp, 2)   # 轉回十進位
        