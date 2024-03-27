
/* Javascript Program for Bad Character Heuristic of Boyer
Moore String Matching Algorithm */
let NO_OF_CHARS = 256;

// A utility function to get maximum of two integers
function max (a,b)
{
	return (a > b)? a: b;
}

// The preprocessing function for Boyer Moore's
// bad character heuristic
function badCharHeuristic(str,size)
{
    let badchar = new Array(NO_OF_CHARS);
	// Initialize all occurrences as -1
	for (let i = 0; i < NO_OF_CHARS; i++)
		badchar[i] = -1;

	// Fill the actual value of last occurrence
	// of a character (indices of table are ascii and values are index of occurrence)
	for (i = 0; i < size; i++)
		badchar[ str[i].charCodeAt(0) ] = i;

	return badchar;
}

function search(txt,pat) {
	let patternLength = pat.length;
	let txtLength = txt.length;

	let badchar = badCharHeuristic(pat, patternLength);

	let i = 0;

	while (i <= (txtLength - patternLength)) {
		let j = patternLength - 1;

		while(j >= 0 && pat[j] == txt[i+j])
		    j--;

		if (j < 0) {
			document.write("Patterns occur at shift = " + i);

			//txt[s+m] is character after the pattern in text
			i += (i + patternLength < txtLength) ? patternLength - badchar[txt[i + patternLength].charCodeAt(0)] : 1;
		}

		else
			i += max(1, j - badchar[txt[i+j].charCodeAt(0)]);
	}
}

let txt="ABAAABCD".split("");
let pat = "ABC".split("");
search(txt, pat);
