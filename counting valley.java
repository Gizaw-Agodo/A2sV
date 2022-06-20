function countingValleys(n, s) {
     const min = 2;
     const max = 1000000;
     s = (typeof s === "string") ? s.split('') : s;
     // ["U", "D", "D", "D", "U", "D", "U", "U"] 
 
     // check if s meets the requirements
     if (s.length >= min
          && s.length <= max
          && n === parseInt(n, 0)
          && n >= min
          && n <= max 
          && n === s.length) {
          
          // converting the array steps to integers
          s = s.map(steps => ((steps === "U") ? 1 : -1));
          // [1, -1, -1, -1, 1, -1, 1, 1]
          
          let path = 0; 
          for(let i in s) {
               path += s[i];
               //the man in the forest
          } 
