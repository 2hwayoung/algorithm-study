# link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 길이가 1이면 s return
        if len(s) <= 1:
            return s

        startindex = 0
        length = 0
        for i in range(len(s)):
            #현재 위치의 문자를 더했을 때 palindrome인지 확인
            if s[i-length:i+1] == s[i-length:i+1][::-1]: 
                startindex = i-length 
                length += 1                                  
            # 양쪽으로 하나씩 더했을 때 palindrome인지 확인                                                                                                                         
            elif i-length>0 and s[i-length-1:i+1] == s[i-length-1:i+1][::-1]:
                startindex = i-1-length
                length += 2
                
        return s[startindex:length+startindex]
