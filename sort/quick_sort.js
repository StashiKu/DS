let arr = [3,14,1,7,9,8,11,6,4,2];

function choosePivot(arr, low, high) {
  const mid = Math.floor((low + high) / 2);

  // Compare the three elements and return the median value
  if (arr[low] <= arr[mid] && arr[low] <= arr[high]) {
    if (arr[mid] <= arr[high]) {
      return mid;
    } else {
      return high;
    }
  } else if (arr[mid] <= arr[low] && arr[mid] <= arr[high]) {
    if (arr[low] <= arr[high]) {
      return low;
    } else {
      return high;
    }
  } else {
    if (arr[low] <= arr[mid]) {
      return low;
    } else {
      return mid;
    }
  }
}

function quickSort(arr) {
    if (arr.length < 2) {
        return arr;
    }

    const pivot = arr[0];
    const left = [];
    const right = [];

    for (let i = 1; i < arr.length; i++) {
        if (pivot > arr[i]) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    return quickSort(left).concat(pivot, quickSort(right));
}

quickSort(arr);
