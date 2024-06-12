function createCounter(n: number): () => number {
    let prev: number = n
    return function() {
        prev += 1
        return prev-1
    }
}


