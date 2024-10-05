class HashMap {
  constructor() {
    this.buckets = new Array(16).fill().map(() => []);
    this.size = 0;
    this.loadFactor = 0.75;
  }

  multiplicativeHash(key) {
    // Use prime number to generate a random* number
    const prime = 31;
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = prime * hash * key;
    }

    return Math.abs(hash) % this.buckets.length;
  }

  simpleHash(key) {
    // Sum all the ASCII values of characters in key and take modulo with bucket length
    let total = 0;
    for (let i = 0; i < key.length; i++) {
      total += key.charCodeAt(i);
    }

    return total % this.buckets.length;
  }

  djb2Hash(key) {
    let hash = 5381;
    for (let i = 0; i < key.length; i++) {
      hash = (hash << 5) + hash + key.charCodeAt(i);
    }

    return hash;
  }

  set(key, value) {
    const index = this.simpleHash(key);
    const bucket = this.buckets[index];

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket[i][1] = value;
        return;
      }
    }

    bucket.push([key, value]);
    this.size++;
  }

  get(key, value) {
    const index = this.simpleHash(key);
    const bucket = this.buckets[index];

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        return bucket[i][1];
      }
    }

    return undefined;
  }
}

const hashMap = new HashMap();
hashMap.set("key", "value");
console.log(hashMap.get("key"));
