// t/c = O(nlogn)
// s/c = O(n)

function merge(left, right) {
    let arr = []

    while (left.length && right.length) {
        if (left[0] < right[0]) {
            arr.push(left.shift())
        } else {
            arr.push(right.shift())
        }
    }

    console.log('Результат: ' + arr);

    return [ ...arr, ...left, ...right ]
}

function mergeSort(array) {
  if(array.length < 2){
    return array
  }

  const half = array.length / 2

  const left = array.splice(0, half)

  console.log('Слева:' + left);
  console.log('Справа:' + array);

  return merge(mergeSort(left),mergeSort(array))
}

array = [3, 5, 1, 6, 9, 8, 2];
console.log(mergeSort(array));