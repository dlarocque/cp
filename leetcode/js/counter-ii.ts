type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let cnt = init
    return {
        increment: () => ++cnt,
        decrement: () => --cnt,
        reset: () => {
            cnt = init;
            return cnt;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
