#include <list>
#include <unordered_map>
#include <utility>

class LRUCache {
    int cap;
    std::list<std::pair<int, int>> cache; // front = most recently used.
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> pos;

public:
    LRUCache(int capacity) : cap(capacity) {}

    int get(int key) {
        auto it = pos.find(key);
        if (it == pos.end()) return -1;
        // Move the node to the front without invalidating iterators.
        cache.splice(cache.begin(), cache, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = pos.find(key);
        if (it != pos.end()) {
            it->second->second = value;
            cache.splice(cache.begin(), cache, it->second);
            return;
        }
        if ((int)cache.size() == cap) {
            // Evict the least recently used entry from the back.
            pos.erase(cache.back().first);
            cache.pop_back();
        }
        cache.emplace_front(key, value);
        pos[key] = cache.begin();
    }
};
