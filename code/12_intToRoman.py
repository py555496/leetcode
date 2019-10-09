class Solution(object):
    def get_str(self, num, char_arr):
        out_str = ""
        if num == 9:
            out_str += char_arr[2] + char_arr[0] 
        elif num == 4:
            out_str += char_arr[2] + char_arr[1] 
        elif num > 4 and num < 9:
            out_str = char_arr[1] + "".join([char_arr[2] for _ in range(num - 5)])
        else:
            out_str = "".join([char_arr[2] for _ in range(num)])
        return out_str
    
    def intToRoman(self, num):
        out_str = ""
        a = num
        char_arr = ['M','D','C','L','X','V','I']
        if a >= 1000:
            out_str += "".join([char_arr[0] for _ in range(a/1000)])
            a = a % 1000
        if a / 100 > 0:
            out_str += self.get_str(a / 100,char_arr[:3])
            a = a % 100
        if a / 10 > 0:
            out_str += self.get_str(a / 10,char_arr[2:5])
            a = a % 10
        if a > 0:
            out_str += self.get_str(a,char_arr[4:])
        return out_str
        """
        b_arr.append(a/1000)
        a = a%1000
        b_arr.append(a/500)
        a = a%500
        b_arr.append(a/100)
        a = a%100
        b_arr.append(a/50)
        a = a%50
        b_arr.append(a/10)
        a = a%10
        b_arr.append(a/5)
        a = a%5
        b_arr.append(a/1)
        """
        """
        :type num: int
        :rtype: str
        """