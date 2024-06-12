function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const transformedArr: number[] = [];
    arr.forEach((elem, idx) => {
        transformedArr[idx] = fn(elem, idx); 
    });
    return transformedArr;
};
