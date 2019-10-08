class Solution(object):
    def orderlyQueue(self, S, K):
        if K == 1:
            index = -1
            min_n = 9999
            for i in range(len(S)):
                if ord(S[i]) < min_n:
                    min_n = ord(S[i])
                    index = i
            cand_index = []
            min_n = chr(min_n)
            for i in range(len(S)):
                if S[i] == min_n:
                    cand_index.append(i)
            if len(cand_index) == 1:
                return S[index:] + S[:index]
            else:
                out_index = 0
                add_i = 1
                while True:
                    print cand_index
                    if len(cand_index) == 1:
                        out_index = cand_index[0]
                        break
                    alpha = []
                    for g in cand_index:
                        alpha.append(S[(g + add_i) % len(S)])
                    print alpha, add_i
                    sorted_alpha = sorted(alpha)
                    temp_min = sorted_alpha[0]
                    new_cand_index = []
                    for i in range(len(alpha)):
                        if alpha[i] == temp_min:
                            new_cand_index.append(cand_index[i])
                    cand_index = new_cand_index                    
                    add_i += 1
                    if i > len(S):
                        out_index = cand_index[0]
                        break
                return S[out_index:] + S[:out_index]
        else:
            S = list(S)
            for i in range(0, len(S)):
                for j in range(len(S) - 1, i, -1):
                    if j - 1 >= 0:
                        if ord(S[j]) < ord(S[j - 1]):
                            S[j], S[j - 1] = S[j - 1], S[j]
            return "".join(S)
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        