document.getElementById("index1").addEventListener('click', function () {
	window.location = './main.html';
});

let status=1;
let middle_status=1;

function judje_color_and_display() {
	if (status==1)
	{
		document.getElementById("btn1").style.color = "#272727";
		document.getElementById("btn2").style.color = "#7B7B7B";
		document.getElementById("btn3").style.color = "#7B7B7B";
		document.getElementById("btn4").style.color = "#7B7B7B";
		document.getElementById("right_main_block1").style.display="flex";
		document.getElementById("right_main_block2").style.display="none";
		document.getElementById("right_main_block3").style.display="none";
		document.getElementById("right_main_block4").style.display="none";
	}
	else if (status==2)
	{
		document.getElementById("btn1").style.color = "#7B7B7B";
		document.getElementById("btn2").style.color = "#272727";
		document.getElementById("btn3").style.color = "#7B7B7B";
		document.getElementById("btn4").style.color = "#7B7B7B";
		document.getElementById("right_main_block1").style.display="none";
		document.getElementById("right_main_block2").style.display="flex";
		document.getElementById("right_main_block3").style.display="none";
		document.getElementById("right_main_block4").style.display="none";
	}
	else if (status==3)
	{
		document.getElementById("btn1").style.color = "#7B7B7B";
		document.getElementById("btn2").style.color = "#7B7B7B";
		document.getElementById("btn3").style.color = "#272727";
		document.getElementById("btn4").style.color = "#7B7B7B";
		document.getElementById("right_main_block1").style.display="none";
		document.getElementById("right_main_block2").style.display="none";
		document.getElementById("right_main_block3").style.display="flex";
		document.getElementById("right_main_block4").style.display="none";
	}
	else if (status==4)
	{
		document.getElementById("btn1").style.color = "#7B7B7B";
		document.getElementById("btn2").style.color = "#7B7B7B";
		document.getElementById("btn3").style.color = "#7B7B7B";
		document.getElementById("btn4").style.color = "#272727";
		document.getElementById("right_main_block1").style.display="none";
		document.getElementById("right_main_block2").style.display="none";
		document.getElementById("right_main_block3").style.display="none";
		document.getElementById("right_main_block4").style.display="flex";
	}
	else
	{
		alert("前端的索引值出錯");
	}
}

function judje_middle_color_and_display() {
	if (middle_status==1)
	{
		document.getElementById("middle_title1").style.color = "#272727";
		document.getElementById("middle_title2").style.color = "#7B7B7B";
		document.getElementById("middle_title1_info").style.display="flex";
		document.getElementById("middle_title2_info").style.display="none";
	}
	else if (middle_status==2)
	{
		document.getElementById("middle_title1").style.color = "#7B7B7B";
		document.getElementById("middle_title2").style.color = "#272727";
		document.getElementById("middle_title1_info").style.display="none";
		document.getElementById("middle_title2_info").style.display="flex";
	}
	else
	{
		alert("middle前端的索引值出錯");
	}
}

judje_middle_color_and_display();
judje_color_and_display();

document.getElementById("btn1").addEventListener('click', function () {
	status=1;
  	judje_color_and_display();
});

document.getElementById("btn2").addEventListener('click', function () {
	status=2;
  	judje_color_and_display();
});

document.getElementById("btn3").addEventListener('click', function () {
	status=3;
  	judje_color_and_display();
});

document.getElementById("btn4").addEventListener('click', function () {
	status=4;
  	judje_color_and_display();
});

document.getElementById("middle_title1").addEventListener('click', function () {
	middle_status=1;
  	judje_middle_color_and_display();
});

document.getElementById("middle_title2").addEventListener('click', function () {
	middle_status=2;
  	judje_middle_color_and_display();
});