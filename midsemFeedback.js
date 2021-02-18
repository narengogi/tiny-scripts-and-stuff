// All the commented out code should have been technically working, I tried replacing setTimeout with onload, but that doesnt seem to work either
//This script works on the individual course page, instead of on the feedback landing page as I orginally intended
// Perhaps I'll fix it for endsem, because I had to write this in like 15 mins, and now I can't access the feedback page

// var subjects = window.frames[0].document.getElementsByTagName('b');

// var i = 0;

// while (i < subjects.length) {
// 	if (subjects[i].firstChild.data !== 'Home') {
// 		if (subjects[i].firstChild.data !== 'Logout') {
// 			subjects[i].click();
// setTimeout(1000);
var fields = window.frames[1].document.getElementsByTagName('input');
var j = 0;
while (j < fields.length - 1) {
	if (fields[j].value === '') {
		fields[j].value = 'Best class ever';
		j++;
	}
}
fields[fields.length - 1].click();
// 		}
// 	}

// 	i++;
// }
