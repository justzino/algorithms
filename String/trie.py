"""
보통 문자열이 존재하는지 확인: O(n)
Trie 알고리즘: O(m) (m은 문자열의 길이)

문자열을 검색하는 문제에서 입력되는 문자열이 많을 경우 자주 사용
빠른 시간복잡도 덕분에 검색엔진 사이트에서 제공하는 자동 완성 및 검색어 추천 기능에서 Trie 알고리즘을 사용
"""


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = {}


class Trie:
    """
    find: O(m) - 문자열 하나 찾는 operation
    add: O(m) - 문자열 추가하는 operation
    """
    def __init__(self):
        self._root = TrieNode()

    def _recurAdd(self, node: TrieNode, word: str) -> None:
        if len(word) == 0:
            node.isEnd = True
            return

        ch = word[0]
        next_link = node.links.get(ch)
        if next_link is None:
            node.links[ch] = TrieNode()
            next_link = node.links[ch]
        self._recurAdd(next_link, word[1:])

    def add(self, word: str) -> None:
        if len(word) == 0:
            return

        self._recurAdd(self._root, word)

    def _recurSearch(self, node: TrieNode, word: str) -> bool:
        if len(word) == 0:
            isEnd = node.isEnd
            return isEnd

        ch = word[0]
        if ch == '.':
            letters = node.links.keys()
            for key in letters:
                ret = self._recurSearch(node.links[key], word[1:])
                if ret is True:
                    return True
            return False

        else:
            next_link = node.links.get(ch)
            if next_link:
                return self._recurSearch(next_link, word[1:])
            return False

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        return self._recurSearch(self._root, word)


trie = Trie()
trie.add('baby')
trie.add('ball')
trie.add('tree')
trie.add('trie')

print('baby', trie.search('baby'))
print('ba..', trie.search('ba..'))
print('.ree', trie.search('.ree'))
print('nocope', trie.search('nocope'))
