# 중복 없애기
# 정렬되어 있지 않은 연결리스트가 주어졌을 때 이 리스트에서 중복되는 원소를 제거하는 코드를 작성하라.
# 연관문제) 임시 버퍼를 사용할 수 없다면 어떻게 풀 수 있을까?

from ..node import Node

class Solution:
    def removeDuplicate(self, head: Node) -> Node:
        # 원소들을 추적하기 위해 간단히 해시테이블 사용
        # 시간복잡도: O(N), N = 연결리스트 길이
        hashTable = {}
        prev = None
        n = head
        while n is not None:
            if n.get_data() in hashTable.keys():
                prev.set_next(n.get_next()) # 중복된 원소 삭제 (prev는 그대로)
            else:
                hashTable[n.get_data()] = True
                prev = n
            n = n.get_next()
        return n
    
    # 연관문제) 임시 버퍼를 사용할 수 없다면 어떻게 풀 수 있을까?
    def removeDuplicate2(self, head:Node) -> Node:
        # 비효율적이지만 투 포인터로 처리
        # current 포인터는 연결리스트 순회용, runner 포인터는 중복원소 확인용
        # 시간복잡도: O(N^2) / 공간복잡도: O(1) 
        current = head
        while current is not None:
            runner = current
            while runner.get_next() is not None:
                if runner.get_next().get_data() == current.get_data():
                    runner.set_next(runner.get_next().get_next())
                else:
                    runner = runner.get_next()
            current = current.get_next()