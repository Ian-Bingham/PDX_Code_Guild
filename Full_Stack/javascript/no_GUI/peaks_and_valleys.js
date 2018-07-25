// peaks_and_valleys.js 7/24/18

function peaks(num_list) {
    let peaks_indices = [];
    for (let i=0; i < num_list.length - 1; i++) {
        if (i != 0 || i != num_list.length - 1) {
            if (num_list[i] > num_list[i - 1] && num_list[i] > num_list[i + 1]) {
                peaks_indices.push(i);
            }
        }
    }
    return peaks_indices;
}

function valleys(num_list) {
    let valleys_indices = [];
    for (let i=0;  i < num_list.length - 1; i++) {
        if (i != 0 || i != num_list.length - 1) {
            if (num_list[i] < num_list[i - 1] && num_list[i] < num_list[i + 1]) {
                valleys_indices.push(i);
            }
        }
    }
    return valleys_indices;
}

function peaks_and_valleys(num_list) {
    let pv_indices = peaks(num_list).concat(valleys(num_list));
    pv_indices.sort(function(a, b) {return a - b});
    return pv_indices;
}

let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9];
alert(`Peak indices at: ${peaks(data)}`);
alert(`Valley indices at: ${valleys(data)}`);
alert(`Peak and Valley indices at: ${peaks_and_valleys(data)}`);