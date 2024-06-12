type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const transformedArr: number[] = [];
    arr.forEach((elem, idx) => {
        const res = fn(elem, idx);
        if (res) {
            transformedArr.push(elem);
        }
    });
    return transformedArr;
};
