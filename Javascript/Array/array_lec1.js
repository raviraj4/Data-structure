const strings = ['d', 'e', 's', 'f']
// 4*4 = 16 bytes of storage
// push
strings.push('x')
// pop
strings.pop();
strings.pop(); // O(1)
// unshift - O(n) longer!
strings.unshift('v'); // 
// splice (start, delete, item)
strings.splice(3, 0, 'bhadwya'); // O(n) longer
console.log(strings);
// inserting and deleting not really fast
// which is why there are two types of array - i) static and ii) dynamic array

// in javascript and py we have dynamic array which lets us dynamically increase the size 
// while in cpp once size is fixed you may have to create new memory for new items
// for example c++: int a[5] {1,2,3,4,5} you can't have a sixth element

