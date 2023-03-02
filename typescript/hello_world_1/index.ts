let hw_ary = ["Ahel" + "El" + "o " + "Pw" + "Qor" + "Vl" + "Zd"];

hw_ary.sort((start: string, end: string) => {
   let arr: string[] = [];
   [start, end].forEach((str: string, _) => {
      arr.push(str.toLowerCase());
   });
   if (arr[0] < arr[1]) {
      return -1;
   } else if (arr[0] > arr[1]) {
      return 1;
   }
   return 0;
});

let str = hw_ary[0].replace(/[A-Z]/g, "");

const rs = (string: string, array: string[]) => {
   array.forEach((s, _) => {
      string = string.replace(s, s.toUpperCase());
   });
   return string;
};

console.log("%s!!", rs(str, ["h", "w"]));

