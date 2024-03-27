let arr = [3,14,1,7,9,8,11,6,4,2];

function comb_sort(arr) {
    const l = arr.length;
    const factor = 1,247;
    let gapFactor = l / factor;

    while (gapFactor > 1) {
        const gap = Math.round(gapFactor);

        for (i = 0, j = gap; j < l; i++, j++) {
            if (arr[i] > arr[j]) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }

        gapFactor = gapFactor / factor;
    }

    return arr
}
