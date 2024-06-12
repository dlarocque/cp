type F = (x: number) => number;

function compose(functions: F[]): F {
    if (functions.length === 0) {
        return (x: number) => x;
    } else {
        return (x: number) => {
            var func = functions[0];
            let comp = compose(functions.slice(1));
            return func(comp(x));
        }
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 
 compose([f, h, g])
 
 function(x: number) => functions[0](comp(x))
 comp(x) = functions[1](comp(x))
 */
