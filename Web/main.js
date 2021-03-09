let but_currency = ['currency_usa_text', 'currency_eur_text', 'currency_rub_text', 'currency_bel_text',
'term_text_1', 'term_text_3', 'term_text_6', 'term_text_11', 'term_text_15', 'term_text_20', 'term_text_30',
'return_text_1', 'return_text_2', 'rate_text_1', 'rate_text_2',
'currency_usa_text_1', 'currency_eur_text_1', 'currency_rub_text_1',
'def_text_1', 'def_text_2','credit_potr_text_1', 'cred_text_1', 'cred_text_2', 'cred_text_3'
]
let but_res = ["Американский доллар", "Евро", "Российский рубль", "Белорусский рубль",
'1 месяц', '3 месяца', '6 месяцев', '1 год', '1.5 года', '2 года', '3 года',
'Безотзывной', 'Отзывной', 'Фиксированная', 'Плавающая',
"Американский доллар", "Евро", "Российский рубль", 'Покупка', 'Продажа', 'Потребительский', 'На развитие',
'На автомобиль', 'На жилье'
]

setTimeout(() => {
	document.getElementById('Dep_pages').style.display = 'block'
	document.getElementById('btn_checked').style.display = 'block'
	document.getElementById('btn_checked_1').style.display = 'block'
	document.getElementById('btn_checked_2').style.display = 'block'
}, 1500)

for (let i = 0; i < but_currency.length; i++) {
	if (i < 4) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_value_of_deposits').value = but_res[i];
		}
	}
	else if (i == 11 || i == 12) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_return_of_deposits').value = but_res[i];
		}
	}
	else if (i == 13 || i == 14) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_type_of_deposits').value = but_res[i];
		}
	}
	else if (i > 14 && i < 18) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_currency_value').value = but_res[i];
		}
	}
	else if(i >= 18 && i < 20) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_currency_def').value = but_res[i];
		}
	}
	else if (i == 20 ) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_credit_potr').value = but_res[i];
		}
	}
	else if (i >= 21) {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_credit_def').value = but_res[i];
		}
	}
	else {
		document.getElementById(but_currency[i]).onclick = function() {
		document.getElementById('input_term_of_deposits').value = but_res[i];
		}
	}
}

// document.getElementById('currency_usa_text').onclick = function() {
// 	document.getElementById('input_value_of_deposits').value = "Американский доллар";
// }

// document.getElementById('currency_eur_text').onclick = function() {
// 	document.getElementById('input_value_of_deposits').value = "Евро";
// }

// document.getElementById('currency_rub_text').onclick = function() {
// 	document.getElementById('input_value_of_deposits').value = "Российский рубль";
// }

// document.getElementById('currency_bel_text').onclick = function() {
// 	document.getElementById('input_value_of_deposits').value = "Белорусский рубль";
// }


// Вкладки
let tab;
let tabContent;

let ul_tab;
let ul_content;

window.onload=function () {
	tabContent=document.getElementsByClassName('tabContent');
	tab=document.getElementsByClassName('tab');
	hideTabsContent(1);
	norm=document.getElementsByClassName('norm');
	content=document.getElementsByClassName('content');
	hide(1);
	ul_tab = document.getElementsByClassName('ul_tab');
	ul_content = document.getElementsByClassName("ul_content");
	hide_ul_content(1);
} 

function hideTabsContent(a){
	for (let i =a; i<tabContent.length; i++){
		tabContent[i].classList.remove('show');
		tabContent[i].classList.add('hide');
		tab[i].classList.remove('whiteborder');
	}
}

document.getElementById('tabs').onclick = function(event) {
	let target = event.target;
	if (target.className == 'tab'){
		for (let i=0; i<tab.length; i++){
			if(target == tab[i]){
				showTabsContent(i);
				break;
			}
		}
	}
}

function showTabsContent(b){
	if (tabContent[b].classList.contains('hide')){
		hideTabsContent(0);
		tab[b].classList.add('whiteborder');
		tabContent[b].classList.remove('hide');
		tabContent[b].classList.add('show');
	}
}

// Вкладки 2
let norm;
let content;
function hide(a){
	for (let i =a; i<content.length; i++){
		content[i].classList.remove('old');
		content[i].classList.add('young');
		norm[i].classList.remove('nice');
	}
}

document.getElementById('me').onclick = function(event) {
	let target = event.target;
	if (target.className == 'norm'){
		for (let i=0; i<norm.length; i++){
			if(target == norm[i]){
				show(i);
				break;
			}
		}
	}
}

function show(b){
	if (content[b].classList.contains('young')){
		hide(0);
		norm[b].classList.add('nice');
		content[b].classList.remove('young');
		content[b].classList.add('old');
	}
}


function hide_ul_content(a) {
	for (let i = a; i < ul_tab.length; i++) {
		ul_tab[i].classList.remove("whiteboredr");
		ul_content[i].classList.remove("show_ul_content");
		ul_content[i].classList.add("hide_ul_content");
	}
}
document.getElementById('ultabs').onclick = function(event) {
	let target = event.target;
	if (target.className == 'ul_tab') {
		for (let i = 0; i < ul_tab.length; i++) {
			if (target == ul_tab[i]) {
				show_ul_content(i);
				break;
			}
		}
	} 
}

function show_ul_content(b) {
	if (ul_content[b].classList.contains("hide_ul_content")) {
		hide_ul_content(0);
		ul_tab[b].classList.add("whiteboredr");
		ul_content[b].classList.add("show_ul_content");
		ul_content[b].classList.remove("hide_ul_content");
	}
}

const btn = document.getElementById('btn');
const nav = document.getElementById('nav');

btn.addEventListener('click', () => {
	nav.classList.toggle('active');
	btn.classList.toggle('active');
})

// Контент меню
// создание функции для того чтобы не переписывать несколько раз
function ShowContent(li, content) {
	const ser_1 = document.getElementById(li);
	const ser_con_1 = document.getElementById(content)
	ser_1.addEventListener('mouseenter', () => {
		ser_con_1.classList.add('ser_active');
	})
	ser_1.addEventListener('mouseleave', () => {
		ser_con_1.classList.remove('ser_active');
	})

}
// Переменные для первого цикла
done = "done";
done_content = "done_content";

done_incr = 0;
done_content_incr = 0;

for (let i = 0; i < 64; i++) {
	ShowContent(done, done_content)
	done_incr += 1;
	done_content_incr += 1;
	done = "done"; // переприсваивание переменных, так как при следующем действии будет добавляться не 2 а 12, т.к. программа считает, что 12 это строка 
	done_content = "done_content";
	done += done_incr;
	done_content += done_content_incr;
}

fonts_name = ['Italic', 'Verdana', 'Georgia', 'Courier New']

// let modal = document.getElementById('mymodal');
// 		let img = document.getElementById('myImg');
// 		let modalIMG = document.getElementById('img01');
// 		let captionText = document.getElementById('caption');

// 		img.onclick = function() {
// 			modal.style.display = 'block'
// 			modalIMG.src = this.src;
// 			captionText.innerHTML = this.alt
// 		}
// 		let span = document.getElementsByClassName('close')[0];
// 		span.onclick = function () {
// 			modal.style.display = 'none';
// 		}

// for (let i = 0; i < 4; i++) {
// document.getElementById('fonts_btn').onclick = function() {
// 	if (document.getElementById('fonst_input').value == "Italic") {
// 		for (let i = 0; i < 163; i++) {
// 			document.querySelectorAll("p")[i].style.cssText = 'font-family:Itaic'
// 		}
// 		for (let i = 0; i < 86; i++) {
// 			document.querySelectorAll("li")[i].style.cssText = 'font-family:Itaic'
// 		}
// 		for (let i = 0; i < 16; i++) {
// 			document.querySelectorAll("a")[i].style.cssText = 'font-family:Itaic'
// 		}
// 	}
// 	if (document.getElementById('fonst_input').value == "Verdana") {
// 		for (let i = 0; i < 163; i++) {
// 			document.querySelectorAll("p")[i].style.cssText = 'font-family:Verdana'
// 		}
// 		for (let i = 0; i < 86; i++) {
// 			document.querySelectorAll("li")[i].style.cssText = 'font-family:Verdana'
// 		}
// 		for (let i = 0; i < 16; i++) {
// 			document.querySelectorAll("a")[i].style.cssText = 'font-family:Verdana'
// 		}
// 	}
// 	if (document.getElementById('fonst_input').value == "Georgia") {
// 		for (let i = 0; i < 163; i++) {
// 			document.querySelectorAll("p")[i].style.cssText = 'font-family:Georgia'
// 		}
// 		for (let i = 0; i < 86; i++) {
// 			document.querySelectorAll("li")[i].style.cssText = 'font-family:Georgia'
// 		}
// 		for (let i = 0; i < 16; i++) {
// 			document.querySelectorAll("a")[i].style.cssText = 'font-family:Georgia'
// 		}
// 	}
// 	if (document.getElementById('fonst_input').value == "Courier New") {
// 		for (let i = 0; i < 163; i++) {
// 			document.querySelectorAll("p")[i].style.cssText = 'font-family:Courier New'
// 		}
// 		for (let i = 0; i < 86; i++) {
// 			document.querySelectorAll("li")[i].style.cssText = 'font-family:Courier New'
// 		}
// 		for (let i = 0; i < 16; i++) {
// 			document.querySelectorAll("a")[i].style.cssText = 'font-family:Courier New'
// 			document.querySelectorAll("a")[i].style.cssText = 'font-size:20'
// 		}
// 	}
// }
// }

// Writing text
// let el = document.getElementById('str');
// 	let string = 'vИзменять размер фотографий еще никогда не было так просто.'
// 	let str = string.split(''); 
// 	(function animate() {
// 			str.length > 0 ? el.innerHTML += str.shift() : clearTimeout(running); // eсли ... то к элементу прибавлям первый удельный символ из массива; cleartimeout останавливает выполнение функции setTimeout
// 			let running = setTimeout(animate, 10); // скорость выполнения
// 		})();
